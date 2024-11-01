from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, blank=False)
    published_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(
        max_length=20, unique=True, blank=False, null=False
    )
    pages = models.PositiveIntegerField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} (by {self.author})"
