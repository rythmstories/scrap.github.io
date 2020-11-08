from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import webs, suggestionyellow

urlpatterns = [
    url(r'websyellow/',webs, name="create"),
    url(r'suggestion',suggestionyellow, name="create"),

]










