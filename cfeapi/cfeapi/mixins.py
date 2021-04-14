from django.http import JsonResponse

class JsonResponseMixin(object):

	def render_to_json_response(self, context, **response_kwargs):
		return JsonResponse(self.get_data(context))

	def get_data(self,context):
		# modify the passed context(variable) in some format
		return context

