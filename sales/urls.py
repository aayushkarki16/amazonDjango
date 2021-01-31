from django.urls import path
from sales import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('login_views', views.login_views, name='login_views'),
    path('logout', views.logout, name='logout'),
    path('success', views.success, name='success'),
    path('sorry', views.sorry, name='sorry'),
    path('shopsignup', views.shop_sign, name='shop_sign'),
    path('shop', views.shop, name='shop'),
    path('product', views.product, name='product'),
    path('productshow', views.productshow, name='productshow'),
    path('productedit/<int:id>', views.productedit, name='productedit'),
    path('productupdate/<int:id>', views.productupdate, name='productupdate'),
    path('productdestroy/<int:id>', views.productdestroy, name='productdestroy'),
    path('offer', views.offer, name='offer'),
    path('offershow', views.offershow, name='offershow'),
    path('offeredit/<int:id>', views.offeredit, name='offeredit'),
    path('offerupdate/<int:id>', views.offerupdate, name='offerupdate'),
    path('offerdestroy/<int:id>', views.offerdestroy, name='offerdestroy'),
    path('search_product', views.search_product, name='search_product')

]

