from django import forms
from building_name_generator.models import District, HashedLocation, Municipality


class GenerateHashForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.none())
    municipality = forms.ModelChoiceField(queryset=Municipality.objects.none())

    class Meta:
        model = HashedLocation
        fields = [
            'province',
            'district',
            'municipality',
            'wardnumber',
            'road',
            'chowk',
        ]
