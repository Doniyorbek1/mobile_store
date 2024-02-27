from django.http import HttpRequest, JsonResponse
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
            model=data['model']
        )
        # Save product to database
        product.save()
        # Return response
    return JsonResponse({'status': 'ok'})
   