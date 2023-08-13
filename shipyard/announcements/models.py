from django.db import models


class Announcements(models.Model):
    """An announcement to broadcast to community"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    expired_at = models.DateTimeField(db_index=True)

    def __str__(self):
        return self.title
