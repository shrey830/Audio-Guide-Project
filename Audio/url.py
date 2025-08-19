from django.urls import path
from Audio import views

urlpatterns = [
    # path('',views.login,name='login'),
    path('',views.index,name='index'),
    path('header/',views.header,name='header'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('tour/',views.tour,name='tour'),
    path('contact/',views.contact,name='contact'),
    path('home/',views.home,name='home'),
    path('tour-detail1/',views.tourdetail1,name='tour-detail1'),
    path('tour-detail2/',views.tourdetail2,name='tour-detail2'),
    path('tour-detail3/',views.tourdetail3,name='tour-detail3'),
    path('tour-detail4/',views.tourdetail4,name='tour-detail4'),
    path('tour-detail5/',views.tourdetail5,name='tour-detail5'),
    path('tour-detail6/',views.tourdetail6,name='tour-detail6'),
    path('tour-detail7/',views.tourdetail7,name='tour-detail7'),
    path('tour-detail8/',views.tourdetail8,name='tour-detail8'),
    path('tour-detail9/',views.tourdetail9,name='tour-detail9'),
    path('tour-detail10/',views.tourdetail10,name='tour-detail10'),
    path('Audio1/',views.Audio1,name='Audio1'),
    path('bookguide/', views.bookguide_page, name='bookguide'), 
    path('bookguide/<str:guide_name>/<str:guide_place>/',views.bookguide_page,name='bookguide'),
    path('send_otp/', views.send_otp, name='send_otp'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register_page,name='register'),
    path('logout/',views.logout,name='logout'),
    path('audio_page/',views.audio_player,name='audio_page'),
    path('ahmedabad/', views.ahmedabad, name='ahmedabad'),
    path('profilepage/',views.profile_page,name='profilepage'),

    

 
]