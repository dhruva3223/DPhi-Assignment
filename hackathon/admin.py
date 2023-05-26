from django.contrib import admin
from .models import Hackathon, UserHackathon, Submission
# Register your models here.

admin.site.register(Hackathon)
admin.site.register(UserHackathon)
admin.site.register(Submission)