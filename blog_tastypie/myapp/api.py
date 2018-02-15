from tastypie.resources import ModelResource
from blog_tastypie.myapp.models import Entry


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
