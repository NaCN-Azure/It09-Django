from django import forms
from application.models import Job, User

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        
    def clean(self):
        cleaned_data = super().clean()
        city = cleaned_data.get('city')
        employer_id = self.initial.get('employer_id')

        if not city and employer_id:
            employer = User.objects.get(pk=employer_id)
            cleaned_data['city'] = employer.city
        return cleaned_data