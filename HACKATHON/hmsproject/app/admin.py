from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User,Appointment,Patient,Payment,Department

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'name', 'user_type', 'city', 'date_joined', 'status']

@admin.register(Appointment)
class UserAdmin(admin.ModelAdmin):
    list_display = ['appointment_ref', 'appointment_id', 'doctor', 'date']

@admin.register(Patient)
class UserAdmin(admin.ModelAdmin):
    list_display = ['patient_ref', 'patient_id', 'problem', 'medicine']

@admin.register(Payment)
class UserAdmin(admin.ModelAdmin):
    list_display = ['payment_ref','order_id', 'payment_id', 'amount', 'date','status']

@admin.register(Department)
class UserAdmin(admin.ModelAdmin):
    list_display = ['dept_ref', 'dept_id', 'position']