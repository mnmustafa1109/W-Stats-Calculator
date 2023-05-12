from django import forms
from .setField import setField
from django.forms import CharField
import re

class KendallWValueForms(forms.Form):
    set_1 = CharField(label='Set 1', max_length=100, help_text="1,2,3", required=True)
    set_2 = CharField(label='Set 2', max_length=100, help_text="3,4,5", required=True)

    def clean_set_1(self):
        # raise an exception if the values are not csv
        value = self.cleaned_data.get('set_1')

        pattern = re.compile(r"^[0-9\,]*$")
        if bool(pattern.search(value)) is False:
            raise forms.ValidationError("Values in Set 1 must be comma-separated.")

        #delete repeated commas
        value = re.sub(r',+', ',', value)
        print(value)

        # print(pattern.findall("z")
        # print(pattern.findall("1,2,3,4"))

        # Check if the value is empty
        # if not value:
        #     raise forms.ValidationError("Set 1 is required.")
        #
        # # Split the value by commas
        # values = value.split(',')
        #
        # # Check if all values are non-empty
        # if not all(values):
        #     raise forms.ValidationError("Values in Set 1 must be comma-separated.")

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



