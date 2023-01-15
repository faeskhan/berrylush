from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse 
import os
from . models import Product, Review
from . forms import ReviewForm, UserForm, RegisterForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def index(request):
    review = Review.objects.all()
    context = {'review': review}
    return render(request, 'index.html', context)

def authenticationlogin(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('index')

    form = UserForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('reviews-create-edit')
        else:
            print('Username/Email OR Password is incorrect')

    context = {'form': form, 'page': page}
    return render(request, 'authentication-log-in.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def register(request):
    page = 'register'           #This is used in the authentication html to diffretiate whether the user is loging in or signing up
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'User acount was created!')
            return redirect('reviews-create-edit')
        else:
            messages.error(request, 'Something went wrong... try again')
            

    context={'form': form, 'page': page}
    return render(request, 'authentication-log-in.html', context)

def contactus(request):
    return render(request, 'contact-us.html')

def planyourvisit(request):
    return render(request, 'plan-your-visit.html')

def products(request):
    query = ''

    if request.GET.get('query'):
        query = request.GET.get('query') 

    products = Product.objects.distinct().filter(Q(title__icontains = query) | Q(bio__icontains = query) | Q(price__icontains = query) | Q(category__icontains = query))
    categories = Product.objects.distinct().values_list('category', flat=True)
    context = {'query': query, 'products': products, 'categories': categories}
    return render(request, 'products.html', context)

def samplePDF(request):
    filepath = os.path.join('documents', 'samplePDF.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def reviewscreateedit(request):
    form = ReviewForm()


    if request.user.is_authenticated:
        review = Review.objects.distinct().filter(Q(owner = request.user))

        page = request.GET.get('page')
        results = 4
        paginator = Paginator(review, results)

        try:
            review = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            review = paginator.page(page)
        except EmptyPage:
            page = paginator.num_pages
            review = paginator.page(page)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                review = form.save(commit=False) 
                review.owner = request.user
                review.save()
            else:
                form.save()
            return redirect('reviews-create-edit')
        else:
            print('something went wrong')
    if request.user.is_authenticated:
        context = {'review': review, 'form': form, 'paginator': paginator}
    else:
        context = {'form': form}
    return render(request, 'reviews-create-edit.html', context)
    
def detail_reviews(request, pk):
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews-create-edit')

    context = {'form': form}
    return render(request, 'detail_reviews.html', context)

def delete_review(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('reviews-create-edit')