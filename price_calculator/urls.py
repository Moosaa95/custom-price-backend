# from django.urls import path
# from .views import ProductListAPIView, OptionListAPIView, PriceCalculatorAPIView

# urlpatterns = [
#     path('products/', ProductListAPIView.as_view(), name='product_list'),
#     path('options/', OptionListAPIView.as_view(), name='option_list'),
#     path('price-calculator/', PriceCalculatorAPIView.as_view())
# ]


from django.urls import path
from .views import PriceCalculatorView, GetProduct

urlpatterns = [
    path('calculate_price/', PriceCalculatorView.as_view(), name='calculate_price'),
    path('get_products/', GetProduct.as_view(), name='get_products'),
]
