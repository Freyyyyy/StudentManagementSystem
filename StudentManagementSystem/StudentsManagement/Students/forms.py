from django import forms
from .models import Student, Grade

class StudentForm(forms.ModelForm):
    enrollment_date = forms.DateField(disabled=True, required=False)
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'email', 'is_active']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade_type', 'score']
