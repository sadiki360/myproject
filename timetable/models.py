from django.db import models

class TimeTable(models.Model):
    DAY_CHOICES = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
    ]
    SESSION_CHOICES = [
        ('Matin', 'Matin (08:30 - 12:30)'),
        ('Soir', 'Soir (14:00 - 18:00)'),
    ]
    GROUP_CHOICES = [
        ('AD-S1', 'AD - S1'),
        ('AD-S2', 'AD - S2'),
        ('IDAI-S1', 'IDAI - S1'),
        ('IDAI-S2', 'IDAI - S2'),
    ]

    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    session = models.CharField(max_length=10, choices=SESSION_CHOICES)
    group = models.CharField(max_length=10, choices=GROUP_CHOICES)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.day} - {self.session} - {self.group} : {self.subject}"