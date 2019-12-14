from django.urls import path
from django.views.generic import TemplateView
from .views import Goodsp,GoodsOneview,Login

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('about',TemplateView.as_view(template_name='about.html')),
    path('api/goods',Goodsp.as_view()),
    path('api/goods/<int:id>',GoodsOneview.as_view()),
    path('api/login',Login.as_view()),
]
