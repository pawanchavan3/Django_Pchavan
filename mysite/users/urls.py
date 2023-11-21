from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [

    # orders
    path('orders/<int:id>/<int:pdcd>/<str:user>/', views.Orders, name='orders'),
        
    #updating customer orders   
    path('upd_orders/,<int:upd_orders_id>/',views.update_orders,name='upd_orders'),
 
    # customer rating-feedback view

    path('crf/<int:it_id>/<int:pc>/', views.CusRatFeed, name='CusRatFeed'),
    
    #updating customer ratings and feedbacks
    path('crf/<int:details_id>/<int:crf_id>/',views.update_crf,name='upd_crf')


    ]