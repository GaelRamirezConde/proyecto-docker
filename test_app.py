import unittest
from app import calcular_suma

class PruebasUnitarias(unittest.TestCase):
    
    def test_suma_correcta(self):
        resultado = calcular_suma(0, 10)
        self.assertEqual(resultado, 10)
        
    def test_suma_acumulada(self):
        resultado = calcular_suma(50, 10)
        self.assertEqual(resultado, 60)

if __name__ == '__main__':
    unittest.main()