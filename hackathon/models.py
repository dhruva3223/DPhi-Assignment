from django.db import models
from django.contrib.auth.models import User

class Hackathon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon/images/')
    hackathon_image = models.ImageField(upload_to='hackathon/images/')
    TYPE_CHOICES = (
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    )
    type_of_submission = models.CharField(max_length=10, choices=TYPE_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.CharField(max_length=50)

class UserHackathon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

class Submission(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    submission_file = models.FileField(upload_to='hackathon/submissions/')
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
