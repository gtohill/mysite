from django import forms


class RegistrationForm(forms.Form):
    LOC = (
        ("SEL", "Select Location"),
        ("LDN", "London"),
        ("MGA", "Mississauga"),
        ("WRO", "Waterloo"),
    )

    STAT = (
        ("SEL", "Select Status"),
        ("FR", "Free Evaluation"),
        ("RS", "Returning Student"),
    )

    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    name = forms.CharField(label='First Name', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    location = forms.ChoiceField(widget=forms.Select, choices=LOC)
    status = forms.ChoiceField(widget=forms.Select, choices=STAT)
    age = forms.CharField(label='Age', max_length=2)
    questions = forms.CharField(widget=forms.Textarea, label='Questions/Comments', max_length=300)


class OrientationForm(forms.Form):
    confirm = forms.BooleanField(required=False)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField()
    questions = forms.CharField(widget=forms.Textarea, label='Questions', max_length=300)
