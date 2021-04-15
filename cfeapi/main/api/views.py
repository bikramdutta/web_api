from main.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse


class UpdateModelDetailAPIView(View):
	'''
	Retrieve
	Update
	Delete
	---> object
	'''

	def get(self, request, *args, **kwargs):
		obj = UpdateModel.objects.get(id=1)
		# We have added a serialization method for instance
		# in the model itself.
		json_data = obj.serialize()		
		return HttpResponse(json_data, content_type='application/json')

	def put(self, request,*args, **kwargs):

		return HttpResponse({}, content_type='application/json')

	def delete(self, request, *args, **kwargs):

		return HttpResponse({}, content_type='application/json')


class UpdateModelListAPIView(View):
	'''
	List View
	Create View
	'''


	def get(self, request):
		qs = UpdateModel.objects.all()
		json_data = qs.serialize()

		return HttpResponse(json_data, content_type='application/json')

	def post(self, request):

		return HttpResponse({}, content_type='application/json')

	def put(self, request):

		return HttpResponse({}, content_type='application/json')
	def delete(self, request):

		return HttpResponse({}, content_type='application/json')