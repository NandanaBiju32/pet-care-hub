# from django.shortcuts import render
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from .models import Pet
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.http import HttpResponse
# # def index(request):
# #     return HttpResponse("Hello World")
#
# def home(request):
#     return render(request, 'home.html')
#
# # def login_page(request):
# #     return render(request, 'login.html')
#
# def login_page(request):
#
#     if request.method == "POST":
#
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request,
#                             username=username,
#                             password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#
#     return render(request, 'login.html')
#
# def buy_now(request):
#
#     if not request.user.is_authenticated:
#         return redirect('login')
#
#     return render(request, 'success.html')
#
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
#
# # Home Page
# def home(request):
#     return render(request, 'home.html')
#
#
# # Login Page
# # def login_page(request):
# #
# #     if request.method == "POST":
# #
# #         username = request.POST.get('username')
# #         password = request.POST.get('password')
# #
# #         user = authenticate(
# #             request,
# #             username=username,
# #             password=password
# #         )
# #
# #         if user is not None:
# #             login(request, user)
# #             return redirect('home')
# #
# #     return render(request, 'login.html')
#
# # LOGIN PAGE
# # def login_page(request):
# #
# #     next_url = request.GET.get('next')
# #
# #     if request.method == "POST":
# #
# #         username = request.POST.get('username')
# #         password = request.POST.get('password')
# #
# #         user = authenticate(
# #             request,
# #             username=username,
# #             password=password
# #         )
# #
# #         if user is not None:
# #
# #             login(request, user)
# #
# #             # RETURN TO PREVIOUS PAGE
# #             if next_url:
# #                 return redirect(next_url)
# #
# #             return redirect('home')
# #
# #     return render(request, 'login.html')
#
#
# def login_page(request):
#
#     if request.method == "POST":
#
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         # GET NEXT URL FROM FORM
#         next_url = request.POST.get('next')
#
#         user = authenticate(
#             request,
#             username=username,
#             password=password
#         )
#
#         if user is not None:
#
#             login(request, user)
#
#             # REDIRECT TO NEXT PAGE
#             if next_url:
#                 return redirect(next_url)
#
#             return redirect('home')
#
#     return render(request, 'login.html')
# # Adopt Page
#
#
# # ADOPTION PAGE
# def adopt_page(request):
#
#     # DEFAULT PETS
#     default_pets = [
#
#         {
#             'image': 'https://images.unsplash.com/photo-1517849845537-4d257902454a?w=500',
#             'name': 'Buddy',
#             'pet_type': 'Dog',
#             'breed': 'Golden Retriever',
#             'place': 'Kochi',
#             'age': '2 Years',
#             'weight': '12 Kg',
#             'owner_name': 'Rahul',
#             'contact': '9876543210'
#         },
#
#         {
#             'image': 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=500',
#             'name': 'Kitty',
#             'pet_type': 'Cat',
#             'breed': 'Persian',
#             'place': 'Ernakulam',
#             'age': '1 Year',
#             'weight': '4 Kg',
#             'owner_name': 'Anjali',
#             'contact': '9876501234'
#         },
#
#         {
#             'image': 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=500',
#             'name': 'Rocky',
#             'pet_type': 'Dog',
#             'breed': 'Labrador',
#             'place': 'Thrissur',
#             'age': '3 Years',
#             'weight': '18 Kg',
#             'owner_name': 'Arjun',
#             'contact': '9876511111'
#         }
#
#     ]
#
#     # DATABASE PETS
#     db_pets = Pet.objects.all()
#
#     return render(request, 'adopt.html', {
#         'default_pets': default_pets,
#         'db_pets': db_pets
#     })
#
#
# # Add Pet Page
#
#
# # ADD PET PAGE
# # def add_pet(request):
# #
# #     # CHECK LOGIN
# #     if not request.user.is_authenticated:
# #         return redirect('login')
# #
# #     if request.method == 'POST':
# #
# #         pet_type = request.POST.get('pet_type')
# #         breed = request.POST.get('breed')
# #         name = request.POST.get('name')
# #         place = request.POST.get('place')
# #         age = request.POST.get('age')
# #         weight = request.POST.get('weight')
# #         owner_name = request.POST.get('owner_name')
# #         contact = request.POST.get('contact')
# #         image = request.POST.get('image')
# #
# #         # SAVE PET
# #         Pet.objects.create(
# #             pet_type=pet_type,
# #             breed=breed,
# #             name=name,
# #             place=place,
# #             age=age,
# #             weight=weight,
# #             owner_name=owner_name,
# #             contact=contact,
# #             image=image
# #         )
# #
# #         return redirect('adopt')
# #
# #     return render(request, 'add_pet.html')
#
# # ADD PET PAGE
# def add_pet(request):
#
#     # CHECK LOGIN
#     if not request.user.is_authenticated:
#         return redirect('/login/?next=/add-pet/')
#
#     if request.method == 'POST':
#
#         pet_type = request.POST.get('pet_type')
#         breed = request.POST.get('breed')
#         name = request.POST.get('name')
#         place = request.POST.get('place')
#         age = request.POST.get('age')
#         weight = request.POST.get('weight')
#         owner_name = request.POST.get('owner_name')
#         contact = request.POST.get('contact')
#         image = request.POST.get('image')
#
#         # SAVE PET
#         Pet.objects.create(
#             pet_type=pet_type,
#             breed=breed,
#             name=name,
#             place=place,
#             age=age,
#             weight=weight,
#             owner_name=owner_name,
#             contact=contact,
#             image=image
#         )
#
#         return redirect('adopt')
#
#     return render(request, 'add_pet.html')
#
#
# # BUY NOW PAGE
# def buy_now(request):
#
#     # CHECK LOGIN
#     if not request.user.is_authenticated:
#         return redirect('login')
#
#     return render(request, 'success.html')
#
#
# def payment_page(request):
#
#     product = request.GET.get('product')
#     price = request.GET.get('price')
#
#     context = {
#         'product': product,
#         'price': price
#     }
#
#     return render(request,
#                   'payment.html',
#                   context)
#
# def register_user(request):
#
#     if request.method == 'POST':
#
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         # CHECK USERNAME EXISTS
#         if User.objects.filter(username=username).exists():
#
#             messages.error(request,
#                            "Username already exists")
#
#             return redirect('register')
#
#         # CREATE USER
#         user = User.objects.create_user(
#
#             username=username,
#             email=email,
#             password=password
#
#         )
#
#         user.save()
#
#         messages.success(request,
#                          "Registration Successful")
#
#         return redirect('login')
#
#     return render(request,
#                   'register.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Pet



def home(request):

    return render(request, 'home.html')


def login_page(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        next_url = request.POST.get('next')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)


            if next_url:
                return redirect(next_url)

            return redirect('dashboard')

        else:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(request, 'login.html')

def buy_now(request):


    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'success.html')




def register_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect('register')


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(
            request,
            "Registration Successful"
        )

        return redirect('login')

    return render(request, 'register.html')


def adopt_page(request):


    default_pets = [

        {
            # 'image': 'https://images.unsplash.com/photo-1517849845537-4d257902454a?w=500',
            'name': 'Buddy',
            'pet_type': 'Dog',
            'breed': 'Golden Retriever',
            'place': 'Kochi',
            'age': '2 Years',
            'weight': '12 Kg',
            'owner_name': 'Rahul',
            'contact': '9876543210'
        },

        {
            # 'image': 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=500',
            'name': 'Kitty',
            'pet_type': 'Cat',
            'breed': 'Persian',
            'place': 'Ernakulam',
            'age': '1 Year',
            'weight': '4 Kg',
            'owner_name': 'Anjali',
            'contact': '9876501234'
        }

    ]


    db_pets = Pet.objects.all()

    return render(request, 'adopt.html', {

        'default_pets': default_pets,
        'db_pets': db_pets

    })


# ADD PET PAGE
def add_pet(request):

    # LOGIN CHECK
    if not request.user.is_authenticated:

        return redirect('/login/?next=/add-pet/')

    if request.method == 'POST':

        pet_type = request.POST.get('pet_type')
        breed = request.POST.get('breed')
        name = request.POST.get('name')
        place = request.POST.get('place')
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        owner_name = request.POST.get('owner_name')
        contact = request.POST.get('contact')
        # image = request.POST.get('image')
        # image = models.ImageField(upload_to='pets/')
        image = request.FILES.get('image')

        # SAVE PET
        Pet.objects.create(

            pet_type=pet_type,
            breed=breed,
            name=name,
            place=place,
            age=age,
            weight=weight,
            owner_name=owner_name,
            contact=contact,
            image=image

        )

        messages.success(
            request,
            "Pet Added Successfully 🐾"
        )

        return redirect('adopt')

    return render(request, 'add_pet.html')


# PAYMENT PAGE
def payment_page(request):

    # LOGIN CHECK
    if not request.user.is_authenticated:

        return redirect('/login/?next=/payment/')

    product = request.GET.get('product')
    price = request.GET.get('price')

    context = {

        'product': product,
        'price': price

    }

    return render(
        request,
        'payment.html',
        context
    )


# LOGOUT
def logout_user(request):

    logout(request)

    return redirect('home')


# USER DASHBOARD

def dashboard(request):

    # LOGIN CHECK
    if not request.user.is_authenticated:

        return redirect('login')

    # USER ADDED PETS
    pets = Pet.objects.filter(
        owner_name=request.user.username
    )

    context = {

        'pets': pets

    }

    return render(request,
                  'dashboard.html',
                  context)


def edit_pet(request, id):

    pet = Pet.objects.get(id=id)

    if request.method == 'POST':

        pet.name = request.POST.get('name')
        pet.breed = request.POST.get('breed')
        pet.place = request.POST.get('place')
        pet.age = request.POST.get('age')

        pet.save()

        return redirect('dashboard')

    return render(
        request,
        'edit_pet.html',
        {'pet': pet}
    )


# DELETE PET
def delete_pet(request, id):

    pet = Pet.objects.get(id=id)

    pet.delete()

    return redirect('dashboard')


# ALL PRODUCTS PAGE




def success(request):

    return render(request,
                  'success.html')

# ALL PRODUCTS PAGE
from .models import Product


# PRODUCTS PAGE
def products_page(request):

    # WEBSITE PRODUCTS

    products = [

        # FOOD PRODUCTS

        {
            'id': 1,
            'name': 'Premium Dog Food',
            'price': 1200,
            'category': 'Food',
            'image': 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=500',
            'description': 'Healthy dog food rich in protein and vitamins.'
        },

        {
            'id': 2,
            'name': 'Cat Food',
            'price': 950,
            'category': 'Food',
            'image': 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=500',
            'description': 'Nutritious food for healthy cats.'
        },


        # MEDICINES

        {
            'id': 3,
            'name': 'Pet Medicine',
            'price': 850,
            'category': 'Medicine',
            'image': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=500',
            'description': 'Effective medicine for pet immunity and health.'
        },

        {
            'id': 4,
            'name': 'Pet Shampoo',
            'price': 450,
            'category': 'Medicine',
            'image': 'https://images.unsplash.com/photo-1517849845537-4d257902454a?w=500',
            'description': 'Gentle shampoo for pet skin care.'
        },


        # ACCESSORIES

        {
            'id': 5,
            'name': 'Dog Leash',
            'price': 500,
            'category': 'Accessories',
            'image': 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=500',
            'description': 'Strong and stylish leash for your pet.'
        },

        {
            'id': 6,
            'name': 'Pet Bed',
            'price': 1500,
            'category': 'Accessories',
            'image': 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=500',
            'description': 'Comfortable bed for pets.'
        }

    ]




    added_products = Product.objects.all()


    return render(
        request,
        'products.html',
        {
            'products': products,
            'added_products': added_products
        }
    )


def view_product(request, id):

    products = [

        {
            'id': 1,
            'name': 'Premium Dog Food',
            'price': 1200,
            'category': 'Food',
            'image': 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=500',
            'description': 'Healthy dog food rich in protein and vitamins.'
        },

        {
            'id': 2,
            'name': 'Pet Medicine',
            'price': 850,
            'category': 'Medicine',
            'image': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=500',
            'description': 'Effective medicine for pet immunity and health.'
        },

        {
            'id': 3,
            'name': 'Dog Leash',
            'price': 500,
            'category': 'Accessories',
            'image': 'https://images.unsplash.com/photo-1517849845537-4d257902454a?w=500',
            'description': 'Strong and stylish leash for your pet.'
        }

    ]

    product = None

    for item in products:

        if item['id'] == id:

            product = item

    return render(
        request,
        'view_product.html',
        {'product': product}
    )

def logout_view(request):
    logout(request)
    return redirect('home')

def contact_owner(request, id):


    default_pets = [

        {
            'id': 1,
            'image': 'https://images.unsplash.com/photo-1517849845537-4d257902454a?w=500',
            'name': 'Buddy',
            'owner_name': 'Rahul',
            'contact': '9876543210',
            'place': 'Kochi'
        },

        {
            'id': 2,
            'image': 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=500',
            'name': 'Kitty',
            'owner_name': 'Anjali',
            'contact': '9876501234',
            'place': 'Ernakulam'
        }

    ]



    for pet in default_pets:

        if pet['id'] == id:

            return render(
                request,
                'contact_owner.html',
                {'pet': pet}
            )



    pet = Pet.objects.get(id=id)

    return render(
        request,
        'contact_owner.html',
        {'pet': pet}
    )