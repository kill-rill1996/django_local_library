from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('books/', views.BookListView.as_view(), name='books'),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),

    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [
    url(r'^books/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    url(r'^authors/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^authors/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^authors/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]
