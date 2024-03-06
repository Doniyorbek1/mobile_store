from django.http import HttpRequest, JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
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

# update product 
def update_parduct(request: HttpRequest, pk: int) -> JsonResponse:
    """update product by id"""
    if request.method == "POST":
        product = Smartphones.objects.get(id=pk)
        data = json.loads(request.body)
        product.price = data.get('price', product.price)
        product.img_url = data.get('img_url', product.img_url)
        product.color = data.get('color', product.color)
        product.ram = data.get('ram', product.ram)
        product.memory = data.get('memory', product.memory)
        product.name = data.get('name', product.name)
        product.model = data.get('company', product.model)
        product.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})
   

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
        product = Smartphones.objects.filter(model__contains = name)
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

# get model
def lst_models(request: HttpRequest) -> JsonResponse:
    """get all models"""
    try:
        product = Smartphones.objects.all()
        data = []
        for i in product:
            data.append(i.to_dict()['model'])
        data = list(set(data))
    except:
        return JsonResponse({"data":"not found"})
    return JsonResponse(data=data, safe=False)
        
# delete product by id
def delete_product(request: HttpRequest, pk : int)-> JsonResponse:
    if request.method =="GET":
        product =  Smartphones.objects.get(id = pk)
        product.delete()
        
        return JsonResponse({"product": "deleted product"})
    else:
        return JsonResponse({"status":"error"})