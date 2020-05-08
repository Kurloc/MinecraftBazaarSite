from django.urls import path

from . import views

app_name = 'schedule_roster'


urlpatterns = [
    path('sells/<item>', views.index_sells, name='indexing roster'),
    path('buys/<item>', views.index_buys, name='indexing roster'),
]
