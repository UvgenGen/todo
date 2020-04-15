from django.conf.urls import include, url
from rest_framework import routers

from .api import MessageViewSet
from .views import ToDoView

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    url(r'^$', ToDoView.as_view(), name='message'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]
