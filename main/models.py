from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=7, decimal_places=5)
    max_student = models.IntegerField()
    lifetime = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Student(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

