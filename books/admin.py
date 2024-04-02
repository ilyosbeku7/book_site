from django.contrib import admin

from .models import Owner, BooksOwner, Comment, Book, Category

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'email')
    search_fields=('first_name', 'last_name', 'email')
    list_display_links=( 'first_name', )
    
class BookAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'created_at')
    search_fields=( 'name', )
    list_display_links=( 'name', )


class CommentAdmin(admin.ModelAdmin):
    list_display=('user', 'book', 'star_given')
    search_fields=( 'user', 'book', )
    list_display_links=( 'user', )

class BooksOwnerAdmin(admin.ModelAdmin):
    list_display=('book', 'owner', )
    search_fields=( 'owner', 'book', )
    list_display_links=( 'book', )

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(BooksOwner, BooksOwnerAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category)