from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ShoppinglistAPIView
from .views import ShoppingitemAPIView

urlpatterns = {
    url(r'^shoppinglists/$', ShoppinglistAPIView.as_view(), name="shoppinglists"),
    url(r'^shoppinglists/(?P<pk>[0-9]+)/shoppingitems/$', ShoppingitemAPIView.as_view(), name="shoppingitems"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
