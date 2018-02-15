from django.conf.urls import url, include
from tastypie.api import Api
from blog_tastypie.myapp.api import EntryResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(EntryResource())
v1_api.register(UserResource())

urlpatterns = [
    url(r'^blog/', include('blog_tastypie.myapp.urls')),
    url(r'^api/', include(v1_api.urls)),
]
