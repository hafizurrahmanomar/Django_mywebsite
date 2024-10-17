from django.forms import ModelForm

from . models import MobilePhone


class CreateUpdateMobile(ModelForm):
    class Meta:
        model = MobilePhone
        fields = '__all__'
