from django.forms import ModelForm
from .models import Product

class RoomForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    