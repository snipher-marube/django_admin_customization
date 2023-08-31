from django import forms
from django.forms import ModelForm, RadioSelect


from tickets.models import Ticket

class TicketAdminForm(ModelForm):
    first_name = forms.CharField(label='first_name', max_length=255)
    last_name = forms.CharField(label='last_name', max_length=255)

    class Meta:
        model = Ticket
        fields = [
            'concert',
            'first_name',
            'last_name',
            'payment_method',
            'is_active'
        ]
        widgets = {
            'payment_method': RadioSelect()
        }

        def __init__(self, *args, **kwargs):
            instance = kwargs.get('instance')
            initial = {}
            if instance:
                customer_full_name_split = instance.customer_full_name.split(" ", maxsplit=1)
                initial = {
                    "first_name": customer_full_name_split[0],
                    "last_name": customer_full_name_split[1],
                }
            super().__init__(*args, **kwargs, initial=initial)

        
        def save(self, commit=True):
            self.instance.customer_full_name = self.cleaned_data["first_name"] + " " \
                                            + self.cleaned_data["last_name"]
            return super().save(commit)
        
        
            
