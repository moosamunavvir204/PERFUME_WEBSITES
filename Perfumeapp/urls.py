from django.urls import path,include
from  Perfumeapp import views
from . import views
import razorpay

urlpatterns=[
    path('Home/', views.Home, name='Home'),
    path('About/', views.About, name='About'),
    path('product/', views.product, name='product'),
    # path('filtered_product/<cat_name>/',views.filtered_product,name='filtered_product'),
    path('filtered_product/<str:cat_name>/', views.filtered_product, name='filtered_product'),
    path('contact/',views.contact,name='contact'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('terms/', views.terms, name='terms'),
    path('payment/',views.payment,name='payment'),
    path('main_page/',views.main_page,name='main_page'),
    path('User_register/',views.User_register,name='User_register'),
    path('save_register/', views.save_register, name='save_register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('Single_iteam/<int:pro_id>',views.Single_iteam,name='Single_iteam'),
    path('Cart_page/',views.Cart_page,name='Cart_page'),
    path('save_to_cart/<int:pro_id>/',views.save_to_cart,name='save_to_cart'),
    path('Check_out_page/',views.Check_out_page,name='Check_out_page'),
    path('save_check_out/', views.save_check_out, name='save_check_out'),
    path('end_page/',views.end_page,name='end_page'),
    path('remove_from_cart/<int:pro_id>/', views.remove_from_cart, name='remove_from_cart'),
    path( 'increase_quantity/<int:pro_id>/', views.increase_quantity,name='increase_quantity'),
    path('decrease_quantity/<int:pro_id>/',views.decrease_quantity,name='decrease_quantity'),
    path('search_product/', views.search_product, name='search_product'),
    path('add_review/<int:pro_id>/',views.add_review,name='add_review'),
path(
    'delete_review/<int:review_id>/',
    views.delete_review,
    name='delete_review'
),



]
