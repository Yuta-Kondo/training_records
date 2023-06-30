from django import forms
from .models import Training
from django.utils import timezone


class RecordTraining(forms.ModelForm):
    training_date = forms.DateTimeField(
        initial=timezone.now,
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    )

    class Meta:
        model = Training
        fields = [
            'activity',
            'training_date',
        ]
