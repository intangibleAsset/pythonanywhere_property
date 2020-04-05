from django import forms
import logging
from . models import Item, ItemImage

logger = logging.getLogger(__name__)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'description',
            'seizedBy',
            'exhibitRef',
            'seizedDate',
            'seizedTime',
            'seizedLocation',
        ]

class AddImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = [
            'image',
        ]



