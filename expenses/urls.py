from django.urls import path
from .views import (
    login_view, logout_view, profile_view, register_view,
    add_category_view, add_item_view, add_transaction_view,
    category_view, edit_category_view,  edit_transaction_view,
    reports_view, transactions_view,
)


app_name = 'expenses'

urlpatterns = [
    path('', login_view, name='login'),
    path('budget/category/', category_view, name='expense_list'),
    path('budget/logout/', logout_view, name='logout'),
    path('budget/profile/', profile_view, name='profile'),
    path('budget/Register/', register_view, name='register'),
    path('budget/addcategory/', add_category_view, name='add_category'),
    path('budget/additem/', add_item_view, name='add_item'),
    path('budget/addtransaction/', add_transaction_view, name='add_transaction'),
    path('budget/editcategory/<int:category_id>/', edit_category_view, name='edit_category'),
    path('budget/edittransaction/<int:transaction_id>/', edit_transaction_view, name='edit_transaction'),
    path('budget/reports/', reports_view, name='reports'),
    path('budget/transactions/', transactions_view, name='transactions'),
]

