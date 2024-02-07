# models.py

from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=100)
    meet_link = models.CharField(max_length=200, blank=True)
    date_time = models.DateTimeField()

    def _str_(self):
        return self.title
    
# models.py

import uuid

class Meeting(models.Model):
    # ...
    
    def generate_meet_link(self):
        return f'https://meet.google.com/{uuid.uuid4()}'
    
# models.py

class Meeting(models.Model):
    # ...
    
    def save(self, *args, **kwargs):
        if not self.meet_link:
            self.meet_link = self.generate_meet_link()
        super().save(*args, **kwargs)
        