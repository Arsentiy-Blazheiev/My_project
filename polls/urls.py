from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('zones/', views.zones_index, name='zones_index'),
    # path('zones/<int:zone_id>/', views.zone_detail, name='zone_detail'),

    path('actions/', views.actions_index, name='actions_index'),
    path('actions/<int:action_id>/', views.action_detail, name='action_detail'),
]
