from django import forms

class UploadFileFrom(forms.Form):
    RESOURCE_CHOICES = [
        (1, 'Resource Type'),
        (2, 'Theory'),
        (3, 'Lab'),
    ]
    email= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Department= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Course= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    texxt= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    file= forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(choices=RESOURCE_CHOICES, widget=forms.Select(attrs={'class': 'select'}))


class Facultyinfo(forms.Form):
    g_suit= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    initial= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    room_no= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    file= forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

