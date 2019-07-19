from django import forms

from .models import PostcodeList


class PostcodeListForm(forms.ModelForm):

    class Meta:
        model = PostcodeList
        fields = ('title', 'text', 'csv')
