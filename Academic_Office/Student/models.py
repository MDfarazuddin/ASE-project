from django.db import models
# Create your models here.
class Students(models.Model):
    S_id=models.CharField(max_length=10,primary_key=True)
    S_name=models.CharField(max_length=250)
    slug = models.SlugField()
    S_email = models.EmailField(blank=True,default="farazuddin.m17@iiits.in")
    S_password = models.CharField(max_length=50)
    def __str__(self):
    	return self.S_name
