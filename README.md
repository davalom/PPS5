# Verificador de Palíndromos

## Descripción
Este programa sirve para verificar si una cadena de texto es un palíndromo. Un palíndromo es una palabra, frase o secuencia que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios, acentos y signos de puntuación.

## Tecnologías Utilizadas
- **Lenguaje de Programación**: Python 3.x
- **Bibliotecas**:
  - `re` (expresiones regulares) para el procesamiento de texto

## Características
- Verifica si una cadena es un palíndromo
- Ignora espacios, acentos y signos de puntuación
- Maneja caracteres especiales y acentos en español
- Incluye pruebas unitarias para validar la funcionalidad

## Instalación
1. Instalar Python 3.x
2. Clonar el repositorio
4. Crear un entorno virtual y activarlo
3. Instalar las dependencias necesarias

## Uso
### Como Script
```bash
python charfun.py
```
El programa pedirá una frase por consola e indicará si es un palíndromo o no.

### Como Módulo
```python
from charfun import esPalindromo

# Ejemplo de uso
resultado = esPalindromo("Anita lava la tina")
print(resultado)  # True
```

## Ejemplos de Palíndromos
- "Anita lava la tina"
- "Oso"
- "Reconocer"
- "A mamá, Roma le aviva el amor a papá, y a papá, Roma le aviva el amor a mamá"

## Pruebas
El proyecto incluye pruebas unitarias en el archivo `test_charfun.py`. Para ejecutar las pruebas:
```bash
python -m unittest test_charfun.py
```

## Autor
- **Nombre**: David AO
- **Fecha**: Mayo de 2025

## Licencia
Este proyecto está bajo la Licencia MIT.