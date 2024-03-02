from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.lookups import IContains
import json
from .models import Smartphones


def add_product(reqeust: HttpRequest) -> JsonResponse:
    """add new product to database"""
    # Check if request method is POST
    if reqeust.method == 'POST':
        # Get data from request
        data = json.loads(reqeust.body)
        print(data)
        # Create new product
        product = Smartphones(
            price=data['price'],
            img_url=data['img_url'],
            color=data['color'],
            ram=data['ram'],
            memory=data['memory'],
            name=data['name'],
            model=data['company']
        )
        # Save product to database
        product.save()
        # Return response
    return JsonResponse({'status': 'ok'})
   

def get_products(request: HttpRequest) -> JsonResponse:
    """get all products from database"""
    # Get all products from database
    products = Smartphones.objects.all()
    # Create list of products
    data = []
    for product in products:
        data.append(product.to_dict())
    # Return response
    return JsonResponse(data, safe=False)


def get_product_id(request: HttpRequest, pk: int) -> JsonResponse:
    """get product by id"""
    # Get product by id
    try:
        product = Smartphones.objects.get(id=pk)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    # Return response
    return JsonResponse(product.to_dict())

def get_name(request: HttpRequest, name: str) -> JsonResponse:
    """get product by name"""
    # Get product by name
    try:
        product = Smartphones.objects.filter(name__contains = name)
        data = []
        for i in product:
            data.append(i.to_dict())
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    # Return response
    return JsonResponse(data=data, safe=False )
# get color 
def get_color(request: HttpRequest, color: str) -> JsonResponse:
    """get product by color """
    try:
        product =  Smartphones.objects.filter(color__contains = color)
        data = []
        for i in product:
            data.append(i.to_dict())
    except:
        return JsonResponse({"data":"not found"})

    return JsonResponse(data=data, safe=False)