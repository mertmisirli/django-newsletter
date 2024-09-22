from django.shortcuts import render
from .models import Newsletter, NewsletterCategory
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
import math

# Create your views here.
# newsletterCategories = [
#     {
#         "name" : "Spor"
#     },
#     {
#         "name" : "Siyaset"
#     },
#     {
#         "name" : "Sanat"
#     },
#     ]
# newsletterList = [
#     {
#         "id" : 1,
#         "title" : "Haber1",
#         "content" : "Haber 1 içerik"
#     },
#     {
#         "id" : 2,
#         "title" : "Haber2",
#         "content" : "Haber 2 içerik"
#     },
#     {
#         "id" : 3,
#         "title" : "Haber3",
#         "content" : "Haber 3 içerik"
#     },
# ]

def home(request):
    return render(request, "index.html")

def newsletter(request):
    newsletters = Newsletter.objects.all()
    newsletters_length = len(newsletters)

    total_page_count = math.ceil(newsletters_length / 10)

    paginator = Paginator(newsletters, 10)  
    page_number = request.GET.get('page') 

    if page_number is None:
        page_number = 1  # Varsayılan olarak 1. sayfayı al

    page_obj = paginator.get_page(page_number)

    data = {
        "newsletterCategories" : NewsletterCategory.objects.all(),
        "newsletters" : page_obj,
        'total_page_count' : total_page_count,
        'page_range' : range(1, total_page_count + 1),  
        'current_page' : page_number
    }

    return render(request, "newsletter.html", data)

def news_detail(request, id):
    data = {
        "newsletter" : Newsletter.objects.get(id=id)
    }
    return render(request, "news_detail.html", data)


def category_newsletter(request, category_id):
    category = get_object_or_404(NewsletterCategory, id=category_id)
    newsletters = Newsletter.objects.filter(category=category)

    newsletters_length = len(newsletters)

    total_page_count = math.ceil(newsletters_length / 4)
    # Pagination ayarları
    paginator = Paginator(newsletters, 4)  
    page_number = request.GET.get('page')  

    if page_number is None:
        page_number = 1  # Varsayılan olarak 1. sayfayı al

    page_obj = paginator.get_page(page_number)

    return render(request, 'category_newsletter.html', {
        'newsletters': page_obj,
        'category': category,
        'total_page_count' : total_page_count,
        'page_range' : range(1, total_page_count + 1),  
        'current_page' : page_number
    })
    # category = get_object_or_404(NewsletterCategory, id=category_id)
    # newsletters = Newsletter.objects.filter(category=category)
    # return render(request, 'category_newsletter.html', {'newsletters': newsletters, 'category': category})