from django import forms
from .models import Student, Note
from .validators import validate_cpf

class StudentForm(forms.ModelForm):
    ncpf = forms.CharField(label='CPF(sem hífen)', validators=[validate_cpf] )
    class Meta:
        model = Student 
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'lname': 'Sobrenome',
            'nrg': 'Número RG',
            'birth_date': 'Data de nascimento',
            'nphone01': 'Telefone',
            'nphone02': 'Celular',
            'addr01': 'Endereço',
            'addr02': 'Complemento',
            'district': 'Bairro',
            'ncep': 'CEP',
            'local': 'Cidade',
            'state': 'Estado',
            'email': 'Email',
            'course': 'Curso',
            'team': 'Turma',
            'college': 'Instituição',
            'finish': 'Conclusão',
            'novalid': 'Inativo',
        }
        
        widgets = {
            'birth_date'	: forms.TextInput(attrs={'type':'date'}),
            'ncep'	: forms.TextInput(attrs={'type':'number'}),
            'nphone01': forms.TextInput(attrs={'type':'number'}),
            'nphone02': forms.TextInput(attrs={'type':'number'}),
            'team': forms.TextInput(attrs={'type':'number'}),
        }
        

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        labels = {'student': 'Aluno', 'text':''}
