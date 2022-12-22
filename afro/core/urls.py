from django.urls import path



from . import views

urlpatterns = [

    path('home', views.home, name='home'),
    path('projects/', views.project, name='projects'),
    path('projects/<int:project_id>/',views.project_detail, name='project_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('about-me/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('resume/', views.resume, name='resume'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    
]