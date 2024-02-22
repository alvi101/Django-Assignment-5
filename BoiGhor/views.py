from django.shortcuts import render
from book.models import Book
from django.views.generic import ListView
from book.models import Category

# Create your views here.


class HomeView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


def filterview(request, id):
    category = Category.objects.get(id=id)
    all_category = Category.objects.all()
    books = Book.objects.filter(category=category)
    return render(request, 'filtered_books.html', {'books': books, 'categories': all_category})