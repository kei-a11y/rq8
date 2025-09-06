# kk10/urls.py
from django.urls import path
from . import views

app_name = "info"

urlpatterns = [
    path("info-request/", views.request_form_view, name="request_form"),
    path("info-request/success/", views.request_success_view, name="request_success"),
    path("admin-list/", views.admin_list_view, name="admin_list"),
    path("export/excel/", views.export_excel, name="export_excel"),
]

