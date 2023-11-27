from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Transaction, Category, Item, AccountInfo, Report
from .forms import RegistrationForm, TransactionForm, CategoryForm, ItemForm
# Create your views here.

from django.shortcuts import render
from .models import Transaction

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful, Welcome!')
            return redirect('profile_view')  # Use the correct URL name
        else:
            messages.error(request, 'Invalid login. Please try again.')

    return render(request, 'budget/login/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout is successful Thanks for using Budgetly')
    return redirect('budget/login/profile.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created your username is {username}. Welcome.')
            return redirect('budget/login/profile.html')
        else:
            form = RegistrationForm()

        return render(request, 'budget/login/Register.html', {'form': form})

def profile_view(request):
    return render(request, 'budget/login/profile.html')

def add_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
         form.save()
        return redirect('budget/category.html')    
    else:
        form = CategoryForm()
    return render(request, 'budget/addcategory.html', {'form': form})

def add_item_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
         form.save()
        return redirect('budget/category.html')    
    else:
        form = CategoryForm()
    return render(request, 'budget/additem.html', {'form': form})

def add_transaction_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction added successfully!')
            return redirect('transactions')  # Make sure 'transactions_view' is the name of the URL pattern where you list transactions
    else:
        form = TransactionForm()
    return render(request, 'budget/addtransaction.html', {'form': form})

def category_view(request):
    categories = Category.objects.all()
    return render(request, 'budget/category.html', {'categories': categories})

def edit_category_view(request, category_id):
    category = Category.objects.get(pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('budget/category.html')    
    else:
        form = CategoryForm(instance=category)
    return render(request, 'budget/editcategory.html', {'form': form, 'category': category})

def edit_transaction_view(request, transaction_id):
    transaction = Transaction.objects.get(pk=transaction_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('budget/transaction.html')    
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'budget/edittransaction.html', {'form': form, 'transaction': transaction})

def reports_view(request):
    reports = Report.objects.all()
    return render(request, 'budget/reports.html')


def transactions_view(request):
    transactions = Transaction.objects.all()
    return render(request, 'budget/transactions.html', {'transactions': transactions})



