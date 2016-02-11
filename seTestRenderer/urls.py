from django.conf.urls import url
from seTestRenderer.views import StateList

urlpatterns = [
    url(r'^$', StateList, name="home"),
]
