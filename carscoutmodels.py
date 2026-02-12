# from django.db import models
# from django.contrib.auth.models import User

# # 1. User Profile for extra details
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=[('Buyer', 'Buyer'), ('Seller', 'Seller')]) 
#     phone = models.CharField(max_length=15)

# # 2. Car Listings 
# class Vehicle(models.Model):
#     seller = models.ForeignKey(User, on_delete=models.CASCADE) 
#     make = models.CharField(max_length=50) 
#     model = models.CharField(max_length=50) 
#     year = models.PositiveIntegerField() 
#     price = models.DecimalField(max_digits=12, decimal_places=2) 
#     mileage = models.PositiveIntegerField() 
#     description = models.TextField() 
#     is_available = models.BooleanField(default=True) 
#     created_at = models.DateTimeField(auto_now_add=True)

# # 3. Car Photos (Multiple photos per car) 
# class VehiclePhoto(models.Model):
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='photos')
#     image = models.ImageField(upload_to='cars/')
#     is_360_view = models.BooleanField(default=False) 

# # 4. Virtual Inspection & AI Diagnostics 
# class InspectionReport(models.Model):
#     vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
#     ai_summary = models.TextField() 
#     accident_history = models.TextField() 
#     maintenance_records = models.TextField() 
#     is_certified = models.BooleanField(default=False) 

# # 5. Financing Options 
# class FinancingOption(models.Model):
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     bank_name = models.CharField(max_length=100)
#     interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
#     tenure_months = models.IntegerField()

# # 6. In-App Messaging 
# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_msgs')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_msgs')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

# # 7. Negotiation & Offers 
# class Negotiation(models.Model):
#     buyer = models.ForeignKey(User, on_delete=models.CASCADE)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     offered_price = models.DecimalField(max_digits=12, decimal_places=2)
#     status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')]) 

# # 8. Test Drive Scheduling 
# class TestDrive(models.Model):
#     buyer = models.ForeignKey(User, on_delete=models.CASCADE)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     date_time = models.DateTimeField() 
#     status = models.CharField(max_length=20, default='Scheduled') 

# # 9. Wishlist / Price Alerts 
# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     alert_on_price_drop = models.BooleanField(default=True) 

# # 10. Transactions & Paperwork 
# class Transaction(models.Model):
#     vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
#     buyer = models.ForeignKey(User, on_delete=models.CASCADE)
#     final_amount = models.DecimalField(max_digits=12, decimal_places=2)
#     payment_status = models.BooleanField(default=False) 
#     paperwork_completed = models.BooleanField(default=False) 