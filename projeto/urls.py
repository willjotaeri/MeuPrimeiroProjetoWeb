from django.urls import path
from app.views import login, home, solicitado_solicitante_list
from django.views.generic import RedirectView

app_name = 'app'

urlpatterns = [
    path('', RedirectView.as_view(url='/login/'), name='root'),
    path('login/', login, name='login'),
    path('home_solicitante/', home, name='home_solicitante'),
    path('solicitado_solicitante_list/', solicitado_solicitante_list, name='solicitado_solicitante_list'),
]
