from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile 
        fields = ('foretag', 'stad')
		
		
		
class CategorySelectionForm(forms.ModelForm):
	
	class Meta:
		model = UserProfile 
		fields = ('bol1',	'bol2',	'bol3',	'bol4',	'bol5',	'bol6',	'bol7',	'bol8',	'bol9',	'bol10',	'bol11',	'bol12',	'bol13',	'bol14',	'bol15',	'bol16',	'bol17',	'bol18',	'bol19',	'bol20',	'bol21',	'bol22',	'bol23',	'bol24',	'bol25',	'bol26',	'bol27',	'bol28',	'bol29',	'bol30',	'bol31',	'bol32',	'bol33',	'bol34',	'bol35',	'bol36',	'bol37',	'bol38',	'bol39',	'bol40',	'bol41',	'bol42',	'bol43',	'bol44',	'bol45',	'bol46',	'bol47',	'bol48',	'bol49',	'bol50',	'bol51',	'bol52',	'bol53',	'bol54',	'bol55',	'bol56',	'bol57',	'bol58',	'bol59',	'bol60',	'bol61',	'bol62',	'bol63',	'bol64',	'bol65',	'bol66',	'bol67',	'bol68',	'bol69',	'bol70',	'bol71',	'bol72',	'bol73',	'bol74',	'bol75',	'bol76',	'bol77',	'bol78',	'bol79',	'bol80',	'bol81',	'bol82',	'bol83',	'bol84',	'bol85',	'bol86',	'bol87',	'bol88',	'bol89',	'bol90',	'bol91',	'bol92',	'bol93',	'bol94',	'bol95',	'bol96',	'bol97',	'bol98',	'bol99',	'bol100',	'bol101',	'bol102',	'bol103',	'bol104',	'bol105',	'bol106',	'bol107',	'bol108',	'bol109',	'bol110',	'bol111',	'bol112',	'bol113',	'bol114',	'bol115',	'bol116',	'bol117',	'bol118',	'bol119',	'bol120',	'bol121',	'bol122',	'bol123',  'bol124',	'bol125',	'bol126',	'bol127',	'bol128')