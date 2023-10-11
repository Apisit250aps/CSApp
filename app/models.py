from django.db import models

# Create your models here.

DAYS = (
        ("Mon", "Monday"),
        ("Tue", "Tuesday"),
        ("Wed", "Wednesday"),
        ("Thu", "Thursday"),
        ("Fri", "Friday"),
    )


CLASS_YEARS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    )

TERM = (
        (1, 1),
        (2, 2)
    )


class SchoolYear(models.Model):

    year = models.IntegerField()

    def __str__(self):

        return f"ปีการศึกษา {self.year}"


class TimeTable(models.Model):

    year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    
    term = models.IntegerField(choices=TERM)
    class_year = models.IntegerField(choices=CLASS_YEARS)

    date = models.CharField(choices=DAYS,
        max_length=3)

    time_from = models.CharField()
    time_to = models.CharField()

    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=255)
    class_room = models.IntegerField()
    teacher = models.CharField(max_length=255)
