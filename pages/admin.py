from django.contrib import admin,messages
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
    list_display = ('date', 'time', 'order_number', 'product_number', 'inspector', 'determination', 'defect_status')
    list_filter = ('date', 'determination', 'defect_status', 'inspector')
    search_fields = ('order_number', 'product_number', 'inspector', 'product_name')
    # 註冊自訂的 Actions
    actions = ['delete_all_ipqc']

    def delete_all_ipqc(self, request, queryset):
        """
        自訂動作：刪除資料庫中所有的 IPQC 資料
        """
        # 注意：此處直接對整個 Model 的全體資料進行刪除，忽略前端勾選的項目
        total_deleted, _ = IPQCList.objects.all().delete()
        
        # 發送成功訊息給前端...
        self.message_user(
            request, 
            f"成功刪除了全部共 {total_deleted} 筆 IPQC 資料。", 
            messages.SUCCESS
        )
    
    # 設定在下拉選單中顯示的文字
    delete_all_ipqc.short_description = "❌ 刪除所有 IPQC 資料 (慎用)"
