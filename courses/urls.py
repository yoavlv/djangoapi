from django.urls import path , include
from . import views
from rest_framework import routers

# Get request get something and show it on the screen
# Post request Post something on the DB

router = routers.DefaultRouter()
router.register("courses", views.CourseView)

urlpatterns = [
    path("", include(router.urls))



]
