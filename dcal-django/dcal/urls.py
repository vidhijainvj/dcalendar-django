
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from event import views

router = routers.DefaultRouter()
router.register(r'events',views.eventView,'event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

