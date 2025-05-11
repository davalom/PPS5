import unittest
from charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):

    def test_palindromos_validos(self):
        #Pruebas con palíndromos válidos.
        palindromos = [
            "Anita lava la tina", 
            "Somos o no somos",  
            "'Amor azul' Ramera, de todo te di. Mariposa colosal, sí, yo de todo te di. Poda la rosa, Venus. El átomo como tal es un evasor alado. Pide, todo te doy: isla, sol, ocaso, pirámide. Todo te daré: mar, luz, aroma.", 
            "¿Acaso hubo búhos acá?", 
            "Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida", 
            "Adán y raza; azar y nada.", 
            "A ti no, bonita.", 
            "A mamá, Roma le aviva el amor a papá, y a papá, Roma le aviva el amor a mamá.", 
            "El bar es imán o zona miserable."
        ]
        for frase in palindromos:
            with self.subTest(frase=frase):
                self.assertTrue(esPalindromo(frase))

    def test_palindromos_invalidos(self):
        #Pruebas con cadenas que no son palíndromos.
        no_palindromos = [
            "Hola mundo", 
            "Python",
            "¿Acaso hubo búhos acá? [de Juan Filloy]"
        ]
        for frase in no_palindromos:
            with self.subTest(frase=frase):
                self.assertFalse(esPalindromo(frase))

    def test_entradas_invalidas(self):
        #Pruebas con cadenas que no son palíndromos.
        no_cadenas = [
            None, 
            False, 
            12321, 
            ['a', 'n', 'a']
        ]
        for entrada in no_cadenas:
            with self.subTest(entrada=entrada):
                self.assertFalse(esPalindromo(entrada))

    def test_cadena_vacia(self):
        #Verifica que una cadena vacía es considerada palíndroma.
        self.assertTrue(esPalindromo(""))

    def test_cadena_espacios(self):
        #Verifica que los espacios son ignorados correctamente.
        self.assertTrue(esPalindromo("a   a"))

    def test_numeros(self):
        #Verifica que la función maneja cadenas numéricas.
        self.assertTrue(esPalindromo("12321"))
        self.assertFalse(esPalindromo("12345"))

    def test_palabras_con_signos(self):
        #Verifica que los signos de puntuación no afectan el resultado.
        self.assertTrue(esPalindromo("Anita, lava la tina!"))
        self.assertFalse(esPalindromo("Anita, no laves la tina!"))

if __name__ == '__main__':
    unittest.main()
