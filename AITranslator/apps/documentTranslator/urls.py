from django.urls import path
from . import views

urlpatterns = [
    path('', views.showPage, name='showDocumentTranslator'),
]
