from django.conf.urls import url

from zbj import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^classifier/', views.classifier, name='classifier'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^shop/', views.shop, name='shop'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^detail/(\w+)/$', views.detail, name='detail'),
    url(r'^data', views.data, name='data'),
    url(r'^pycharts_good', views.pycharts_good, name='pycharts_good'),
    url(r'^pycharts_price', views.pycharts_price, name='pycharts_price'),
    url(r'^predict', views.pridict, name='predict'),
    url(r'^show_company/(\w+)/$', views.show_company, name='show_company')
]