
from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from reco.urls import *
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^image/', include('image_app.urls')),
    url(r'^post/', include('create_app.urls')),
    url(r'^blog/', include('blog.urls')),
    path('', include('reco.urls')),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)