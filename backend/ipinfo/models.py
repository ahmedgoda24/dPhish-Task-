from django.db import models

# Create your models here.
class IPAddress(models.Model):
   
    ip_address = models.GenericIPAddressField()
    data_info = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address