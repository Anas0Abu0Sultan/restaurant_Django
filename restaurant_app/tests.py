from django.test import TestCase

# Create your tests here. just for start
def cart_view(request):
	
	if request.method == "POST":
		item_id = request.POST.get("item_id")
		toppings = request.POST.getlist("topping_id")
		extras = request.POST.getlist("extra_id")
		size = request.POST.get("size_id")
		user = request.user

		p = Item_List.objects.get(pk=item_id)
		price_id = p.base_price_id.id

		# Calculate Price:

		# Calculate topping quantity
		count_topping = 0
		for topping in toppings: 
			count_topping+=1
		# Calculate extra quantity
		count_extra = 0
		for extra in extras: 
			count_extra+=1


		topping_price = Price_List.objects.get(name="Topping")
		extra_price = Price_List.objects.get(name="Extra")
		item = Price_List.objects.get(pk=price_id)


		# if large option selected
		if size and int(size) == 7:
			total_price = item.base_price + item.large_supp + count_topping*topping_price.large_supp + count_extra*extra_price.base_price
		else:
			total_price = item.base_price + count_topping*topping_price.base_price + count_extra*extra_price.base_price

		# Add new item to cart
		if size == None:
			new_item = Cart_List(user_id=user, item_id=Item_List.objects.get(pk = item_id), size=None, calculated_price=total_price)
		else:
			new_item = Cart_List(user_id=user, item_id=Item_List.objects.get(pk = item_id), size=Size.objects.get(pk = size), calculated_price=total_price)

		# add item to cart
		new_item.save()

		# add toppping and extras to item
		for topping in toppings: 
			new_item.toppings.add(topping)
		for extra in extras: 
			new_item.extra.add(extra)
		# return HttpResponseRedirect(reverse("cart"))
		messages.success(request, "Meal added to cart!")
		return HttpResponseRedirect(reverse("index"))
		# return render(request, "orders/index.html", {"message": "Meal added to cart!"})

	else:
		try:
			cart = Cart_List.objects.filter(user_id=request.user, is_current=True)
		except Cart_List.DoesNotExist:
			raise Http404("Cart does not exist")
		
		total_price = cart.aggregate(Sum('calculated_price'))['calculated_price__sum']

		cart_ordered = Cart_List.objects.filter(user_id=request.user, is_current=False)

		context = {
		"cart_items" : cart,
		"total_price": total_price,
		"cart_items_ordered" : cart_ordered,
		}

		return render(request, "orders/cart.html", context)

def topping_view(request, cart_id):
	# view topping from cart

	try:
		pizza = Cart_List.objects.get(pk=cart_id)
	except Cart.DoesNotExist:
		raise Http404("Pizza not in Cart or does not include topping")
	context = {
		"toppings" : pizza.toppings.all()
		}
	return render(request, "orders/topping.html", context)






































from django.shortcuts import render,redirect,HttpResponse
from app1.models import Category,Product,CartItem
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
import stripe
from app1.payments import PaymentService
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY



def payment_success(request):
    return render(request, 'success.html')


def process_payment(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)

    if request.method == 'POST':
        # Retrieve the payment token from the request
        token = request.POST.get('stripeToken')

        try:
            # Create a charge using Stripe
            charge = stripe.Charge.create(
                amount=int(total * 100),  # Stripe requires the amount in cents
                currency='usd',
                description='Payment for products',
                source=token,
            )

            # If the charge is successful, complete the order and do necessary processing
            if charge.status == 'succeeded':
                # Clear the cart items or mark them as purchased

                # Redirect to a success page or display a success message
                return redirect('payment_success')

        except stripe.error.CardError as e:
            # Handle card errors and display an error message to the user
            error = e.user_message

    # Render the payment form with the total amount
    context = {
        'total': total
    }
    return render(request, 'payment.html', context)