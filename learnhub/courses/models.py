from django.db import models

# Create your models here.



class Enrollment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    selected_course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DemoClassRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    preferred_date = models.DateField()
    course_interest = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StudentQuestion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    