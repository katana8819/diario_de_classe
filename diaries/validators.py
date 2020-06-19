from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_cpf(value):
	string_cpf = value
	if (len(string_cpf) != 11) or (not string_cpf.isdigit()):
		raise ValidationError(
            _(f'{value} CPF inválido!'),
            params={'value': value},
        )
