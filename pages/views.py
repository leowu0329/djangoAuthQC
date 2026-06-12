from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import DefectList, OperatorList, OrderList, SpecList, IPQCList

@login_required  # 這個裝飾器會自動檢查登入狀態
def home_page(request):
    return render(request, 'home.html')  # 假設你的首頁模板是 home.html

@login_required
def ipqc_list_view(request):
    items = IPQCList.objects.all().order_by('-date', '-time')
    return render(request, 'app/ipqc/ipqc_list.html', {'items': items})

@login_required
def defect_list_view(request):
    items = DefectList.objects.all()
    return render(request, 'app/ipqc/defect_list.html', {'items': items})

@login_required
def operator_list_view(request):
    items = OperatorList.objects.all()
    return render(request, 'app/ipqc/operator_list.html', {'items': items})

@login_required
def order_list_view(request):
    items = OrderList.objects.all().order_by('-date')
    return render(request, 'app/ipqc/order_list.html', {'items': items})

@login_required
def spec_list_view(request):
    items = SpecList.objects.all()
    return render(request, 'app/ipqc/spec_list.html', {'items': items})
