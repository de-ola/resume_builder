from django.db import models
from user.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Biodata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="biodata")
    gender_type = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(max_length=10, choices=gender_type, default="Male")
    bio = RichTextField()

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    project_name = models.CharField()
    project_url = models.URLField()