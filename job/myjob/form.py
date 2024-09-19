from django import forms
from . models import Apply,Job,Comment
from django.utils.translation import gettext_lazy as _




class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = [ 'body']





class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('title_ar', 'location_ar','description_ar')
        fields += ('title_en', 'location_en', 'description_en')
        fields += ('job_type', 'category', 'vacancy', 'salary', 'experience', 'image')         
        exclude = ('slug', 'available', 'owner')

        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        head = _('test')
        engCon=_('English Content')
        othDat=_('Other Data')
        separator_html = f'<h3 style="text-align: center;">{head}</h3>'
        separator1_html =f"<h3 style='text-align: center;'> {engCon}</h3>\n "
        separator2_html =f"<h3 style='text-align: center;'> {othDat}</h3>\n "
        
        self.fields['description_ar'].help_text += separator1_html
        self.fields['description_en'].help_text += separator2_html




class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('email', 'website', 'cv', 'cover_letter')
        labels = {
            'email': '',
            'website': '',
            'cv': '',
            'cover_letter': '',
        }

