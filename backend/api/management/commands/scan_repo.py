import os
import json
import fnmatch
from django.core.management.base import BaseCommand
from api.models import CandidateFile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load external config once
CONFIG_FILE = os.path.abspath(os.path.join(BASE_DIR, "../scan_ignore.json"))
with open(CONFIG_FILE, "r") as f:
    IGNORE_CONFIG = json.load(f)


class Command(BaseCommand):
    help = "Scan a local repo and save files as candidate snippets, tech-aware, ignores irrelevant files"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            required=True,
            help="Path to the local repo to scan",
        )
        parser.add_argument(
            "--tech",
            type=str,
            required=True,
            help="Technology stack to determine ignore/include patterns (e.g., 'python', 'javascript')",
        )

    def handle(self, *args, **options):
        repo_path = options["path"]
        tech = options.get("tech", "default")

        # Verify path exists
        if not os.path.isdir(repo_path):
            self.stderr.write(self.style.ERROR(f"The path {repo_path} is not a valid directory."))
            return

        # Get the config for this tech
        config = IGNORE_CONFIG.get(tech, {})
        ignore_dirs = set(config.get("ignore_dirs", []))
        ignore_files = config.get("ignore_files", [])
        include_exts = config.get("include_extensions", [])
        include_paths = config.get("include_paths", [])

        # Walk the repo
        for root, dirs, files in os.walk(repo_path):
            # Skip ignored directories in-place
            dirs[:] = [d for d in dirs if d not in ignore_dirs]

            for file in files:
                # Skip files matching ignore patterns
                if any(fnmatch.fnmatch(file, pattern) for pattern in ignore_files):
                    continue

                # Check extension
                ext = os.path.splitext(file)[1].lstrip('.').lower()
                if include_exts and ext not in include_exts:
                    continue

                # Optional path filtering
                if include_paths and not any(p in root for p in include_paths):
                    continue

                # Full file path
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, repo_path)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        code = f.read()
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error reading {file_path}: {e}"))
                    continue

                # Save to CandidateFile if not exists
                candidate_file, created = CandidateFile.objects.get_or_create(
                    repo_path=repo_path,
                    file_path=relative_path,
                    defaults={'language': ext or 'unknown', 'code': code}
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added: {relative_path}"))
                else:
                    self.stdout.write(f"Skipped (already exists): {relative_path}")
