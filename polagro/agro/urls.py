from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-product'),
    path('users/', views.users, name = 'users'),
    path('about/', views.aboutus, name = 'About'),
    path('pesticides/update/<int:product_id>', views.update_product),
    path('pesticides/delete/<int:product_id>', views.delete_product),

    path('seed&plant/update/<int:product_id>', views.update_product),
    path('seed&plant/delete/<int:product_id>', views.delete_product),

    path('traps/update/<int:product_id>', views.update_product),
    path('traps/delete/<int:product_id>', views.delete_product),

    path('fertilizers/update/<int:product_id>', views.update_product),
    path('fertilizers/delete/<int:product_id>', views.delete_product),

    path("register", views.register_request, name="register"),

    path("login", views.login_request, name="login"),

    path("logout", views.logout_request, name= "logout"),
    path('contact1/', views.contact_view, name='contact'),
    path('seed&plant/', views.seed_plant, name='seed&plant'),
    path('traps/', views.traps, name='traps'),
    path('fertilizers/', views.fertilizers, name='fertilizers'),
    path('pesticides/', views.pesticides, name='pesticides'),
]
urlpatterns += staticfiles_urlpatterns()


