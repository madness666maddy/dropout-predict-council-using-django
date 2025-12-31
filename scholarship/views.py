from django.shortcuts import render, get_object_or_404
from .models import Scholarship
from student.models import Student   # adjust if your app name differs

# Scholarship list page
def scholarship_list(request):
    scholarships = Scholarship.objects.all()
    return render(request, 'scholarship/list.html', {
        'scholarships': scholarships
    })

# Recommendation page
def recommend_scholarship(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    eligible = Scholarship.objects.filter(
        min_marks__lte=student.total_marks,
        max_income__gte=student.family_income
    )

    return render(request, 'scholarship/recommend.html', {
        'student': student,
        'scholarships': eligible
    })
