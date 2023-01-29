from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings    



urlpatterns = [
    path('', views.profile, name="profile"),
    path('signout/',views.signout, name="signout"),
    path('signup/',views.signup, name="signup"),
    path('login/',views.signin, name="login"),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name='register'),
    path('edit_profile/<str:pk>/',views.edit_profile, name='edit_profile'),
    path('create_chore/', views.create_chore, name='create_chore'),
    path('my_chores/', views.my_chores, name='my_chores'),
    path('chores_feed/', views.chores_feed, name='chores_feed'),
    path('register_chore/<str:pk>/', views.register_chore, name='register_chore'),
    path('my_registrations/', views.my_registrations, name='my_registrations'),
    path('unregister/<str:pk>/', views.unregister, name='unregister'),
    path('view_elder_profile/<str:pk>/', views.view_elder_profile, name='view_elder_profile'),
    path('edit_chore/<str:pk>/',views.edit_chore, name='edit_chore'),
    path('delete_chore/<str:pk>/',views.delete_chore, name='delete_chore'),
    path('done_chore/<str:pk>/',views.done_chore, name='done_chore'),
    
    #path('delete_profile/<str:pk>/',views.delete_profile, name='delete_profile'),
    #path(r'form',views.register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )
