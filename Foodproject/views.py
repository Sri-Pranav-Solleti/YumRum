from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages  
from .models import *
import http;
# Create your views here.
def register(request):
    if(request.method=="POST"):
        data=request.POST
        user_name=data.get('name')
        email=data.get('email')
        password=data.get('password')
        user=User.objects.filter(username=user_name)
        if user.exists():
            messages.error(request, "Username already exists! Please try a different one.")
            return render(request,'signup.html')
        user=User.objects.create(username=user_name,email=email)
        user.set_password(password)
        user.save()
        print(user)
        login(request, user)
        context=request.user.username
        return redirect('home1')
    return render(request,'signup.html')

def login_view(request):
    if(request.method=="POST"):
        data=request.POST
        user_name=data.get('username')
        password=data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request,user)
            context=request.user.username
            return redirect('home1')
        else:
            messages.error(request,"Invalid username or password")
    return render(request,'login.html')
def logout_view(request):
    logout(request)
    return redirect('login_view')
    
def home1(request):
    context = {'data': request.user.username if request.user.is_authenticated else "Guest"}
    return render(request, 'home.html', context)
def aboutus(request):
    return render(request,'aboutus.html')



def menu(request):
    query = request.GET.get('search', '')  
    if query:
        menu_items = menuitem.objects.filter(name__icontains=query).order_by('name') 
    else:
        menu_items = menuitem.objects.all().order_by('name')  
    return render(request, 'menu.html', {'data': menu_items, 'query': query})


def confirm(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist("selected_items") 
        cart.objects.all().delete()  
        if selected_ids:
            for i in selected_ids:
                menu_item_obj = menuitem.objects.get(id=i)
                quantity_field = f"quantity_{i}"  
                quantity = int(request.POST.get(quantity_field, 1))  
                cart.objects.create(
                    menu_item=menu_item_obj,
                    number=quantity
                )
            return redirect('placeorder')  
    return HttpResponse("No items selected.")


def placeorder(request):
    data = cart.objects.all()
    if not data:  
        return HttpResponse("Your cart is empty. Please select items first.")
    for item in data:
        item.total_price = item.number * item.menu_item.price
    grand_total = sum(item.total_price for item in data)
    tax_rate = 0.05
    tax = round(grand_total * tax_rate, 2) 
    final_total = round(grand_total + tax, 2)

    return render(request, 'placeorder.html', {
        'data': data,
        'grand_total': grand_total,
        'tax': tax,
        'final_total': final_total
    })



def reservation(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("phone")
        date1 = request.POST.get("checkin")
        date2 = request.POST.get("checkout")
        guests = request.POST.get("guests")
        special = request.POST.get("requests")

       

        # Create the reservation
        reservation = Reservation.objects.create(
            user=request.user,  # Assign the logged-in user
            name=name,
            email=email,
            number=number,
            date1=date1,
            date2=date2,
            guests=guests,
            special=special
        )
        reservation.save()
        print("Success")
        return redirect("thank")  
    return render(request, "reservation.html")

def thank(request):
    return render(request,'reservety.html')
def end(request):
    return render(request,'end.html')
def reviews(request):
    if request.method=="POST":
        data=request.POST
        user=request.user
        name=data.get('name')
        description=data.get('desc')
        obj=Review.objects.create(user=user,name=name,description=description)
        obj.save()
        print('success')
        return redirect('feedback')
    return render(request,'reviews.html')

def feedback(request):
    return render(request,'tk.html')

def contactus(request):
    return render(request,'contactus.html')
def gallery (request):
    return render(request,'gallery.html')




         
