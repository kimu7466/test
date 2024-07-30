from django.db import models

# Create your models here.
class BaseClass(models.Model):
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True

class staff(BaseClass):
    user = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)

    def __str__(self):
        return f"{self.user}"