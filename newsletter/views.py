from django.shortcuts import render
from .models import Newsletter, NewsletterCategory
from django.shortcuts import render, get_object_or_404
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
    data = {
        "newsletterCategories" : NewsletterCategory.objects.all(),
        "newsletters" : Newsletter.objects.all()
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
    return render(request, 'category_newsletter.html', {'newsletters': newsletters, 'category': category})