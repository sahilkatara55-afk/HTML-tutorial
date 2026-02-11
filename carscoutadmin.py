from django.contrib import admin
from .models import *

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price', 'is_available')
    search_fields = ('make', 'model')

@admin.register(InspectionReport)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'is_certified')

@admin.register(Negotiation)
class NegotiationAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'vehicle', 'offered_price', 'status')
    list_editable = ('status',)

# Baki na badha models ne pan simple register kari shakay
admin.site.register(UserProfile)
admin.site.register(VehiclePhoto)
admin.site.register(FinancingOption)
admin.site.register(Message)
admin.site.register(TestDrive)
admin.site.register(Favorite)
admin.site.register(Transaction)