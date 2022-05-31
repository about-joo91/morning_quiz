from django.shortcuts import redirect, render
from .models import Article, Category
# Create your views here.


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories' : categories})
def summit(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'new.html', {'categories' : categories})
    


def save(request):   
    title = request.GET.get('title','')
    content = request.GET.get('content','')
    category = Category.objects.get(name = request.GET.get('category',''))
    new_article = Article.objects.create(title=title, content =content, category = category)
    new_article.save()
    return redirect('/')