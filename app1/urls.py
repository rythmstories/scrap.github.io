from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import webs, check

urlpatterns = [
    url(r'websyellow/',webs, name="create"),
    url(r'check',check, name="create"),

]






