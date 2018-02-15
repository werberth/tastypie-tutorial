from django.conf.urls import url, include
from blog_tastypie.myapp.api import EntryResource

entry_resource = EntryResource()

urlpatterns = [
    url(r'^blog/', include('blog_tastypie.myapp.urls')),
    url(r'^api/', include(entry_resource.urls)),
]
