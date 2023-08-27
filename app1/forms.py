from django import forms
from app1.models import Course

#Create Forms Here

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {'cname':'Course:','dur':'Duration:','fee':'Fees:','trainer':'Instructor:'}
        widgets = {
            'cname':forms.TextInput(attrs={'class':'form-control'}),
            'dur':forms.NumberInput(attrs={'class':'form-control'}),
            'fee':forms.NumberInput(attrs={'class':'form-control'}),
            'trainer':forms.TextInput(attrs={'class':'form-control'}),
        }


