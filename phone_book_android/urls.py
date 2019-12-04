from django.conf.urls import url

from phone_book_android import views

urlpatterns = [
    url(r'^get_token/$',views.get_my_token),
    url(r'^phone/list/$', views.get_phone_list),
    url(r'^phone/(?P<id>\d+)/$', views.get_phone_by_id),
    url(r'^phone/add/$', views.add_phone),
    url(r'^phone/delete/$', views.delete_phone),
    url(r'^phone/update/$', views.update_phone),
]
