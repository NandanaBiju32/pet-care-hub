from django.urls import path
from .import views
from django.conf import settings

from django.conf.urls.static import static
urlpatterns=[
#     path('',views.index,name='index'),
    path('',views.home,name='home'),
    path('login/', views.login_page, name='login'),
    path('', views.buy_now, name='buy_now'),
path('adopt/', views.adopt_page, name='adopt'),
    path('add-pet/', views.add_pet, name='add_pet'),
path('payment/', views.payment_page, name='payment'),
path('register/', views.register_user, name='register'),
path('login/', views.login_page, name='login'),
path('dashboard/', views.dashboard,name='dashboard'),
path('logout/',views.logout_user,name='logout'),
path('edit-pet/<int:id>/',views.edit_pet,name='edit_pet'),
path('delete-pet/<int:id>/',views.delete_pet,name='delete_pet'),
path('edit-pet/<int:id>/',views.edit_pet,name='edit_pet'),
path('products/',views.products_page,name='products'),
path('view_product/<int:id>/',views.view_product,name='view_product'),
path('success/',views.success,name='success'),
path('logout/',views.logout_view,name='logout'),
path('logout/',views.logout_user,name='logout'),
path('contact-owner/<int:id>/',views.contact_owner,name='contact_owner'),
]