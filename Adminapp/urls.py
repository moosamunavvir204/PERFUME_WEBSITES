from django.urls import path,include
from Adminapp import views


urlpatterns=[
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_page/', views.add_page, name='add_page'),
    path('save_perfume/',views.save_perfume,name='save_perfume'),
    path('details_page/',views.details_page,name='details_page'),
    path('edit_page<int:per_id>/', views.edit_page, name='edit_page'),
    path('delete_page<int:per_id>/', views.delete_page, name='delete_page'),
    path('Update_Perfume<int:per_id>/', views.Update_Perfume, name='Update_Perfume'),

    # ----------------------------product--------------------------------------------------------------------------------------#

    path('product_page/', views.product_page, name='product_page'),
    path('save_product/', views.save_product, name='save_product'),
    path('product_details/', views.product_details, name='product_details'),
    path('edit_product<int:pro_id>/', views.edit_product, name='edit_product'),
    path('delete_product<int:pro_id>/', views.delete_product, name='delete_product'),
    path('Update_Product<int:pro_id>/', views.Update_Product, name='Update_Product'),
# ---------------------------client---------------------------------------------------------------------------------------
    path('Client_page/', views.Client_page, name='Client_page'),
    path('Client_details/', views.Client_details, name='Client_details'),
    path('save_Client/', views.save_Client, name='save_Client'),
    path('edit_client<int:clint_id>/', views.edit_client, name='edit_client'),
    path('Update_Client<int:clint_id>/', views.Update_Client, name='Update_Client'),
    path('delete_client<int:clint_id>/', views.delete_client, name='delete_client'),


    path('banner_page/', views.banner_page, name='banner_page'),
    path('banner_details/', views.banner_details, name='banner_details'),
    path('save_banner/', views.save_banner, name='save_banner'),
    path('edit_banner<int:banner_id>/', views.edit_banner, name='edit_banner'),
    path('update_banner<int:banner_id>/', views.update_banner, name='update_banner'),
    path('delete_banner<int:banner_id>/', views.delete_banner, name='delete_banner'),
]