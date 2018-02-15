from django.conf.urls import url, include
from tastypie.api import Api
from blog_tastypie.myapp.api import EntryResource

v1_api = Api(api_name='v1')
entry_resource = EntryResource()

urlpatterns = [
    url(r'^blog/', include('blog_tastypie.myapp.urls')),
    url(r'^api/', include(entry_resource.urls)),
]
