from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Review
from .forms import ReviewForm
from account.models import BorrowHistory

# Create your views here.


class BookDetailView(DetailView):
    model = Book
    template_name = "detail.html"

    """
    name = models.CharField(max_length=200)
    body = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    posted_on = models.DateField(auto_now_add=True, blank=True, null=True)
    """

    def post(self, request, *args, **kwargs):
        review_form = ReviewForm(self.request.POST)
        book = self.get_object()
        if self.request.method == "POST":
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.name = self.request.user
                new_review.book = Book.objects.get(id=book.id)
                new_review.save()
        # return back to current book detail page
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        book = self.get_object()
        reviews = Review.objects.filter(book=book)
        review_form = ReviewForm()

        account = self.request.user.account
        user_borrow_history = BorrowHistory.objects.filter(account=account)
        borrowed = user_borrow_history.filter(book=book).exists()

        context["form"] = review_form
        context["reviews"] = reviews
        context["borrowed"] = borrowed
        return context
