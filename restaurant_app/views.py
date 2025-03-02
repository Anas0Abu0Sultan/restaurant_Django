from django.shortcuts import render
from .models import AboutUs, AboutUsImage, Rest_detail,Services,Drinks,Meals,Sandwiches,Grills,Sweets,Salads,Chefs,Contact,Cart,CartItem,Comment
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
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .forms import DrinkForm, SaladForm, MealForm, SandwichForm, GrillForm, SweetForm,ChefForm,CommentForm,ContactUsForm,RestDetailForm

#                                       <<<<<<     test    >>>>>
def test(request):
    services = Services.objects.all()
    return render(request, 'restaurant/navbar_other.html',{'services':services})





#                                       <<<<<<     Home    >>>>>

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
    # clients = Clients.objects.all()
    comments = Comment.objects.filter(status='approved').order_by('-created_at')

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
        # 'clients': clients,
        'comments':comments,
        'first_half': first_half,
        'second_half': second_half,
        }
    return render(request,'restaurant/index.html',context)


#                                       <<<<<<     About    >>>>>

def about(request):
    about_us = AboutUs.objects.first()
    about_us_images = AboutUsImage.objects.filter(about_us=about_us) if about_us else None
    chefs_list = Chefs.objects.all()
    # paginator = Paginator(chefs_list,8)
    # page_number = request.GET.get('page')
    # chefs  = paginator.get_page(page_number)
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
        'chefs':chefs_list,
        'rest_detail': rest_detail,

        }
    return render(request,'restaurant/about.html',context)





#                                       <<<<<<     Service    >>>>>

def service(request):
    services = Services.objects.all()
    rest_detail = get_object_or_404(Rest_detail,pk =1)
    breadcrumb_section_url = reverse('restaurant_app:about')
    comments = Comment.objects.filter(status='approved').order_by('-created_at')


    context = {
        'services': services,
        'service':'active',
        'page_title': 'Services',
        'breadcrumb_section': 'About',
        'breadcrumb_active': 'Services',
        'rest_detail': rest_detail,
        'breadcrumb_section_url': breadcrumb_section_url,
        'comments': comments,


        }
    return render(request,'restaurant/services.html',context)






#                                       <<<<<<     Menu    >>>>>

def menu(request, category):

    drinks = Drinks.objects.all().order_by('-price')
    meals = Meals.objects.all().order_by('-price')
    sandwiches = Sandwiches.objects.all().order_by('-price')
    grills = Grills.objects.all().order_by('-price')
    sweets = Sweets.objects.all().order_by('-price')
    salads = Salads.objects.all().order_by('-price')
    rest_detail = get_object_or_404(Rest_detail,pk =1)
    breadcrumb_section_url = reverse('restaurant_app:cart')

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
        'breadcrumb_section': 'my orders',
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





def menu_new(request, category):
    drinks = Drinks.objects.all().order_by('-price')
    meals = Meals.objects.all().order_by('-price')
    sandwiches = Sandwiches.objects.all().order_by('-price')
    grills = Grills.objects.all().order_by('-price')
    sweets = Sweets.objects.all().order_by('-price')
    salads = Salads.objects.all().order_by('-price')
    rest_detail = get_object_or_404(Rest_detail, pk=1)

    context = {
        'drinks': drinks,
        'meals': meals,
        'sandwiches': sandwiches,
        'grills': grills,
        'sweets': sweets,
        'salads': salads,
        'category': category,
        'rest_detail': rest_detail,
    }
    return render(request, 'restaurant/menu_new.html', context)






#                                       <<<<<<     Testimonial    >>>>>

def testimonial(request):
    # clients = Clients.objects.all()
    rest_detail = get_object_or_404(Rest_detail,pk =1)

    context = {
        # 'clients': clients,
        'rest_detail':rest_detail,
        }
    return render(request,'testimonial.html',context)



#                                       <<<<<<     Team    >>>>>

def our_team(request):
    chefs = Chefs.objects.all()
    rest_detail = get_object_or_404(Rest_detail,pk =1)

    context = {
        'chefs': chefs,
        'rest_detail':rest_detail,
        }
    return render(request,'team.html',context)




#                                       <<<<<<     Contact    >>>>>

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


#                                       <<<<<<     Booking    >>>>>

def booking(request):
    pass


#                                       <<<<<<     Addd to Cart    >>>>>

from django.contrib.contenttypes.models import ContentType

# @login_required
# def add_to_cart(request):
#     if request.method == 'POST':
#         object_id = request.POST.get('object_id')
#         content_type = request.POST.get('content_type')
#         size = request.POST.get('size')
#         quantity = int(request.POST.get('quantity', 1))
#         content_type = ContentType.objects.get(model=content_type.lower())
#         food_item = content_type.get_object_for_this_type(id=object_id)
#         cart, created = Cart.objects.get_or_create(user=request.user if request.user.is_authenticated else None)
#         cart_item, created = CartItem.objects.get_or_create(cart=cart,
#                                                             content_type=content_type,
#                                                             object_id=object_id,
#                                                             size=size if size else None)
#         if not created:
#             cart_item.quantity += quantity
#         else:
#             cart_item.quantity = quantity

#         cart_item.save()

#     return redirect('restaurant_app:cart')            

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        object_id = request.POST.get('object_id')
        content_type = request.POST.get('content_type')
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))

        try:
            # Get the content type and food item
            content_type = ContentType.objects.get(model=content_type.lower())
            food_item = content_type.get_object_for_this_type(id=object_id)

            # Ensure food_item exists
            if food_item is None:
                print(f"Food item not found for object_id: {object_id} and content_type: {content_type}")
                return redirect('restaurant_app:menu')  # Redirect to menu or handle error

            # Get or create the cart
            cart, created = Cart.objects.get_or_create(user=request.user if request.user.is_authenticated else None)

            # Get or create the cart item
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                content_type=content_type,
                object_id=object_id,
                size=size if size else None
            )

            # Update quantity
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity

            cart_item.save()

        except ContentType.DoesNotExist:
            print(f"Invalid content_type: {content_type}")
            return redirect('restaurant_app:menu')  # Redirect to menu or handle error
        except Exception as e:
            print(f"Error adding to cart: {e}")
            return redirect('restaurant_app:menu')  # Redirect to menu or handle error

    return redirect('restaurant_app:cart')
                                        
#                                       <<<<<<     Cart    >>>>>

@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user if request.user.is_authenticated else None).first()
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    name = request.user.first_name

    # Calculate the total price for all items in the cart
    total_price = 0
    for item in cart_items:
        if item.food_item is None:
            continue
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

#                                       <<<<<<     update  Cart    >>>>>

def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    quantity = int(request.POST.get('quantity', 1))

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('restaurant_app:cart')

#                                       <<<<<<     Remove from cart    >>>>>

def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('restaurant_app:cart')




#                                       <<<<<<     Dashboard    >>>>>
@staff_member_required
def dashboard(request):
    # Combine all food items from child models
    drinks = Drinks.objects.all()
    salads = Salads.objects.all()
    meals = Meals.objects.all()
    sandwiches = Sandwiches.objects.all()
    grills = Grills.objects.all()
    sweets = Sweets.objects.all()
    chefs = Chefs.objects.all()
    pending_comments = Comment.objects.filter(status='pending')
    comments = Comment.objects.filter(status='approved')
    rejected_comments = Comment.objects.filter(status='rejected')
    contact = get_object_or_404(Contact,id=1)
    # Combine all food items into a single list
    food_items = list(drinks) + list(salads) + list(meals) + list(sandwiches) + list(grills) + list(sweets)

    # Statistics
    total_carts = Cart.objects.count()
    total_comments = Comment.objects.count()
    total_chefs = Chefs.objects.count()
    total_services = Services.objects.count()
    about_us = AboutUs.objects.first()
    restaurant_details = Rest_detail.objects.first()

    context = {
        'total_carts': total_carts,
        'total_comments': total_comments,
        'total_chefs': total_chefs,
        'total_services': total_services,
        'about_us': about_us,
        'rest_detail': restaurant_details,
        'food_items': food_items,
        'page_title': 'Admin Dashboard',
        'breadcrumb_section': 'Menu',
        'breadcrumb_active': 'Dashboard',
        'Dashboard':'active',
        'chefs':chefs,
        'pending_comments':pending_comments,
        'comments':comments,
        'rejected_comments':rejected_comments,
        'contact':contact,
    }
    return render(request, 'restaurant/dashboard.html', context)


#                                       <<<<<<     Dashboard  Drinks     >>>>>

@staff_member_required
def add_drink(request):
    form = DrinkForm()
    if request.method == 'POST':
        form = DrinkForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Drink added successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error adding the drink.")
    return render(request, 'restaurant/add_food.html', {'form': form, 'food_type': 'Drink'})

@staff_member_required
def edit_drink(request, drink_id):
    drink = get_object_or_404(Drinks, id=drink_id)
    if request.method == 'POST':
        form = DrinkForm(request.POST, request.FILES, instance=drink)
        if form.is_valid():
            form.save()
            messages.success(request, "Drink updated successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error updating the drink.")
    else:
        form = DrinkForm(instance=drink)
    return render(request, 'restaurant/edit_food.html', {'form': form, 'food_type': 'Drink'})


@staff_member_required
def delete_drink(request, drink_id):
    drink = get_object_or_404(Drinks, id=drink_id)
    drink.delete()
    messages.success(request, "Drink deleted successfully!")
    return redirect('restaurant_app:dashboard')



#                                       <<<<<<     Dashboard  Salads     >>>>>
@staff_member_required
def add_salad(request):
    form = SaladForm()
    if request.method == 'POST':
        form = SaladForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Salad added successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error adding the drink.")
    return render(request, 'restaurant/add_food.html', {'form': form, 'food_type': 'Salad'})

@staff_member_required
def edit_salad(request, salad_id):
    salad = get_object_or_404(Salads, id=salad_id)
    if request.method == 'POST':
        form = SaladForm(request.POST, request.FILES, instance=salad)
        if form.is_valid():
            form.save()
            messages.success(request, "Salad updated successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error updating the Salad.")
    else:
        form = SaladForm(instance=salad)
    return render(request, 'restaurant/edit_food.html', {'form': form, 'food_type': 'Salad'})

@staff_member_required
def delete_salad(request, salad_id):
    salad = get_object_or_404(Salads, id=salad_id)
    salad.delete()
    messages.success(request, "Salad deleted successfully!")
    return redirect('restaurant_app:dashboard')


#                                       <<<<<<     Dashboard  Meal     >>>>>
@staff_member_required
def add_meal(request):
    form = MealForm()
    if request.method == 'POST':
        form = MealForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Meal added successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error adding the Meal.")
    return render(request, 'restaurant/add_food.html', {'form': form, 'food_type': 'Meal'})

@staff_member_required
def edit_meal(request, meal_id):
    meal = get_object_or_404(Meals, id=meal_id)
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES, instance=meal)
        if form.is_valid():
            form.save()
            messages.success(request, "Meal updated successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error updating the Meal.")
    else:
        form = MealForm(instance=meal)
    return render(request, 'restaurant/edit_food.html', {'form': form, 'food_type': 'Meal'})

@staff_member_required
def delete_meal(request, meal_id):
    meal = get_object_or_404(Meals, id=meal_id)
    meal.delete()
    messages.success(request, "Meal deleted successfully!")
    return redirect('restaurant_app:dashboard')



#                                       <<<<<<     Dashboard  Sandwich     >>>>>
@staff_member_required
def add_sandwich(request):
    form = SandwichForm()
    if request.method == 'POST':
        form = SandwichForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Sandwich added successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error adding the sandwich.")
    return render(request, 'restaurant/add_food.html', {'form': form, 'food_type': 'Sandwich'})

@staff_member_required
def edit_sandwich(request, sandwich_id):
    sandwich = get_object_or_404(Sandwiches, id=sandwich_id)
    if request.method == 'POST':
        form = SandwichForm(request.POST, request.FILES, instance=sandwich)
        if form.is_valid():
            form.save()
            messages.success(request, "Sandwich updated successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error updating the sandwich.")
    else:
        form = SandwichForm(instance=sandwich)
    return render(request, 'restaurant/edit_food.html', {'form': form, 'food_type': 'Sandwich'})


@staff_member_required
def delete_sandwich(request, sandwich_id):
    sandwich = get_object_or_404(Sandwiches, id=sandwich_id)
    sandwich.delete()
    messages.success(request, "Sandwich deleted successfully!")
    return redirect('restaurant_app:dashboard')



#                                       <<<<<<     Dashboard  Grill     >>>>>
@staff_member_required
def add_grill(request):
    form = GrillForm()
    if request.method == 'POST':
        form = GrillForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Grill added successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error adding the Grill.")
    return render(request, 'restaurant/add_food.html', {'form': form, 'food_type': 'Grill'})


@staff_member_required
def edit_grill(request, grill_id):
    grill = get_object_or_404(Grills, id=grill_id)
    if request.method == 'POST':
        form = GrillForm(request.POST, request.FILES, instance=grill)
        if form.is_valid():
            form.save()
            messages.success(request, "Grill updated successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error updating the grill.")
    else:
        form = GrillForm(instance=grill)
    return render(request, 'restaurant/edit_food.html', {'form': form, 'food_type': 'Grill'})

@staff_member_required
def delete_grill(request, grill_id):
    grill = get_object_or_404(Grills, id=grill_id)
    grill.delete()
    messages.success(request, "Grill deleted successfully!")
    return redirect('restaurant_app:dashboard')




#                                       <<<<<<     Dashboard  Sweet     >>>>>

@staff_member_required
def add_sweet(request):
    form = SweetForm()
    if request.method == 'POST':
        form = SweetForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Sweet added successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error adding the sweet.")
    return render(request, 'restaurant/add_food.html', {'form': form, 'food_type': 'Sweet'})

@staff_member_required
def edit_sweet(request, sweet_id):
    sweet = get_object_or_404(Sweets, id=sweet_id)
    if request.method == 'POST':
        form = SweetForm(request.POST, request.FILES, instance=sweet)
        if form.is_valid():
            form.save()
            messages.success(request, "Sweet updated successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error updating the sweet.")
    else:
        form = SweetForm(instance=sweet)
    return render(request, 'restaurant/edit_food.html', {'form': form, 'food_type': 'Sweet'})

@staff_member_required
def delete_sweet(request, sweet_id):
    sweet = get_object_or_404(Sweets, id=sweet_id)
    sweet.delete()
    messages.success(request, "Sweet deleted successfully!")
    return redirect('restaurant_app:dashboard')



#                                       <<<<<<     Dashboard  Chefs     >>>>>

@staff_member_required
def add_chef(request):
    form = ChefForm()
    if request.method == 'POST':
        form = ChefForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Chef added successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error adding the chef.")
    return render(request, 'restaurant/chef/add_chef.html', {'form': form})

@staff_member_required
def edit_chef(request,chef_id):
    chef = get_object_or_404(Chefs, id=chef_id)
    if request.method == 'POST':
        form = ChefForm(request.POST, request.FILES, instance=chef)
        if form.is_valid():
            form.save()
            messages.success(request, "Chef updated successfully!")
            return redirect('restaurant_app:dashboard')
        else:
            messages.error(request, "There was an error updating the chef.")
    form = ChefForm(instance=chef)
    return render(request, 'restaurant/chef/edit_chef.html', {'form': form})

@staff_member_required
def delete_chef(request,chef_id):
    chef = get_object_or_404(Chefs, id=chef_id)
    chef.delete()
    messages.success(request, "Chef deleted successfully!")
    return redirect('restaurant_app:dashboard')

#                                       <<<<<<     Dashboard  Comment     >>>>>


@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)  
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.status = 'pending'  # Set status to pending
            comment.save()
            messages.success(request, 'Your comment has been submitted we will publish it soon.')
            return redirect('restaurant_app:home')
        else:
            messages.error(request, "There was an error submitting your comment.")
    else:
        form = CommentForm()
    return render(request, 'restaurant/comment/add_comment.html', {'form': form})
       

@staff_member_required
def delete_comment(request,comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, "Comment deleted successfully!")
    return redirect('restaurant_app:dashboard')

@staff_member_required
def update_comment_status(request, comment_id, status):
    # Get the comment or return 404 if not found
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Update the status
    comment.status = status
    comment.save()
    
    # Notify the admin
    messages.success(request, f'Comment status updated to {status}.')
    return redirect('restaurant_app:dashboard')  # Redirect to the manage comments page


@staff_member_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contat Us information updated successfully!.')
            return redirect('restaurant_app:dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, "Error in updateing the contact us.")
    else:
        form = ContactUsForm(instance=contact)
    return render(request, 'restaurant/edit_contact.html', {'form': form})


@staff_member_required
def edit_rest_detail(request):
    # Fetch the first Rest_detail object
    rest_detail = Rest_detail.objects.first()
    
    if not rest_detail:
        # If no Rest_detail object exists, create one with default values
        rest_detail = Rest_detail.objects.create()

    if request.method == 'POST':
        # Bind the form to the POST data and the existing instance
        form = RestDetailForm(request.POST, request.FILES, instance=rest_detail)
        if form.is_valid():
            form.save()  # Save the updated Rest_detail
            return redirect('restaurant_app:dashboard')  # Redirect to the dashboard or another page
    else:
        # Display the form with the existing Rest_detail data
        form = RestDetailForm(instance=rest_detail)
    
    return render(request, 'restaurant/edit_rest_detail.html', {'form': form})