from django.db import models


class Restaurant(models.Model):
    class Meta:
        db_table = 'restaurants'
        ordering = ['-id']
    
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
