from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import ShoppinglistListView
from .views import ShoppingitemListView
from .views import ShoppinglistDetailView
# from .views import ShoppingitemDetailView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace="rest_framework")),
    url(r'^shoppinglists/$', ShoppinglistListView.as_view(), name="shoppinglists"),
    url(r'^shoppinglists/(?P<shoppinglist_id>[0-9]+)/$', ShoppinglistListView.as_view(), name="shoppinglists"),
    url(r'^shoppinglists/(?P<shoppinglist_id>[0-9]+)/shoppingitems/$', ShoppingitemListView.as_view(), name="shoppingitems"),
    url(r'^shoppinglists/(?P<shoppinglist_id>[0-9]+)/shoppingitems/(?P<shoppingitem_id>[0-9]+)/$', ShoppingitemListView.as_view(), name="shoppingitems"),
    url(r'^shoppinglist/(?P<shoppinglist_id>[0-9]+)/$', ShoppinglistDetailView.as_view(), name="shoppinglistdetails"),
    url(r'^get_token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
