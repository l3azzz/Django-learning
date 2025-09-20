from django.contrib import admin
from web.models import Testimonials, Promoters , Faq, Subscribe


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id","name","description","designation", "image"]

class PromotersAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]

class FaqAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "faq_type","description"]


admin.site.register(Testimonials, TestimonialAdmin)
admin.site.register(Promoters, PromotersAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Subscribe)