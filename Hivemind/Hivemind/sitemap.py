from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["items", 'detail','category','search','order_create','direct_order','login','logout','cart']

    def location(self, item):
        return reverse(item)
    
    # path('', items, name='items'),
    # path('detail/<int:id>',detail, name= 'detail'),
    # path('category/<int:id>',categories, name= 'category'),
    # path('results/', search, name='search'),
    # path('created/', order_create, name='order_create'),
    # path('direct/<int:item_id>/',direct_order, name='direct_order'),
    # path('orders/', orders, name='order'),
    # path('order-details/<int:id>', order_details, name='detail'),
    # path('order-delete/<int:id>/delete', delete_order, name='delete_order'),
    # path('payment/<int:order_id>/', initiate_payment, name='payment'),
    # path('success/', payment_callback, name='payment_callback'),
    # path('signup/', SignUp, name='signup'),
    # path("signup/business/",BusinessSignUpView.as_view(), name="reg"),
    # path('login/',LoginView.as_view(), name='login'),
    # path('logout/', Logout_view , name='logout'),
    # path('sell/', Sell_details, name='sell_details' ),
    # path('', views.inbox, name='inbox'),
    # path('<int:pk>/', views.detail, name='detail'),
    # path('new/<int:item_pk>/', views.new_conversation, name='new'),
    #  path('', views.cart_detail, name='cart_detail'),
    # path('update/<int:product_id>', views.cart_update, name='cart_update'),    
    # path('add/<int:product_id>/', views.cart_add, name='cart_add'),    
    # path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    #     path('', manage, name='manage'),
    # path('detail/<int:id>',detail, name= 'detail'),
    # path('orders/',orders, name= 'ordered'),
    # path('order-details/<int:id>',order_details, name= 'order_details'),
    # path('products/', business_reg, name='reg'),
    # path('inbox/',inbox, name='inbox'),
    # path('<int:pk>/',cdetail, name='cdetail'),