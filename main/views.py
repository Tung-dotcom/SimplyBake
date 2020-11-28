from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request, 'main/about.html')

def products(request):
    return render(request, 'main/products.html')

def connect(request):
    return render(request, 'main/connect.html')