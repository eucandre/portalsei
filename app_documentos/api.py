from tastypie.resources import ModelResource
from .models import *

class TagResourse(ModelResource):
	class Meta:
		queryset = Tag.objects.all()