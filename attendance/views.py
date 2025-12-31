from django.shortcuts import render, redirect
from students.models import Student
from .models import Attendance

def mark_attendance(request):
    students = Student.objects.all()

    if request.method == "POST":
        for student in students:
            status = request.POST.get(str(student.id))
            Attendance.objects.create(
                student=student,
                present=True if status == "present" else False
            )
        return redirect('mark_attendance')

    return render(request, 'attendance/mark.html', {
        'students': students
    })
