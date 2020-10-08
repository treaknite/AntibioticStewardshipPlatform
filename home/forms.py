from django import forms
from .models import Record

class UploadrecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class ApprovalForm(forms.Form):
	antibiotic=forms.ChoiceField(choices=[('piperacillin', 'piperacillin'),('aminoglycoside', 'aminoglycoside'),('ampicillin', 'ampicillin'),('linezolid', 'linezolid'),('carbapenem', 'carbapenem'),('metronidazole', 'metronidazole'),('fluoroquinolone', 'fluoroquinolone'),('clindamycin', 'clindamycin'),('Cindamycine', 'Cindamycine'),('Clarithromycin', 'Clarithromycin'),('Colistine', 'Colistine'),('Deptomycin', 'Deptomycin'),('Doxycylin', 'Doxycylin'),('Erythromycin', 'Erythromycin'),('Gentamicin', 'Gentamicin'),('Gentamycine', 'Gentamycine'),('Manurol', 'Manurol'),('Monobactums', 'Monobactums'),('Ninocycline', 'Ninocycline'),('Polymyxin', 'Polymyxin'),('Streptamycine', 'Streptamycine'),('Streptomycin', 'Streptomycin'),('linezolid', 'linezolid'),('Azithromycine', 'Azithromycine')])
	age=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Number of age'}))
	#location=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Last Credit Rating'}))
	location=forms.ChoiceField(choices=[('Delhi','Delhi'),('Guna','Guna'),('Jaipur','Jaipur'),('Jaisalmer','Jaisalmer'),('Pune','Pune'),('Kharagour','Kharagour'),('Kanchipuram','Kanchipuram'),('Chennai','Chennai'),('Bhopal','Bhopal'),('kanpur','kanpur')])
	gender=forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')])
	pregnancy=forms.ChoiceField(choices=[('Not Pregnant', 'Not Pregnant'),('Pregnant', 'Pregnant'),('Not Applicable','Not Applicable')])
	immunestatus=forms.ChoiceField(choices=[('weak', 'weak'),('good', 'good')])
	infection=forms.ChoiceField(choices=[('upper/lower respiratory tract infection', 'upper/lower respiratory tract infection'),('Abdominal infection /Peritonitis', 'Abdominal infection /Peritonitis'),('bones and joints sepsis', 'bones and joints sepsis'),('pyogenic meningitis', 'pyogenic meningitis'),('urinary tract infection', 'urinary tract infection'),('soft tissue infection', 'soft tissue infection')])