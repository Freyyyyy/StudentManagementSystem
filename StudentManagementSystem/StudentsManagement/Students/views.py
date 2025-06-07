from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Subject, Grade
from .forms import StudentForm, GradeForm


def student_list(request):
    students = Student.objects.all()
    return render(request, 'app/student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    grades = Grade.objects.filter(student=student)
    subjects = student.subjects.all()
    return render(request, 'app/student_detail.html', {'student': student, 'grades': grades, 'subjects': subjects})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'app/student_create.html', {'form': form})


def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=grade.student.pk)
    else:
        form = GradeForm(instance=grade)
    return render(request, 'app/grade_form.html', {'form': form})