# # # from django.db import models

# # # # Create your models here.
# # from django.db import models

# # class Category(models.Model):
# #     name = models.CharField(max_length=100)

# #     def __str__(self):
# #         return self.name


# # class Task(models.Model):
# #     title = models.CharField(max_length=200)
# #     time = models.CharField(max_length=100)
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# #     is_completed = models.BooleanField(default=False)

# #     def __str__(self):
# #         return self.title

# from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     due_date = models.CharField(max_length=100)
#     is_completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    time = models.TimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title