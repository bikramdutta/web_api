from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime
import json
from django.core.serializers import serialize

#for class based views
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
# every class based view is going to inherit this view class

from .models import Update as UpdateModel

# Create your views here.

def update_model_detail_view(request):
	'''
		GET -- to Retrieve data
	'''
	# return render()
	data = {
		'id' : 1,
		'content' : 'Json Test data',
		'date_published' : datetime.now()
	}

	# Sending back a json response for it to work with REST API
	# return JsonResponse(data)

	json_data = json.dumps(data, default=str)
	return HttpResponse(json_data, content_type='application/json')


# class based view
class JsonCBV(View):

	def get(self, request, *args, **kwargs):
			# return render()
		data = {
			'id' : 1,
			'content' : 'Json Test data',
			'date_published' : datetime.now()
		}

		# Sending back a json response for it to work with REST API
		return JsonResponse(data)

class JsonCBV2(View, JsonResponseMixin):
	def get(self, request, *args, **kwargs):
			# return render()
		data = {
			'id' : 1,
			'content' : 'Json Test data',
			'date_published' : datetime.now()
		}

		return self.render_to_json_response(data)


# class SerializedDetailView(View):
# 	def get(self, request, *args, **kwargs):
# 		obj = UpdateModel.objects.get(id=1)
# 		data = {
# 			'user' : obj.user.username,
# 			'content' : obj.content
# 		}

# 		# Sending back a json response for it to work with REST API
# 		# return JsonResponse(data)

# 		json_data = json.dumps(data, default=str)
# 		return HttpResponse(json_data, content_type='application/json')


# class SerializedListView(View):
# 	def get(self, request, *args, **kwargs):
# 		qs = UpdateModel.objects.all()
# 		data = serialize('json', qs, fields=('user','content'))
		 
# 		# Sending back a json response for it to work with REST API
# 		# return JsonResponse(data)

# 		json_data = json.dumps(data, default=str)
# 		return HttpResponse(data, content_type='application/json')


class SerializedDetailView(View):
	def get(self, request, *args, **kwargs):
		obj = UpdateModel.objects.get(id=1)
		# We have added a serialization method for instance
		# in the model itself.
		json_data = obj.serialize()
		
		return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
	def get(self, request, *args, **kwargs):
		qs = UpdateModel.objects.all()
		# Model Manager is configured to return serialized data for 
		# query set.
		json_data = UpdateModel.objects.all().serialize()
		return HttpResponse(json_data, content_type='application/json')