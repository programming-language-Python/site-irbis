from django.urls import path
# from django.views.decorators.cache import cache_page

from .views import *

app_name = 'app'

urlpatterns = [
    # path('', cache_page(60*30)(HomePage), name='home'),
    path('', HomePage, name='home'),
    path('mail_template/', mail_template, name='mail_template'),
    path('Menu/', ViewMenu.as_view(), name='menu'),    
    path('Menu/<int:menu_id>/', GetCardMenu.as_view(), name='card_menu'),
    path('Excursions/', ViewExcursion.as_view(), name='excursion'),
    path('Excursion/<int:excursion_id>/',
         GetCardExcursion.as_view(), name='card_excursion'),
    path('Numbers/', ViewNumbers.as_view(), name='numbers'),
    path('Numbers/<int:number_id>', GetCardNumbers.as_view(), name='card_numbers'),
    path('Orders/', Orders, name='orders'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
#     path('<int:id>/', product_detail,
#          name='product_detail')
]
