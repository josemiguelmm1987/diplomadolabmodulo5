from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 2 != 0:
        raise ValidationError(f'{value} no es un número par.')
    
def validation_categoria(value):
    if value == 'No permitido':
        raise ValidationError('Categoría no permitida.')