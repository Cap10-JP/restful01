from django.urls import re_path, path
from toys import views

urlpatterns = [
    re_path(r'^toys/$', views.toy_list),
    path('toys/<int:pk>', views.toy_detail),
]
