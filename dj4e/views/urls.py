
from django.urls import path
from views import views
app_name = "views"
urlpatterns = [
    path('', views.main,name="main"),
    path('funky/', views.funky,name="funky"),
    path('danger/', views.danger,name="danger"),
    path('template/', views.template,name="templates"),
    path('game/<int:guess>', views.game,name="game"),
    path('loop/', views.loop,name="loop"),
    path('nested/', views.nested,name="nested"),
    path('base/<int:guess>', views.usingbase,name="base"),
    path('reverseurl/', views.revurl,name="reversurl"),
    path('classview/<int:guess>',views.RestMainView.as_view(),name="classview")
]
