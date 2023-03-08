from django.db import models
from user.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Biodata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="biodata")
    profile_pic = models.ImageField(upload_to='user/pics/', blank=True, null=True)
    gender_type = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(max_length=10, choices=gender_type, default="Male")
    whatsapp_url = models.URLField(blank=True, null=True)
    discord_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    telegram_url = models.URLField(blank=True, null=True)
    bio = RichTextField(blank=True, null=True)

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    project_name = models.CharField(max_length=100000, blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    project_description = RichTextField(blank=True, null=True)