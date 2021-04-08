from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	# We can choose the fields that we want to add in the model
	# fields = ['tutorial_published',
	# 			'tutorial_content']

	# We add field sets

	fieldsets = [
		('Title/date', {'fields' : ['tutorial_title','tutorial_published']}),
		('Content', {'fields' : ['tutorial_content']})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(Tutorial, TutorialAdmin)

