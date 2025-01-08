from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('<h1 style="background-color:red";>hello world<h1>')