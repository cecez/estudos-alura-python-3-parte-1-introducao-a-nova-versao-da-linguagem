# Formatação de strings

Documentação: https://docs.python.org/3/library/string.html#formatexamples

```python

# Formatação de floats

>>> print("Tentativa {1} de {0}".format(1, 3))
Tentativa 3 de 1

>>> print("R$ {}".format(1.59))
R$ 1.59

>>> print("R$ {:f}".format(1.59))
R$ 1.590000

>>> print("R$ {:.2f}".format(1.59))
R$ 1.59

>>> print("R$ {:.2f}".format(1.5))
R$ 1.50

>>> print("R$ {:.2f}".format(1.5))
R$ 1.50

>>> print("R$ {:.2f}".format(1234.50))
R$ 1234.50

>>> print("R$ {:7.2f}".format(1234.50))
R$ 1234.50

>>> print("R$ {:7.2f}".format(1.5))
R$    1.50

>>> print("R$ {:07.2f}".format(1.5))
R$ 0001.50

# Formatação de inteiros (dígitos)

>>> print("R$ {:07d}".format(4))
R$ 0000004

>>> print("Data {:02d}/{:02d}".format(9, 4))
Data 09/04

>>> print("Data {:02d}/{:02d}".format(19, 11))
Data 19/11

```