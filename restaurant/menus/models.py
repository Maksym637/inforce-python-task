from django.db import models
from place.models import Restaurant
from users.models import Employee


class Menu(models.Model):
    class Meta:
        db_table = 'menus'
        ordering = ['-id']

    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.CASCADE)
    file_contant = models.FileField(upload_to='content/', null=True)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.restaurant.name


class Vote(models.Model):
    class Meta:
        db_table = 'votes'
        ordering = ['-id']

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.user.username
