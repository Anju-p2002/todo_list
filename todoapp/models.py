from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_completed =models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

