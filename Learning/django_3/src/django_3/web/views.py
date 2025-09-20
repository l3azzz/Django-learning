from django.shortcuts import render, redirect
from web.models import Testimonials,  Promoters, Faq, Subscribe
from django.http.response import HttpResponse
from django.urls import reverse
import json

# Create your views here.
def index(request):
    rent_tracking_faqs = Faq.objects.filter(faq_type="rent_tracking")
    new_deposit_faqs = Faq.objects.filter(faq_type="new_deposit")
    existing_deposit_faqs = Faq.objects.filter(faq_type="existing_deposit")
    promoters = Promoters.objects.all()
    testimonials = Testimonials.objects.all()
    context = {
        "promoter": promoters,
        "testimonial" : testimonials,
        "rent_tracking_faqs" : rent_tracking_faqs,
        "new_deposit_faqs" :   new_deposit_faqs,
        "existing_deposit_faqs" :  existing_deposit_faqs
    }
    print(context)
    return render(request, "index.html", context=context)


def subscribe(request):
    email = request.POST.get("email")
    Subscribe.objects.create(
        email = email
    )
    response_data = {
        "status": "succes",
        "message" : "U R Verifed IDIOT"
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
