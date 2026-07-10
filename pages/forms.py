from django import forms
from .models import IPQCList

class IPQCForm(forms.ModelForm):
    class Meta:
        model = IPQCList
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'order_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入工單號碼'}),
            'operator': forms.TextInput(attrs={'class': 'form-control'}),
            'draw_ver': forms.TextInput(attrs={'class': 'form-control'}),
            'product_number': forms.TextInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'spec': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'inspector': forms.TextInput(attrs={'class': 'form-control'}),
            'determination': forms.Select(attrs={'class': 'form-control'}),
            'defect_type': forms.TextInput(attrs={'class': 'form-control'}),
            'defect_status': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'handing_measure': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mark': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }