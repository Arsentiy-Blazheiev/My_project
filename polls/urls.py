from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path('zones/', views.zones_index, name='zones_index'),
    # path('zones/<int:zone_id>/', views.zone_detail, name='zone_detail'),
    path('actions/', views.actions_index, name='actions_index'),
    # path('actions/<int:action_id>/', views.action_detail, name='action_detail'),
    path('way/', views.way_index, name='way_index'),
    path('terms/', views.terms_index, name='terms_index'),
    path('result/', views.result, name='result'),
    # path('next_step/', views.next_step, name='next_step'),
    # path('next_model/', views.next_model, name='next_model'),
]
