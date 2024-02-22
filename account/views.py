from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, View, ListView
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .models import BorrowHistory, UserAccount
from book.models import Book
from django.views.generic.edit import FormView
from .forms import DespositForm
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.


def send_deposit_email(user, amount, template, to_email):

    message = render_to_string(template, {'user': user, 'amount': amount})
    send_email = EmailMultiAlternatives(
        "Deposited Successfully", '', to=[to_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()


def send_borrow_email(user, amount, book, template, to_email):
    message = render_to_string(
        template, {'user': user, 'amount': amount, 'book': book})
    send_email = EmailMultiAlternatives(
        "Book added to your list", '', to=[to_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()


class RegisterView(FormView):
    template_name = "registration.html"
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class ProfileView(ListView):
    model = BorrowHistory
    template_name = "profile.html"
    context_object_name = "books"

    def get_queryset(self):
        queryset = BorrowHistory.objects.filter(
            account=self.request.user.account)
        return queryset


class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("home")


def user_logout(request):
    logout(request)
    return redirect('home')


class BorrowView(View):
    def get(self, request,  id):
        account = UserAccount.objects.get(user=self.request.user)
        book = Book.objects.get(id=id)
        if book.price > account.balance:
            messages.error(
                request, "Insufficient balance. Deposit to borrow books")
            return redirect('deposit')

        user_borrow_history = BorrowHistory.objects.filter(account=account)
        borrowed = user_borrow_history.filter(book=book).exists()
        if borrowed:
            messages.error(request, "You have already borrowed this book")
            return redirect('profile')

        account.balance -= book.price
        BorrowHistory.objects.create(
            account=account,
            book=book
        )

        account.save(update_fields=["balance"])

        # send_borrow_email(user, amount, book, template, to_email)
        send_borrow_email(self.request.user, book.price,
                          book, "borrow_email.html", self.request.user.email)
        return redirect('profile')


class ReturnView(View):
    def get(self, request, id):
        borrowed_book = BorrowHistory.objects.get(id=id)
        borrow_price = borrowed_book.book.price
        account = self.request.user.account
        account.balance += borrow_price
        account.save(update_fields=['balance'])
        borrowed_book.delete()
        return redirect("profile")


class DepositView(FormView):
    template_name = "deposit.html"
    form_class = DespositForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        amount = form.cleaned_data["amount"]
        account = UserAccount.objects.get(user=self.request.user)
        account.balance += amount
        account.save(update_fields=['balance'])

        # send_deposit_email(user, amount, template, to_email):
        send_deposit_email(self.request.user, amount,
                           "deposit_email.html", account.user.email)
        return super().form_valid(form)
