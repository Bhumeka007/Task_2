from django.shortcuts import render
from django.http import JsonResponse
from itertools import zip_longest
from .models import *

# Create your views here.

def index(request):
    
    computer = Computer.objects.all()
    shirt = Shirt.objects.all()
    jumka = Jhumka.objects.all()
    kangan = Kangan.objects.all()
    laptop = Laptop.objects.all()
    mobile = Mobile.objects.all()
    neklesh = Neklesh.objects.all()
    tshirt = T_Shirt.objects.all()
    womenCloth = Women_Cloth.objects.all()
    
    zipped = zip_longest(shirt, tshirt,womenCloth)
    zipped1 = zip_longest(shirt, tshirt,womenCloth)
    electronics=zip_longest(laptop,mobile,computer)
    electronics1=zip_longest(laptop,mobile,computer)
    Jewellery =zip_longest(jumka,neklesh,kangan)
    Jewellery1 =zip_longest(jumka,neklesh,kangan)

    context = {
        "zipped":zipped,
        "zipped1":zipped1,
        "electronics":electronics,
        "electronics1":electronics1,
        "Jewellery":Jewellery,
        "Jewellery1":Jewellery1 
        
        # 'Computers': computer,
        # 'Shirts': shirt,
        # 'Jumkas': jumka,
        # 'Kangans': kangan,
        # 'Laptops': laptop,
        # 'Mobiles': mobile,
        # 'Nekleshs': neklesh,
        # 'tshirt': tshirt,
        # 'WomenCloths': womenCloth,
        
    }
    
    return render(request, 'index.html', context=context)