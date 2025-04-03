from django import forms
from .models import PersonalInfo, SelfInfo, ProjectInfo, Skill

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['full_name', 'email', 'password', 'profile_image', 'headline']

class SelfInfoForm(forms.ModelForm):
    class Meta:
        model = SelfInfo
        fields = ['short_intro', 'bio', 'achievements_image', 'achievements_desc']

class ProjectInfoForm(forms.ModelForm):
    class Meta:
        model = ProjectInfo
        fields = ['project_title', 'problem_statement', 'feedback', 'github_link']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name']
