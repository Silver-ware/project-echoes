from django.core.management.base import BaseCommand
from api.models import CandidateFile

class Command(BaseCommand):
    help = "Delete all CandidateFile entries from the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force deletion without confirmation",
        )

    def handle(self, *args, **options):
        if not options["force"]:
            self.stdout.write(self.style.WARNING(
                "This will permanently delete ALL CandidateFile entries."
            ))
            confirm = input("Are you sure you want to continue? [y/N]: ").strip().lower()

            if confirm not in ("y", "yes"):
                self.stdout.write(self.style.NOTICE("Operation cancelled."))
                return

        deleted_count, _ = CandidateFile.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS(f"Deleted {deleted_count} CandidateFile entries.")
        )
