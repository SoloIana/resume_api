from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from phone_field import PhoneField


class Resume(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        DISABLED = 'disabled', 'Disabled'

    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    grade = models.IntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(10), MinValueValidator(1)],
    )
    specialty = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    phone = PhoneField()
    email = models.EmailField()


class EducationRecord(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='education',
    )
    place = models.CharField(max_length=300)
    degree = models.CharField(max_length=30)
    graduation_year = models.IntegerField(null=True)


class WorkRecord(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='experience',
    )
    place = models.CharField(max_length=300)
    specialty = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class PortfolioRecord(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='portfolio',
    )
    title = models.CharField(max_length=300)
    description = models.TextField()
    link = models.URLField()
    created_at = models.DateTimeField()
