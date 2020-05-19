from django.urls import path

from . import views

app_name = 'schedule_roster'


urlpatterns = {
    path('buys/<item>', views.index_buys_view, name='indexing roster'),
    path('sells/<item>', views.index_sells_view, name='indexing roster'),
    path('buys_std_deviation_info/<item>', views.buys_index_std_deviation_info, name='std-deviation'),
    path('sells_std_deviation_info/<item>', views.sells_index_std_deviation_info, name='std-deviation'),
}
