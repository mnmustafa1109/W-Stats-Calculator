from django import forms

class KendallWValueForms(forms.Form):
    set_1 = forms.CharField(label='Set 1', max_length=100, help_text="1,2,3", required=True)
    set_2 = forms.CharField(label='Set 2', max_length=100, help_text="3,4,5", required=True)

    def clean_set_1(self):
        # raise an exception if the values are not csv
        value = self.cleaned_data.get('set_1')

        # Check if the value is empty
        if not value:
            raise forms.ValidationError("Set 1 is required.")

        # Split the value by commas
        values = value.split(',')

        # Check if all values are non-empty
        if not all(values):
            raise forms.ValidationError("Values in Set 1 must be comma-separated.")

        return value

    def clean_set_2(self):
        # raise an exception if the values are not csv
        value = self.cleaned_data.get('set_2')

        # Check if the value is empty
        if not value:
            raise forms.ValidationError("Set 2 is required.")

        # Split the value by commas
        values = value.split(',')

        # Check if all values are non-empty
        if not all(values):
            raise forms.ValidationError("Values in Set 2 must be comma-separated.")

        return value



