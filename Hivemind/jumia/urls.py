from django.urls import path, include
from .views import *
from django.contrib.auth.views import *
from .sitemap import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemap_dict = {
    "static": StaticViewSitemap(),
}

app_name = 'jumia'

urlpatterns = [
    path('', items, name='items'),
    path('sitemap.xml', sitemap, {"sitemaps": sitemap_dict}, name="django.contrib.sitemaps.views.sitemap"),
    path('detail/<int:id>', detail, name='detail'),
    path('category/<int:id>', categories, name='category'),
    path('results/', search, name='search'),
]

