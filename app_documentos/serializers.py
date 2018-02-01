from rest_framework import serializers
from .models import *

class TagSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tag
		field = ('tag_nome',)