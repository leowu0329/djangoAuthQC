from django.db import models

class BaseModel(models.Model):
    """基礎模型，提取所有表共通欄位"""
    created_at = models.DateTimeField(verbose_name="建立時間", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新時間", auto_now=True)
    
    class Meta:
        abstract = True


class DefectList(models.Model):
    defect_type = models.CharField(verbose_name = '不良分類',blank=True, null=True)

    class Meta:
        verbose_name = "不良分類"
        verbose_name_plural = "不良分類"

    def __str__(self):
        return self.defect_type

class OperatorList(models.Model):
    name = models.CharField(verbose_name="姓名",blank=True, null=True)
    department = models.CharField(verbose_name="部門",blank=True, null=True)

    class Meta:
        verbose_name = "作業人員"
        verbose_name_plural = "作業人員"

    def __str__(self):
        return self.name
    
class OrderList(models.Model):
    order_number = models.CharField(verbose_name="製令工單",blank=True, null=True)
    date = models.DateField(verbose_name="日期",blank=True, null=True) 
    product_number = models.CharField(verbose_name="品號",blank=True, null=True)
    product_name = models.CharField(verbose_name="品名",blank=True, null=True)
    quantity = models.IntegerField(verbose_name="數量",blank=True, null=True)

    class Meta:
        verbose_name = "製令工單"
        verbose_name_plural = "製令工單"

    def __str__(self):
        return self.order_number
    
class SpecList(models.Model):
    product_number = models.CharField(verbose_name="品號",blank=True, null=True)
    product_name = models.CharField(verbose_name="品名",blank=True, null=True)
    spec= models.CharField(verbose_name="規格",blank=True, null=True)
    draw_ver= models.CharField(verbose_name="版次",blank=True, null=True)
    inspection_hours = models.DecimalField(
        verbose_name="檢驗時數", 
        max_digits=5,           # 關鍵：代表此數字總共可以有幾位數（含小數點前後，5位數如: 999.99）
        decimal_places=2,       # 關鍵：固定保留小數點後 2 位
        default=0.00,           # 關鍵：設定預設值為 0.00
        blank=True, 
        null=True
    )
    
    class Meta:
        verbose_name = "規格"
        verbose_name_plural = "規格"

    def __str__(self):
        return self.product_number

class IPQCList(models.Model):
    # 定義判定的枚舉選項
    DETERMINATION_CHOICES = [
        ('允收', '允收'),
        ('異常', '異常'),
    ]
    date= models.DateField(verbose_name="日期",blank=True, null=True)
    time= models.TimeField(verbose_name="時間",blank=True, null=True)
    order_number = models.CharField(verbose_name="製令工單",blank=True, null=True)
    operator= models.CharField(verbose_name="操作人員",blank=True, null=True)
    draw_ver= models.CharField(verbose_name="版本",blank=True, null=True)
    product_number= models.CharField(verbose_name="品號",blank=True, null=True)
    product_name= models.CharField(verbose_name="品名",blank=True, null=True)
    spec= models.CharField(verbose_name="規格",blank=True, null=True)
    quantity= models.IntegerField(verbose_name="數量",blank=True, null=True)
    inspector= models.CharField(verbose_name="檢驗人員",blank=True, null=True)
    determination = models.CharField(
        verbose_name="判定",
        max_length=10,
        choices=DETERMINATION_CHOICES,
        blank=True,
        null=True
    )
    defect_type= models.CharField(verbose_name="不良類型",blank=True, null=True)
    defect_status= models.TextField(verbose_name="不良狀態",blank=True, null=True)
    handing_measure= models.TextField(verbose_name="後續處置",blank=True, null=True)
    mark= models.TextField(verbose_name="備註",blank=True, null=True)
    
    class Meta:
        verbose_name = "IPQC"
        verbose_name_plural = "IPQC"

    def __str__(self):
        return self.order_number
