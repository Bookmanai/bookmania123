from django.contrib import admin
# Register your models here.
from .models import Author, Genre, Book, Language, Comment

class AuthorInline(admin.TabularInline):
    model = Author
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
admin.site.register(Book, BookAdmin)
inlines = [AuthorInline]


class LanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Language, LanguageAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'display_books')
    fields = ['first_name', 'last_name', 'date_of_birth']
    #    fields = ['first_name', 'last_name', 'date_of_birth','image']
admin.site.register(Author, AuthorAdmin)


class GenreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Genre, GenreAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'book', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
admin.site.register(Comment, CommentAdmin)