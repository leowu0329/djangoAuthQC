from django.contrib import admin
from .models import DefectList, OperatorList, OrderList, SpecList, IPQCList

# Register your models here.

@admin.register(DefectList)
class DefectListAdmin(admin.ModelAdmin):
    list_display = ('id', 'defect_type')
    search_fields = ('defect_type',)

@admin.register(OperatorList)
class OperatorListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
    search_fields = ('name', 'department')

@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'date', 'product_number', 'product_name', 'quantity')
    list_filter = ('date',)
    search_fields = ('order_number', 'product_number', 'product_name')

@admin.register(SpecList)
class SpecListAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'product_name', 'spec', 'draw_ver', 'inspection_hours')
    search_fields = ('product_number', 'product_name')

@admin.register(IPQCList)
class IPQCListAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'order_number', 'product_number', 'inspector', 'defect_status')
    list_filter = ('date', 'defect_status', 'inspector')
    search_fields = ('order_number', 'product_number', 'inspector', 'product_name')
