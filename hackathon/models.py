from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = (
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    )

class Hackathon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon/images/')
    hackathon_image = models.ImageField(upload_to='hackathon/images/')
    type_of_submission = models.CharField(max_length=8, choices=TYPE_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.CharField(max_length=30)

class UserHackathon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

class Submission(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='hackathon/submissions/', null=True, blank=True)
    submission_link = models.URLField(null=True, blank=True)
    submission_image = models.ImageField(upload_to='hackathon/submissions/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.hackathon.type_of_submission == 'file':
            self.submission_link = None
            self.submission_image = None
        elif self.hackathon.type_of_submission == 'link':
            self.submission_file = None
            self.submission_image = None
        elif self.hackathon.type_of_submission == 'image':
            self.submission_file = None
            self.submission_link = None
        super().save(*args, **kwargs)