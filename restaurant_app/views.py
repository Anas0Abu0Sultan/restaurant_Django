from django.shortcuts import render
from .models import AboutUs, AboutUsImage, Rest_detail,Services,Drinks,Meals,Sandwiches,Grills,Sweets,Salads,Chefs,Clients
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

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




def menu(request):
    drinks = Drinks.objects.all()
    meals = Meals.objects.all()
    sandwiches = Sandwiches.objects.all()
    grills = Grills.objects.all()
    sweets = Sweets.objects.all()
    salads = Salads.objects.all()

    context = {
        'drinks': drinks,
        'meals': meals,
        'sandwiches': sandwiches,
        'grills': grills,
        'sweets': sweets,
        'salads': salads,
        }
    return render(request,'menu.html',context)





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