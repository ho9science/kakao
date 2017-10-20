from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'keyboard', views.KeyboardViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^message$', views.blog_page),
]