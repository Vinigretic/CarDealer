from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def car(request):
    return render(request, 'car/car.html')

def car_create(request, product_id):
    output = f'<h2>Product number</h2> <p>id: {product_id}</p>'
    return HttpResponse(output)

def car_id(request, car_id):
    output = f'<h2>Car number</h2> <p>id: {car_id}</p>'
    return HttpResponse(output)

# def car_info(request, car_info_id):
#     output = f'<h2>Car info</h2> <p>id: {car_info_id}</p>'
#     return HttpResponse(output)

def car_info(request, car_info_id):
    return HttpResponseRedirect('/car_id')


