from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    students = models.ManyToManyField(Student, related_name='subjects')

    def __str__(self):
        return f"{self.code} - {self.name}"


class Grade(models.Model):
    GRADE_TYPES = [
        ('Activity', 'Activity'),
        ('Quiz', 'Quiz'),
        ('Exam', 'Exam'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_type = models.CharField(max_length=10, choices=GRADE_TYPES)
    score = models.FloatField()

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.subject.name} - {self.grade_type}"
