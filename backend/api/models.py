from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=80, unique=True)
    synonims = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name

class CodeAsset(models.Model):
    title = models.CharField(max_length=200)
    repository_url = models.URLField(max_length=200)
    root_path = models.CharField(max_length=200, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, related_name='code_assets')

    def __str__(self):
        return self.title

class CodeSnippet(models.Model):
    code_asset = models.ForeignKey(CodeAsset, on_delete=models.CASCADE, related_name='snippets')
    file_path = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    start_line = models.IntegerField()
    end_line = models.IntegerField()
    code = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name='code_snippets', blank=True)
    keywords = models.JSONField(default=list, blank=True)
    subtext = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.code_asset.title} - {self.file_path} ({self.start_line}-{self.end_line})"

class Embeddings(models.Model):
    snippet = models.ForeignKey(CodeSnippet, on_delete=models.CASCADE, related_name='embeddings')
    vector = models.JSONField()


class CandidateFile(models.Model):
    repo_path = models.URLField(max_length=200)
    file_path = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    code = models.TextField() 
    reviewed = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.repo_path} - {self.file_path}"