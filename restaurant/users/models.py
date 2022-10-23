from django.db import models


class Role(models.Model):
    class Meta:
        db_table = 'roles'
        ordering = ['-id']
    

    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    

class User(models.Model):
    class Meta:
        db_table = 'users'
        ordering = ['-id']
    
    roles = models.ManyToManyField(Role, blank=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    phone = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

class Employee(models.Model):
    class Meta:
        db_table = 'employees'
        ordering = ['-id']
    
    employee_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username