from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, PatientViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns =[
    path('api/', include(router.urls))
]