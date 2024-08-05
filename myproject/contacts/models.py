from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    twitter = models.URLField(blank=True)
    avatar_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
