from django.urls import path

from . import views

app_name = 'schedule_roster'


urlpatterns = [
    path('buys/<item>', views.index_buys_view, name='indexing roster'),
    path('sells/<item>', views.index_sells_view, name='indexing roster'),
]
