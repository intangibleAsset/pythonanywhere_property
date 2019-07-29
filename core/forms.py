from django import forms
import logging
from . models import Item, ItemImage

logger = logging.getLogger(__name__)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'description',
            'oic',
            'exhibitRef',
            'seizedDate',
            'seizedTime',
            'seizedLocation',
            'notes',
        ]

class AddImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = [
            'image',
        ]



