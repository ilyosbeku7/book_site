from books.models import Category

def context_processors(request):
    category=Category.objects.all()
    return{'categories':category}