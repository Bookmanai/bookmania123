from django.urls import path
from django.conf.urls import include, url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    #path('book/<int:pk>/read', views.BookDetailView.show_book_pdf, name='show-pdf'),
    #url(r'^pdf', views.BookDetailView.ShowPdf, name='book_pdf'),
    path('author', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    url(r'^signup/$', views.signup, name='signup'),
    path('ru/', views.set_ru, name='ru'),
    path('en/', views.set_en, name='eng'),
]
