from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Transaction

def expense_list(request):
    expenses = Transaction.objects.all()
    return render(request, 'budget/category.html', {'expenses': expenses})

