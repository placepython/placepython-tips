from django.urls import path
from wepynaire.tips.views import detail_view

app_name = "tips"

urlpatterns = [
    path("<slug:slug>/", detail_view, name="detail"),
]
