from modeltranslation.translator import translator, TranslationOptions
from .models import Book, Author, Genre


class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'summary',)


translator.register(Book, BookTranslationOptions)


class AuthorTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)


translator.register(Author, AuthorTranslationOptions)


# class GenreTranslationOptions(TranslationOptions):
#    fields = "name"


# translator.register(Genre, GenreTranslationOptions)
