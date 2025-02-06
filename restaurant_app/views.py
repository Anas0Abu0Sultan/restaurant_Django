from django.shortcuts import render
from .models import AboutUs, AboutUsImage, Rest_detail,Services,Drinks,Meals,Sandwiches,Grills,Sweets,Salads,Chefs,Clients
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import QuerySet


def test(request):
    services = Services.objects.all()
    return render(request, 'restaurant/navbar_other.html',{'services':services})






def home(request):
    rest_detail = get_object_or_404(Rest_detail,pk =1)
    services = Services.objects.all()
    about_us = AboutUs.objects.first()
    about_us_images = AboutUsImage.objects.filter(about_us=about_us) if about_us else None
    drinks = Drinks.objects.all()
    meals = Meals.objects.all()
    sandwiches = Sandwiches.objects.all()
    grills = Grills.objects.all()
    sweets = Sweets.objects.all()
    salads = Salads.objects.all()
    chefs = Chefs.objects.all()
    clients = Clients.objects.all()
    context = {
        'rest_detail': rest_detail,
        'services': services,
        'about_us': about_us,
        'about_us_images': about_us_images,
        'drinks': drinks,
        'meals': meals,
        'sandwiches': sandwiches,
        'grills': grills,
        'sweets': sweets,
        'salads': salads,
        'chefs': chefs,
        'clients': clients,
        }
    return render(request,'restaurant/index.html',context)


def about(request):
    about_us = AboutUs.objects.first()
    about_us_images = AboutUsImage.objects.filter(about_us=about_us) if about_us else None
    chefs_list = Chefs.objects.all()
    paginator = Paginator(chefs_list,8)
    page_number = request.GET.get('page')
    chefs  = paginator.get_page(page_number)

    context = {
        'about_us': about_us,
        'about_us_images': about_us_images,
        'page_title': 'About Us',
        'breadcrumb_section': 'Services',
        'breadcrumb_active': 'About',
        'about':'active',
        'chefs':chefs,
        }
    return render(request,'restaurant/about.html',context)






def service(request):
    services = Services.objects.all()
    context = {
        'services': services,
        'service':'active',
        'page_title': 'Services',
        'breadcrumb_section': 'About',
        'breadcrumb_active': 'Services',
        }
    return render(request,'restaurant/services.html',context)




# def menu(request):
#     drinks = Drinks.objects.all()
#     meals = Meals.objects.all()
#     sandwiches = Sandwiches.objects.all()
#     grills = Grills.objects.all()
#     sweets = Sweets.objects.all()
#     salads = Salads.objects.all()

#     context = {
#         'menu':'active',
#         'page_title': 'Food Menu',
#         'breadcrumb_section': 'About',
#         'breadcrumb_active': 'Menu',
#         'drinks': drinks,
#         'meals': meals,
#         'sandwiches': sandwiches,
#         'grills': grills,
#         'sweets': sweets,
#         'salads': salads,
#         }
#     return render(request,'restaurant/menu.html',context)


from itertools import chain
from random import shuffle
def menu(request, category):

    drinks = Drinks.objects.all().order_by('-price')
    meals = Meals.objects.all().order_by('-price')
    sandwiches = Sandwiches.objects.all().order_by('-price')
    grills = Grills.objects.all().order_by('-price')
    sweets = Sweets.objects.all().order_by('-price')
    salads = Salads.objects.all().order_by('-price')

        # Filter menu items based on the selected category
    if category == 'drinks':
        items = drinks
        name_page = 'Drinks'
    elif category == 'meals':
        items = meals
        name_page = 'Meals'
    elif category == 'sandwiches':
        items = sandwiches
        name_page = 'Sandwiches'
    elif category == 'grills':
        items = grills
        name_page = 'Grills'
    elif category == 'sweets':
        items = sweets
        name_page = 'Sweets'
    elif category == 'salads':
        items = salads
        name_page = 'Salads'
    else:
        # Combine all categories using chain and shuffle the items
        combined_items = list(chain(drinks, meals, sandwiches, grills, sweets, salads))
        shuffle(combined_items)  # Shuffle the combined items
        items = combined_items[:10]  # Get 10 random items
        name_page = 'Most Popular Items'

    # Ensure there are items before slicing
    if items:
        half = len(items) // 2
        first_half = items[:half]
        second_half = items[half:]
    else:
        first_half = []
        second_half = []



    
    context = {
        'menu':'active',
        'page_title': 'Food Menu',
        'breadcrumb_section': 'About',
        'breadcrumb_active': 'Menu',
        'items': items,
        'category': category,
        'first_half': first_half,
        'second_half': second_half,
        'name_page': name_page,
        }
    return render(request,'restaurant/menu.html',context)




def testimonial(request):
    clients = Clients.objects.all()
    context = {
        'clients': clients,
        }
    return render(request,'testimonial.html',context)

def our_team(request):
    chefs = Chefs.objects.all()
    context = {
        'chefs': chefs,
        }
    return render(request,'team.html',context)




def contact(request):
    pass

def booking(request):
    pass