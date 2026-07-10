from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
	path('', views.home_page, name='home'),
	path('ipqc/', views.ipqc_list_view, name='ipqc_list'),
	path('ipqc/create/', views.ipqc_create_view, name='ipqc_create'),
	path('ipqc/edit/<int:pk>/', views.ipqc_edit_view, name='ipqc_edit'),
    path('ipqc/delete/<int:pk>/', views.ipqc_delete_view, name='ipqc_delete'),
    path('ipqc/analyze/', views.ipqc_analyze_view, name='ipqc_analyze'),
    path('ipqc/export/', views.export_ipqc_excel, name='export_ipqc_excel'),
    path('ipqc/import/', views.import_ipqc_excel, name='import_ipqc_excel'),
	path('ipqc/defects/', views.defect_list_view, name='defect_list'),
	path('ipqc/operators/', views.operator_list_view, name='operator_list'),
	path('ipqc/orders/', views.order_list_view, name='order_list'),
	path('ipqc/specs/', views.spec_list_view, name='spec_list'),
	# 重定向 /home/ 到根路徑，避免 404 錯誤
	path('home/', RedirectView.as_view(url='/', permanent=False), name='home_redirect'),
	# 重定向 /cases/ 到根路徑（可能是瀏覽器緩存或歷史記錄）
	path('cases/', RedirectView.as_view(url='/', permanent=False), name='cases_redirect'),
]