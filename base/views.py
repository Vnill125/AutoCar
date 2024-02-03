from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Car, Profile, User, Message, Chat
from .filters import CarFilter
from .forms import RegisterForm, CarForm , CarImageFormSet, ProfileForm

def index(request):
    page = 'index'
    filter = CarFilter(request.GET, queryset=Car.objects.all())
    cars = filter.qs

    order_by_options = {
        '1': 'price',
        '2': '-price',
        '3': 'horse_power',
        '4': '-horse_power',
        '5': 'first_registration_year',
        '6': '-first_registration_year',
    }


    order_by_param = request.GET.get('order_by', '-first_registration_year')
    
    if 'auto' in filter.data:
        order_by_param += f'&auto={filter.data["auto"]}'
         
        if 'brand' in filter.data:
            order_by_param += f'&brand={filter.data["brand"]}'
        if 'model' in filter.data:
                order_by_param += f'&model={filter.data["model"]}'
        if 'body' in filter.data:
                order_by_param += f'&body={filter.data["body"]}'
        if 'first_registration_year' in filter.data:
                order_by_param += f'&first_registration_year={filter.data["first_registration_year"]}'
        if 'fuel_type' in filter.data:
                order_by_param += f'&fuel_type={filter.data["fuel_type"]}'
        if 'max_price' in filter.data:
                order_by_param += f'&max_price={filter.data["max_price"]}'

    order_by_param = order_by_param.lstrip('&')
            
    cars = cars.order_by(order_by_options.get(order_by_param, '-first_registration_year'))

    return render(request, 'index.html', context={'cars': cars, 'filter': filter, 'order_by': order_by_param, 'page':page})
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(request, username=username, password=password)
                
        if User is not None:
            auth_login(request, User)
            messages.success(request, f'Welcome back {username}')
            return redirect('index')
        else:
            messages.error(request,'Wrong password or username! Try again!')
                
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

def register(request):
    form = RegisterForm()
  
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save()
            user.save()
            Profile.objects.create(user=user)
            messages.success(request, f'You have singed up successfully. Welcome {user.username}!')
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Something went wrong! Try again!')
            return render(request, 'register.html', {'form': form})
        
    return render(request, 'register.html', context={'form':form})


def car(request, pk):
    car = Car.objects.get(id=pk)
    return render(request, 'car.html', {'car': car})

@login_required
def new_order(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        formset = CarImageFormSet(request.POST, request.FILES, instance=Car())

        if form.is_valid() and formset.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            formset.instance = car
            formset.save()
            return redirect('car', pk=car.pk)
    else:
        form = CarForm()
        formset = CarImageFormSet(instance=Car())

    return render(request, 'new_order.html', {'form': form, 'formset': formset})

@login_required
def edit_car(request, pk):
    car = Car.objects.get(id=pk)
    form = CarForm(instance=car)
    formset = CarImageFormSet(instance=car)
    
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        formset = CarImageFormSet(request.POST, request.FILES, instance=car)
        
        if form.is_valid() and formset.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            formset.save()
            return redirect('car', pk=car.pk)
    
    return render(request, 'new_order.html', context={'form': form, 'formset': formset})

@login_required
def my_profile(request):
    user = request.user
    form = ProfileForm(instance=user.profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Profile updated!')
            return redirect('my_profile')

    return render(request, 'my_profile.html', context={'user':user, 'form':form})

def user_profile(request,pk):
    user = User.objects.get(id=pk)
    return render(request ,'user_profile.html', context={'user':user})

@login_required
def view_chats(request):
    chats = Chat.objects.filter(participants=request.user)
    chat_entries = []
    
    for chat in chats:
        participant = chat.participants.exclude(id=request.user.id).first()
        
        chat_entries.append((chat, participant))
    
    return render(request, 'my_chats.html', context={'chat_entries': chat_entries})

@login_required
def chat(request, recipient_id):
    user = request.user
    recipient = get_object_or_404(User, id=recipient_id)
    
    chat = Chat.objects.filter(participants=user).filter(participants=recipient).first()
    
    if not chat:
        chat = Chat.objects.create(title=f"Chat between {user.username} and {recipient.username}")
        chat.participants.add(user, recipient)
        
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(sender=request.user, recipient=recipient, content=content, chat=chat)

    return render(request, 'chat.html', {'chat': chat})

@login_required
def my_listings(request):
    user = request.user
    listings = user.car_set.all()
    return render(request, 'my_listings.html', context={'user':user, 'listings':listings})
