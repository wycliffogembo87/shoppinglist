from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import ShoppinglistListView
from .views import ShoppingitemListView
# from .views import ShoppinglistDetailListCreateAPIView
# from .views import ShoppinglistItemListCreateAPIView
# from .views import ShoppinglistItemsListCreateAPIView
# from .views import ShoppinglistItemsListRUDAPIView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace="rest_framework")),
    url(r'^shoppinglists/$', ShoppinglistListView.as_view(), name="shoppinglists"),
    url(r'^shoppinglists/(?P<shoppinglist_id>[0-9]+)/$', ShoppinglistListView.as_view(), name="shoppinglists"),
    url(r'^shoppinglists/(?P<shoppinglist_id>[0-9]+)/shoppingitems/$', ShoppingitemListView.as_view(), name="shoppingitems"),
    url(r'^shoppinglists/(?P<shoppinglist_id>[0-9]+)/shoppingitems/(?P<shoppingitem_id>[0-9]+)/$', ShoppingitemListView.as_view(), name="shoppingitems"),
    url(r'^get_token/', obtain_auth_token)
}

urlpatterns = format_suffix_patterns(urlpatterns)
