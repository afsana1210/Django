from django.urls import path
from . import views
from .views import  signin
from afsana.views import form_view
from .views import signups,signup_view,signup_page_view,CreateMyModelView
urlpatterns=[
    path('',views.index,name='index'),
    path('create',views.CreateMyModelView.as_view(),name='create'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('form/',views.form_view,name='form_view'),
    path('signup_view/',views.signup_view,name='signup_view'),
    path('signup_page_view/<int:id>',views.signup_page_view,name="signup_page_view"),
    path('signup/', views.signups, name='signups'),
    path('signin/', views.signin, name='signin'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]