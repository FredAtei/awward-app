from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='Home'),
    url(r'^profile/(?P<profile_id>\d+)', views.profile, name='profile'),
    url(r'^new/profile/$', views.addprofile, name='new-profile'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^project/(\d+)$', views.projects, name='project'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)