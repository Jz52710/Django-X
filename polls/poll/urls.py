from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    path('',views.index,name='index'),
    path('question/<int:id>',views.detail,name='detail'),
    path('show/<int:id>',views.show,name='show')
]
