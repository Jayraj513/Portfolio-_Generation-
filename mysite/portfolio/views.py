from django.shortcuts import redirect, render
from .forms import PersonalInfoForm, SelfInfoForm, ProjectInfoForm, SkillForm

def register(request):
    if request.method == 'POST':
        personal_info_form = PersonalInfoForm(request.POST, request.FILES)
        self_info_form = SelfInfoForm(request.POST)
        project_info_form = ProjectInfoForm(request.POST)
        skill_form = SkillForm(request.POST)

        if personal_info_form.is_valid() and self_info_form.is_valid() and project_info_form.is_valid() and skill_form.is_valid():
            personal_info = personal_info_form.save()
            self_info = self_info_form.save(commit=False)
            self_info.personal_info = personal_info
            self_info.save()

            project_info = project_info_form.save(commit=False)
            project_info.personal_info = personal_info
            project_info.save()

            skill = skill_form.save(commit=False)
            skill.personal_info = personal_info
            skill.save()

            return redirect('success')
    else:
        personal_info_form = PersonalInfoForm()
        self_info_form = SelfInfoForm()
        project_info_form = ProjectInfoForm()
        skill_form = SkillForm()

    return render(request, 'portfolio/register.html', {
        'personal_info_form': personal_info_form,
        'self_info_form': self_info_form,
        'project_info_form': project_info_form,
        'skill_form': skill_form,
    })

def success(request):
    return render(request, 'success.html')

def form(request):
    return render(request, 'form.html')