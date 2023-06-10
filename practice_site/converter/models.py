from django.db import models

# Create your models here.
class MyImageModel(models.Model):
    id = models.AutoField(primary_key=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.image.name.replace('images/', "")
