from django.urls import path
from . import views
from .views import  signin
from .views import signups
urlpatterns=[
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('form/',views.form_view,name='form_view'),
    path('signup/', views.signups, name='signups'),
    path('signin/', views.signin, name='signin'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]