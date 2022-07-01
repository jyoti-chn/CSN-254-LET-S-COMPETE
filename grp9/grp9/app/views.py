import re
from django.contrib.auth.models import Group,User
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer,Product,Carts,EventRegistered
from .forms import CustomerRegistrationForm, CustomerProfileForm,OrgRegistrationForm

from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductView(View):
  def get(self,request):

     Hackathons = Product.objects.filter(category='H')
     Courses = Product.objects.filter(category='C')
     Internships = Product.objects.filter(category='I')
     Scholarships= Product.objects.filter(category='S')
     CulEvents= Product.objects.filter(category='CE')

     return render(request,'app/home.html',{'Hackathons':Hackathons, 'Courses':Courses, 'Internships':Internships, 'Scholarships':Scholarships, 'CulEvents':CulEvents})





class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart= False
        if request.user.is_authenticated:
                    item_already_in_cart= Carts.objects.filter(Q(product=product.id) &Q(user=request.user))
        return render(request,'app/eventdetail.html',{'product':product ,'item_already_in_cart':item_already_in_cart})




@login_required()
def add_to_cart(request):
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Carts(user=user, product=product).save()
        return redirect('/showevents')
@login_required()
def show_events(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Carts.objects.filter(user=user)
        print(cart)

        cart_product = [p for p in Carts.objects.all() if p.user == request.user]

        if cart_product:
            for p in cart_product:
                return render(request, 'app/showevents.html',{'cart':cart ,})
        else:
            return render(request, 'app/noevents.html')


@login_required()
def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

@login_required()
def orders(request):
    op = EventRegistered.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'order_placed':op})


def Hackathons(request,data=None):
    if data == None:
        Hackathons = Product.objects.filter(category='H')

    return render(request, 'app/hackathons.html',{'Hackathons':Hackathons})

def Courses(request,data=None):
    if data == None:
        Courses = Product.objects.filter(category='C')

    return render(request, 'app/courses.html',{'Courses':Courses})

def Scholarships(request,data=None):
    if data == None:
        Scholarships = Product.objects.filter(category='S')

    return render(request, 'app/scholarships.html',{'Scholarships':Scholarships})

def Internships(request,data=None):
    if data == None:
        Internships = Product.objects.filter(category='I')

    return render(request, 'app/internships.html',{'Internships':Internships})

def CulEvents(request,data=None):
    if data == None:
        CulEvents = Product.objects.filter(category='CE')

    return render(request, 'app/culevents.html',{'CulEvents':CulEvents})


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        tle = Product.objects.all().filter(title__icontains=search)
        cat = Product.objects.all().filter(category__icontains=search)
        bnd = Product.objects.all().filter(brand__icontains=search)
        desc = Product.objects.all().filter(description__icontains=search)

        post=tle|cat|bnd|desc
        return render(request,'app/searchbar.html',{'post':post})

class OrgRegistrationView(View):

    def get(self,request):
        form =OrgRegistrationForm()
        return render(request, 'app/orgregistration.html',{'form':form})


    def post(self,request):
        form=OrgRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! You are registered Successfully!')
            user=form.save()
            group = Group.objects.get(name='ShopOwner')
            user.groups.add(group)
        return render(request,'app/orgregistration.html',{'form':form})


class CustomerRegistrationView(View):

    def get(self,request):
        form =CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})


    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! You are registered Successfully!')
            user = form.save()
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
        return render(request,'app/customerregistration.html',{'form':form})




@method_decorator(login_required(), name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html' , {'form':form,'active':'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']

            reg = Customer(user=usr,name=name, locality=locality, city=city)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
            return render(request, 'app/profile.html', {'form':form,'active':'btn-primary'})








