from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Specializaion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specializaion, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    clinic_address = models.TextField()
    license_number = models.CharField(max_length=11)
    biography = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class AvailableTime(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor} - {self.date} {self.start_time} to {self.end_time}"


class VisitCost(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.doctor}: {self.cost}"



class Comment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    is_visited = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"کاربر {self.name} به دکتر {self.doctor} نظر خود را ثبت کرد"


class Rating(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    product = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField(blank=True, null=True)


class Patient(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    