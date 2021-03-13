from django.db import models
from tastypie.resources import ModelResource
from personalities.models import Personality


class PersonalityResource(ModelResource):
    class Meta:
        queryset = Personality.objects.all()
        resource_name = 'personalities'
