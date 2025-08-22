
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.inicio, name="inicio"),
path('contacto/', views.contacto, name="contacto"),
path('crear/', views.crear_obituario, name='crear_obituario'),
path('listar/', views.listar_obituarios, name='listar_obituarios'),
path('detalle/<int:id>/', views.ver_obituario, name='ver_obituario'),
path('nosotros/', views.nosotros, name='nosotros'),
path('blog/', views.blog_list, name="blog"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)