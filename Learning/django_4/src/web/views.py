from django.shortcuts import render
from web.models import Customers, Features ,DemoRequest, Reviews, Testimonials,midFeatures, Products,Blog
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings


def index(request):
	customers = Customers.objects.all()
	features = Features.objects.all()
	reviews = Reviews.objects.all()
	testimonials = Testimonials.objects.all()
	midfeatures = midFeatures.objects.all()
	products = Products.objects.all()
	blog = Blog.objects.all()
	context = {
		"customers": Customers.objects.all(),
		"features": Features.objects.all(),
		"reviews": Reviews.objects.all(),
		"testimonials": Testimonials.objects.all(),
		"midfeatures": midFeatures.objects.all(),
		"products": Products.objects.all(),
		"blog": Blog.objects.all(),
	}
	return render(request, 'index.html', context=context)


def demo_request_api(request):
	if request.method != 'POST':
		return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

	email = request.POST.get('email', '').strip()
	if not email:
		return JsonResponse({'status': 'error', 'message': 'Email required'}, status=400)

	# Check if already registered
	if DemoRequest.objects.filter(email__iexact=email).exists():
		return JsonResponse({'status': 'exists', 'message': 'Email already registered'}, status=200)

	# Save request
	dr = DemoRequest.objects.create(email=email)

	# Send email (console backend in settings) - keep try/except to avoid crashes
	try:
		send_mail(
			subject='Demo request received',
			message=f'Thank you for requesting a demo. We received your request for {email}.',
			from_email=settings.DEFAULT_FROM_EMAIL,
			recipient_list=[email],
			fail_silently=False,
		)
	except Exception as e:
		# still return success but include warning
		return JsonResponse({'status': 'saved_email_failed', 'message': f'Request saved but email failed: {e}'}, status=200)

	return JsonResponse({'status': 'ok', 'message': 'Demo request received'}, status=200)

def product(request,pk):
	products = Products.objects.all()
	main_product = Products.objects.get(pk=pk)
	context = {
		"products": products,
		"main_product": main_product,
	}
	return render(request, 'product.html', context=context)