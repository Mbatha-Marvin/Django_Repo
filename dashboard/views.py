from django.shortcuts import render
# from django.views.generic import TemplateView

# Create your views here.


def home_page_view(request):
    return render(request, 'dashboard/home_page/index.html')

def dash_view(request):
    return render(request, 'dashboard/dash/index.html')