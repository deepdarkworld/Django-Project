from django.db import models

# Create your models here.
class Uploads(models.Model):
    Images = models.ImageField(upload_to="media")
    Texts  = models.TextField()
    
    class Meta:
        verbose_name_plural = "UPLOAD"
        
    def __str__(self):
        return self.Texts
    
