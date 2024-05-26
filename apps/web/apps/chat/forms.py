from django import forms


class JoinForm(forms.Form):
    name = forms.CharField(label='', max_length=225, min_length=4, widget=forms.TextInput(attrs={
        'class': 'border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full',
        'placeholder': 'Room name'
    }))

    def clean_name(self, *args, **kwargs):
        name_form = self.cleaned_data.get('name')
        return name_form
