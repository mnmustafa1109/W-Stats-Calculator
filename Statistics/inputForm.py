from django import forms
from django.forms import CharField
import re

class KendallWValueForms(forms.Form):
    set_1 = CharField(label='Set 1', max_length=100, help_text="Input should be comma separated as 1,2,3", required=True)
    set_2 = CharField(label='Set 2', max_length=100, help_text="Input should be comma separated as 1,2,3", required=True)

    def clean_set_1(self):
        # raise an exception if the values are not csv
        value = self.cleaned_data.get('set_1')

        pattern = re.compile(r"^[0-9\,]*$")
        if bool(pattern.search(value)) is False:
            raise forms.ValidationError("Values in Set 1 must be comma-separated.")

        #delete repeated commas
        value = re.sub(r',+', ',', value)
        print(value)

        return value

    def clean_set_2(self):
        value = self.cleaned_data.get('set_2')

        pattern = re.compile(r"^[0-9\,]*$")
        if bool(pattern.search(value)) is False:
            raise forms.ValidationError("Values in Set 2 must be comma-separated.")

        # delete repeated commas
        value = re.sub(r',+', ',', value)
        print(value)
        return value



