from django.urls import path

from producer.views import IndexView, OrderDeleteView, register

urlpatterns = [
    path("register/", register, name="register"),
    path("", IndexView.as_view(), name="orders"),
    path("task/<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
]


app_name = "producer"
