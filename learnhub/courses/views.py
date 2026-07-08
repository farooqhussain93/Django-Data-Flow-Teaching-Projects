from django.shortcuts import render, redirect
from .models import Enrollment, DemoClassRequest, StudentQuestion


def home(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "enrollment":
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            selected_course = request.POST.get("selected_course")

            Enrollment.objects.create(
                name=name,
                email=email,
                phone=phone,
                selected_course=selected_course
            )


        elif form_type == "demo":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            preferred_date = request.POST.get("preferred_date")
            course_interest = request.POST.get("course_interest")

            DemoClassRequest.objects.create(
                name=name,
                phone=phone,
                preferred_date=preferred_date,
                course_interest=course_interest
            )


        elif form_type == "question":
            name = request.POST.get("name")
            email = request.POST.get("email")
            question = request.POST.get("question")

            StudentQuestion.objects.create(
                name=name,
                email=email,
                question=question
            )


        return redirect("home")

    return render(request, "courses/index.html")