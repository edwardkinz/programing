from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def about_us(request):
    return  render(request, 'about_us.html')

def our_products(request):
    return  render(request, 'our_products.html')

def contact_us(request):
    return  render(request, 'contact_us.html'),

def newCars(request):
    return  render(request, 'newCars.html')



