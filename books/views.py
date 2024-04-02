from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Owner, BooksOwner, Comment, Category
from django.views import View
from .forms import BooksCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
# Create your views here.

class BooksView(View):
    def get(self, request):
        comment = Comment.objects.all()
        reversed_comments = comment[::-1]  
        last_4_comments = reversed_comments[:4]
        categories=Category.objects.all()
        books=Book.objects.all()
        search_query=request.GET.get('q', "")
        
        if search_query:
            books=books.filter(name__icontains=search_query,)
    
        data={
            
            'categories':categories,
            'books':books,
            'last_4_comments':last_4_comments,
        }

        return render(request, 'books/home_page.html', context=data, )
    

class AboutView(View):

    def get(self, request, id):
        
        book=get_object_or_404(Book, pk=id)
        owners=BooksOwner.objects.all()
        comments=Comment.objects.all()
        form=BooksCommentForm()  

        data={
            
            'book':book,
            'owners':owners,
            'form': form,
            'comments':comments
        }

        return render(request, 'books/about_page.html', context=data)
    
class AddComment(LoginRequiredMixin, View):
    def post(self, request, id):
        form = BooksCommentForm(request.POST)
        book = Book.objects.get(id=id)
        data = {
            'form': form,
            'book': book
        }
        if form.is_valid():
            Comment.objects.create(
                user=request.user,
                book=book,
                comment_text=form.cleaned_data['comment_text'],
                star_given=form.cleaned_data['star_given']
            )
            return redirect(reverse('books:about_page', kwargs={'id': book.id}))
        return render(request, 'books/about_page.html', context=data)

   
    
def category(request, id):
    category=get_object_or_404(Category, pk=id)
    categories=Category.objects.all()
    books=Book.objects.filter(cat=category).order_by('name')
    data={
        'categories':categories,
        'books':books,
        'category': category
    }
    return render(request, 'books/Category.html', context=data)