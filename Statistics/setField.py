from django import forms


class setField(forms.CharField):
    # max length

    def to_python(self, value):
        if not value:
            return None
        return value
    def validate(self, value):
        if value is '0':
            raise forms.ValidationError("Set is required.")