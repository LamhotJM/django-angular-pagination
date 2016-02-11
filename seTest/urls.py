from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from seTest import views

api_urlpatterns = [
    url(r'^$', views.StateList.as_view()),
]
urlpatterns = format_suffix_patterns(api_urlpatterns, allowed=['json'])
