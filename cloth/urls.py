from django.urls import path
from . import views

urlpatterns = [
    path('productCL/', views.ProductListView.as_view(), name='products'),
    path('productCL/<int:id>', views.ProductDetailView.as_view(), name='details'),
    path('add_orderCL/', views.OrderCreateView.as_view(), name='add'),
]