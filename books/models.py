from django.db import models 
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    cat=models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True, related_name='country')
    created_at=models.DateField()
    image=models.ImageField(upload_to='book_images/', default='places/default1.jpg')
    def __str__(self) -> str:
        return self.name
    
class Owner(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    bio=models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class BooksOwner(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='ega')

    def __str__(self) -> str:
        return f"{self.book.name} owned by {self.owner}"
    

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='izohlar')
    comment_text=models.TextField()
    star_given=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at=models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.user} commented to {self.book.name} and gave {self.star_given} stars"

class Category (models.Model):
    name=models.CharField(max_length=100)
    pictures=models.ImageField(upload_to='categories_images/', default='places/default1.jpg')

    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name='Kategoriya'
        verbose_name_plural='Kategoriyalar'