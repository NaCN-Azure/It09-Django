from django import forms
from application.models import Job, User

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        
    def clean_city(self):
        city = self.cleaned_data.get('city')
        employer_id = self.cleaned_data.get('employer_id')
        print(f"Original city: {city}, Employer ID: {employer_id}")

        if not city and employer_id:
            try:
                employer = User.objects.get(pk=employer_id)
                print(f"Employer's city: {employer.city}")
                return employer.city  # 返回 employer 的 city 作为默认值
            except User.DoesNotExist:
                raise forms.ValidationError("Employer not found.")
        return city
    
    def clean(self):
        cleaned_data = super().clean()
        # 处理其他字段的清理逻辑...
        return cleaned_data