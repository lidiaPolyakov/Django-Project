from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings    



urlpatterns = [
    path('', views.home, name="home"),
    path('signout/',views.signout, name="signout"),
    path('signup/',views.signup, name="signup"),
    path('login/',views.signin, name="login"),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name='register'),
    path('edit_profile/<str:pk>/',views.edit_profile, name='edit_profile'),
    path('create_chore/', views.create_chore, name='create_chore'),
    path('my_chores/', views.my_chores, name='my_chores'),
    #path('delete_profile/<str:pk>/',views.delete_profile, name='delete_profile'),
    #path(r'form',views.register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )
