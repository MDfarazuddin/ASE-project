from django.db import models

# Create your models here.
class Students(models.Model):
    S_id=models.CharField(max_length=10,primary_key=True)
    S_name=models.CharField(max_length=250)
    S_grade = models.CharField(max_length=3,blank=True)
    slug = models.SlugField()
    S_email = models.EmailField(blank=True,default="farazuddin.m17@iiits.in")
    def __str__(self):
    	return self.S_name
