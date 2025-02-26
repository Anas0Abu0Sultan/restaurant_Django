from django.shortcuts import render
from .models import AboutUs, AboutUsImage, Rest_detail,Services,Drinks,Meals,Sandwiches,Grills,Sweets,Salads,Chefs,Clients,Contact,Cart,CartItem
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import QuerySet
import random
from django.urls import reverse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from itertools import chain
from random import shuffle
from django.contrib.auth.decorators import login_required

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
    clients = Clients.objects.all()
    chefs = Chefs.objects.all()
    if chefs.count()>=4:
        chefs = random.sample(list(chefs), 4)

    combined_items = list(chain(drinks, meals, sandwiches, grills, sweets, salads))
    shuffle(combined_items)  # Shuffle the combined items
    items = combined_items[:10]  # Get 10 random items

    # Ensure there are items before slicing
    if items:
        half = len(items) // 2
        first_half = items[:half]
        second_half = items[half:]
    else:
        first_half = []
        second_half = []

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
        'first_half': first_half,
        'second_half': second_half,
        }
    return render(request,'restaurant/index.html',context)


def about(request):
    about_us = AboutUs.objects.first()
    about_us_images = AboutUsImage.objects.filter(about_us=about_us) if about_us else None
    chefs_list = Chefs.objects.all()
    paginator = Paginator(chefs_list,8)
    page_number = request.GET.get('page')
    chefs  = paginator.get_page(page_number)
    rest_detail = get_object_or_404(Rest_detail,pk =1)
    breadcrumb_section_url = reverse('restaurant_app:services')


    context = {
        'about_us': about_us,
        'about_us_images': about_us_images,
        'page_title': 'About Us',
        'breadcrumb_section': 'Services',
        'breadcrumb_section_url': breadcrumb_section_url,
        'breadcrumb_active': 'About',
        'about':'active',
        'chefs':chefs,
        'rest_detail': rest_detail,

        }
    return render(request,'restaurant/about.html',context)






def service(request):
    services = Services.objects.all()
    rest_detail = get_object_or_404(Rest_detail,pk =1)
    breadcrumb_section_url = reverse('restaurant_app:about')

    context = {
        'services': services,
        'service':'active',
        'page_title': 'Services',
        'breadcrumb_section': 'About',
        'breadcrumb_active': 'Services',
        'rest_detail': rest_detail,
        'breadcrumb_section_url': breadcrumb_section_url,


        }
    return render(request,'restaurant/services.html',context)







def menu(request, category):

    drinks = Drinks.objects.all().order_by('-price')
    meals = Meals.objects.all().order_by('-price')
    sandwiches = Sandwiches.objects.all().order_by('-price')
    grills = Grills.objects.all().order_by('-price')
    sweets = Sweets.objects.all().order_by('-price')
    salads = Salads.objects.all().order_by('-price')
    rest_detail = get_object_or_404(Rest_detail,pk =1)
    breadcrumb_section_url = reverse('restaurant_app:contact')

        # Filter menu items based on the selected category
    if category == 'Drinks':
        items = drinks
        name_page = 'Drinks'
    elif category == 'Meals':
        items = meals
        name_page = 'Meals'
    elif category == 'Sandwiches':
        items = sandwiches
        name_page = 'Sandwiches'
    elif category == 'Grills':
        items = grills
        name_page = 'Grills'
    elif category == 'Sweets':
        items = sweets
        name_page = 'Sweets'
    elif category == 'Salads':
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


    if request.method == 'POST':
        object_id = request.POST.get('object_id')
        # content_type = request.POST.get('content_type')
        size = request.POST.get('size')
        quantity = request.POST.get('quantity')
    else:
        content_type = 'Drinks'
        object_id = 5
    content_type = object_id.__class__
    # food_type = get_object_or_404(content_type,id=object_id)

    
    context = {
        'menu':'active',
        'page_title': 'Food Menu',
        'breadcrumb_section': 'Contact Us',
        'breadcrumb_active': 'Menu',
        'items': items,
        'category': category,
        'first_half': first_half,
        'second_half': second_half,
        'name_page': name_page,
        'rest_detail':rest_detail,
        'breadcrumb_section_url': breadcrumb_section_url,

        }
    return render(request,'restaurant/menu.html',context)




def testimonial(request):
    clients = Clients.objects.all()
    rest_detail = get_object_or_404(Rest_detail,pk =1)

    context = {
        'clients': clients,
        'rest_detail':rest_detail,
        }
    return render(request,'testimonial.html',context)

def our_team(request):
    chefs = Chefs.objects.all()
    rest_detail = get_object_or_404(Rest_detail,pk =1)

    context = {
        'chefs': chefs,
        'rest_detail':rest_detail,
        }
    return render(request,'team.html',context)





def contact(request):
    rest_detail = get_object_or_404(Rest_detail,pk =1)
    breadcrumb_section_url = reverse('restaurant_app:menu', kwargs={'category': 'choose_as_you_like'})

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            if name and email and subject and message:
             email_subject = f"Contact Form: {subject}"
             email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            # Send the email
            try:
                send_mail(
                    email_subject,
                    email_message,
                    'anas227sultan@gmail.com',  # Replace with your sender email
                    [email]  # Replace with recipient email
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, "Failed to send your message. Please try again later.")
        else:
            messages.error(request, "All fields are required.")


    contact_emails = get_object_or_404(Contact,pk=1)
    context={
        'contact_emails':contact_emails,
        'contact':'active',
        'page_title': 'Contact Us',
        'breadcrumb_section': 'Menu',
        'breadcrumb_active': 'Contact Us',
        'form': form,
        'rest_detail':rest_detail,
        'breadcrumb_section_url':breadcrumb_section_url,
    }
    
    return render(request, 'restaurant/contact.html', context)



def booking(request):
    pass


from django.contrib.contenttypes.models import ContentType

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')
        content_type = request.POST.get('content_type')
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))
        content_type = ContentType.objects.get(model=content_type.lower())
        food_item = content_type.get_object_for_this_type(id=object_id)
        cart, created = Cart.objects.get_or_create(user=request.user if request.user.is_authenticated else None)
        cart_item, created = CartItem.objects.get_or_create(cart=cart,
                                                            content_type=content_type,
                                                            object_id=object_id,
                                                            size=size if size else None)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()

    return redirect('restaurant_app:cart')            
            
                                        

@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user if request.user.is_authenticated else None).first()
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    name = request.user.first_name

    # Calculate the total price for all items in the cart
    total_price = 0
    for item in cart_items:
        # Check if the food item has `get_price_by_size` method
        item.has_price_by_size = hasattr(item.food_item, 'get_price_by_size') and item.size

        # Determine the item price
        if item.has_price_by_size:
            item_price = item.food_item.get_price_by_size(item.size)  # Call method inside view
        else:
            item_price = item.food_item.price

        # Assign computed price and total price for easy template usage
        item.item_price = item_price
        item.total_price = item.quantity * item_price

        # Check category and assign size display
        if isinstance(item.food_item, (Drinks, Salads)):  
            item.display_size = item.size if item.size else "N/A"  # Show size if available
        else:
            item.display_size = "Standard"  # Default for other categories

        # Update total cart price
        total_price += item.total_price
    breadcrumb_section_url = reverse('restaurant_app:menu', kwargs={'category': 'choose_as_you_like'})
    rest_detail = get_object_or_404(Rest_detail,pk =1)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
        'page_title': 'Orders',
        'breadcrumb_section': 'Menu',
        'breadcrumb_active': 'Orders',
        'breadcrumb_section_url':breadcrumb_section_url,
        'rest_detail':rest_detail,
        'name':name,
    }

    return render(request, 'restaurant/cart.html', context)


def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    quantity = int(request.POST.get('quantity', 1))

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('restaurant_app:cart')


def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('restaurant_app:cart')