from django.db import models

# Create your models here.
from django.db import models

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profiles/')
    headline = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class SelfInfo(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    short_intro = models.TextField()
    bio = models.TextField()
    achievements_image = models.ImageField(upload_to='achievements/', null=True, blank=True)
    achievements_desc = models.TextField()

    def __str__(self):
        return f"Self Info of {self.personal_info.full_name}"

class ProjectInfo(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    problem_statement = models.TextField()
    feedback = models.TextField()
    github_link = models.URLField()

    def __str__(self):
        return self.project_title

class Skill(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name
