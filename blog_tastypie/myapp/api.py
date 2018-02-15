from tastypie.resource impor ModelResource
from myapp.models impot Entry


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
