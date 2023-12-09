from django.urls import path
from . import views

urlpatterns = [
    path('all-objectives/', views.all_objectives, name='all_objectives'),
    path('objective/<int:objective_id>/', views.objective_details, name='objective_details'),

]
