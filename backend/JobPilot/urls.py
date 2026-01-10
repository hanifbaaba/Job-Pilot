from .views import CreateJobView, ApplyJobView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'create-job', CreateJobView, basename="create-job")
router.register(r'apply-job', ApplyJobView, basename='apply-job')
urlpatterns = router.urls

