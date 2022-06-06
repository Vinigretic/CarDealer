from django.shortcuts import render
from django.http import HttpResponse

def dealer(request):
    return render(request, 'dealer/dealer.html')

def dealer_id(request, dealer_id):
    output = f'<h2>Dealer id</h2> <p>id: {dealer_id}</p>'
    return HttpResponse(output)

def dealer_name(request):
    name = request.GET.get('name', '')
    id = request.GET.get('id', '')
    output = f'<h2>Dealer</h2> <p>name:{name}, id:{id}</p>'
    return HttpResponse(output)