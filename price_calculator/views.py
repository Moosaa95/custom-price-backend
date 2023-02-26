from decimal import Decimal
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Option
from .forms import OptionForm

class PriceCalculatorView(APIView):

    def post(self, request):
        form = OptionForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data.get("product_id")
            selected_options = form.cleaned_data.get("selected_options", [])
            quantity = form.cleaned_data.get("quantity", 1)

            
            if selected_options:
                selected_options = json.loads(selected_options)
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'error': f'Product with id {product_id} not found'}, status=status.HTTP_404_NOT_FOUND)

            option_prices = {}
            for option in selected_options:
                print("LOL", option, 'END')
                option_price = Product.get_option_price(product_id, option["name"])
                if option_price is None:
                    return Response({'error': f'Option {option["name"]} not found'}, status=status.HTTP_400_BAD_REQUEST)
                option_prices[option['name']] = option_price

            total_price = product.price
            for name, price in option_prices.items():
                total_price += price * Decimal(quantity)

            return Response({'total_price': total_price})
        else:
            return Response({"status":False, "message":form.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class GetProduct(APIView):
    def get(self, request):
        products = Product.get_products()
        return Response(data=products, status=status.HTTP_200_OK)
