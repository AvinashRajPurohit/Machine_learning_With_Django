from django.forms import ModelForm
from .models import Prediction


class PredForm(ModelForm):
    class Meta:
        model = Prediction
        fields = '__all__'
