from django.urls import path
from . import views

app_name = 'cbv'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('schools',views.SchoolListView.as_view(),name='list'),
    path('schools/<pk>/', views.SchoolDetailView.as_view(), name='detail')


]
