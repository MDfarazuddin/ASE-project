from django.db import models

# Create your models here.
class Teachers(models.Model):
	T_id = models.CharField(max_length = 15)
	T_name = models.CharField(max_length = 20)
	T_course = models.CharField(max_length = 20,default="not assigned")
	slug = models.SlugField()
	T_email = models.EmailField(default="farazuddin.m17@iiits.in",blank=True)
	T_password=models.CharField(max_length=50)
	def __str__(self):
		return self.T_name
