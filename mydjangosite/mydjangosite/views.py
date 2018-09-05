from django.http import HttpResponse

def hello(request):
    return HttpResponse("我的第一个python网站")
