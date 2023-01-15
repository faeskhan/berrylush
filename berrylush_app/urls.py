from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('authentication-log-in/', views.authenticationlogin, name="authentication-log-in"),
    path('contact-us/', views.contactus, name="contact-us"),
    path('plan-your-visit/', views.planyourvisit, name="plan-your-visit"),
    path('products/', views.products, name="products"),
    path('samplePDF/', views.samplePDF, name="samplePDF"),
    path('reviews-create-edit/', views.reviewscreateedit, name= "reviews-create-edit"),
    path('detail_reviews/<str:pk>/', views.detail_reviews, name="detail_reviews"),
    path('delete_review/<str:pk>/', views.delete_review, name="delete_review"),
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    path('register/', views.register, name="register"),

]
