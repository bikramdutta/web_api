from django.conf import settings
from django.db import models
from django.core.serializers import serialize
import json

# Create your models here.
def upload_update_image(instance, filename):
	return "updates/{user}/{filename}".format(user=instance.user, filename = filename)

class UpdateQuerySet(models.QuerySet):
	 # def serialize(self):
	 # 	qs = self
	 # 	return serialize('json', qs, fields=('user', 'content','image'))

	 def serialize(self):
	 	qs_value_list = list(self.values('user','content','image'))
	 	return json.dumps(qs_value_list)

class UpdateManager(models.Manager):
	def get_queryset(self):
		return UpdateQuerySet(self.model, using=self._db)

# 'Update' model. like updates from the user. like I have updated a profile pic or discription.
class Update(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to=upload_update_image,
		blank=True, null=True)
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)

	objects = UpdateManager()

	def __str__(self):
		return 'Update - ' + self.content or ""

	def serialize(self):
		json_data = serialize('json', [self], fields=('user', 'content','image'))
		struct = json.loads(json_data)
		data = json.dumps(struct[0]['fields'])
		return data
