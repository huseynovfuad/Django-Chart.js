from django import forms
from .models import Poll

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = [
            'question',
            'option1',
            'option2',
            'option3',
        ]
    def __init__(self,*args,**kwargs):
        super(PollForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['question'].widget.attrs.update({'rows':'3','placeholder': 'TYPE YOUR QUESTION HERE'})
        self.fields['option1'].widget.attrs.update({'placeholder': 'First Option'})
        self.fields['option2'].widget.attrs.update({'placeholder': 'Second Option'})
        self.fields['option3'].widget.attrs.update({'placeholder': 'Third Option'})