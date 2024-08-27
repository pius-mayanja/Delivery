from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["jumia:items",
                'jumia:search', 
                'orders:order_create', 
                'orders:payment_callback',
                'user:signup',
                'user:reg',
                'user:login', 
                'user:logout', 
                'chart:inbox',
                'cart:cart_detail',
                'business:manage',
                'business:ordered',
                'business:reg',
                'business:inbox',
                ]

    def location(self, item):
        return reverse(item)


    # path('', manage, name='manage'),
    # path('detail/<int:id>',detail, name= 'detail'),
    # path('orders/',orders, name= 'ordered'),
    # path('order-details/<int:id>',order_details, name= 'order_details'),
    # path('products/', business_reg, name='reg'),
    # path('inbox/',inbox, name='inbox'),
    # path('<int:pk>/',cdetail, name='cdetail'),