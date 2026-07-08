from django.shortcuts import render
from .models import Contact, Project, Skill

def home(request):
    skills_data = Skill.objects.all()
    return render(request, 'portfolio_app/home.html', {
        'skills': skills_data
    })


def projects(request):
    projects_data = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio_app/projects.html', {
        'projects': projects_data
    })


def contact(request):
    success = False
    error = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            success = True
        else:
            error = True

    return render(request, 'portfolio_app/contact.html', {
        'success': success,
        'error': error
    })
