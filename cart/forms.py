from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=99)
    # HiddenInput чтоб пользователь не видел его в форме
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)
