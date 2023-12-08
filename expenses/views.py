from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Transaction, Category, Report, AccountInfo
from .forms import RegistrationForm, TransactionForm, CategoryForm, ItemForm, LoginForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            print(f'User: {user}')

            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful, Welcome!')
                return redirect('expenses:category')
            else:
                messages.error(request, 'Invalid login. Please try again.')
        else:
            messages.error(request, 'Invalid form submission. Please check your input.')
    else:
        form = LoginForm()

    return render(request, 'budget/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout is successful Thanks for using Budgetly')
    return redirect('budget/profile.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Check if the user with the same username or email already exists
            if AccountInfo.objects.filter(username=username).exists() or AccountInfo.objects.filter(email=email).exists():
                messages.error(request, 'Username or email already exists.')
            else:
                form.save()
                messages.success(request, f'Account successfully created. Welcome, {username}.')
                return redirect('expenses:profile')
        else:
            print('Form is invalid:', form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'budget/Register.html', {'form': form})

def profile_view(request):
    return render(request, 'budget/profile.html')

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



