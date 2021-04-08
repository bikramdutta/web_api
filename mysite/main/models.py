from django.db import models
from datetime import datetime
# Create your models here.
# create a class which inherits models.Model
# models.Model - generic model class, which has inbuilt attributes and stuff to function as a model

class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField('date published', default = datetime.now())

	def __str__(self):
		return 'Tutorial- ' + self.tutorial_title


