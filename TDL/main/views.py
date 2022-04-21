from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import *
from .form import *
from django import forms


def home(request):
    customers = Customer.objects.all()
    items = Item.objects.all()
    context = {'items': items, 'customers': customers}
    return render(request, "main/dashboard.html", context)

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    items = customer.item_set.all()
    
    formset = CustomerFormSet(queryset=Item.objects.none(), instance=customer)

    if request.method == "POST":
        formset = CustomerFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('customer', pk)

    context = {'items': items, 'formset': formset}
    return render(request, "main/customer.html", context)

def delete(request, pk):
    items = Item.objects.get(id=pk)
    if request.method == "POST":
        items.delete()
        return redirect('/')
    context = {'items': items}
    return render(request, "main/update_item.html", context)

def finished(request, pk):
    items = Item.objects.get(id=pk)
    if request.method == "POST":
        items.status = "Completed"
        items.save()
        return redirect('/')
    context = {'items': items}
    return render(request, "main/update_item.html", context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        Customer.objects.create(
                user=user,
        )
        login(request, user)
        return redirect('/')

    context = {'form': form}
    return render(request, "main/register.html", context)
