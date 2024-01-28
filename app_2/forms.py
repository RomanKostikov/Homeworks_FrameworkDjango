from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Описание продукта"}))
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    count = forms.IntegerField()
    image_product = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": "Изображение продукта"}))
