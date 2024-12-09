from django.test import TestCase
from .models import Categoria
from django.core.exceptions import ValidationError
# Create your tests here.
class TestCategoria(TestCase):
    def test_grabacion(self):
        categoria = Categoria(nombre="Bebidas")
        categoria.save()
        self.assertEqual(Categoria.objects.count(), 1)

    # def test_validacion_categoria(self):
    #     with self.assertRaises(ValidationError) as qv:
    #         q = Categoria.objects.create(nombre="No permitido")
    #         q.full_clean()

    #     mensaje = dict(qv.exceptions)
    #     self.assertEqual(mensaje['nombre'][0], ['Categoría no permitida.'])