from django.urls import path
from . import views



urlpatterns = [
    path('',views.poll_list,name='poll-list'),
    path('create/',views.poll_create,name='poll-create'),
    path('<int:poll_id>/vote/',views.poll_vote,name='poll-vote'),
    path('<int:poll_id>/results/',views.poll_results,name='poll-results'),
    #path('get/data/<int:obj_id>/',views.get_resultsData,name='get-result-data'),
    path('api/data/<int:obj_id>/',views.get_api_data,name='api-result-data'),
]