from django.shortcuts import render

# Create your views here.

def login(request):
    print "salam"
    return render(request, 'test/login_test.html', {})