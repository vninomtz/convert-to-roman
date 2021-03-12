"""
Autor: Victor Manuel Niño Martínez
Fecha creación: 11/03/2021
"""
from collections import OrderedDict


class Roman:
    """ Clase para convertir numeros enteros a Romanos """

    __romanKeys = OrderedDict()
    __romanKeys[1000] = 'M'
    __romanKeys[900] = 'CM'
    __romanKeys[500] = 'D'
    __romanKeys[400] = 'CD'
    __romanKeys[100] = 'C'
    __romanKeys[90] = 'XC'
    __romanKeys[50] = 'L'
    __romanKeys[40] = 'XL'
    __romanKeys[10] = 'X'
    __romanKeys[9] = 'IX'
    __romanKeys[5] = 'V'
    __romanKeys[4] = 'IV'
    __romanKeys[1] = 'I'

    @classmethod
    def convert_from_int(cls, number: int):
        """
        Método público que recibe un numero entero
        y devuelve su correspondiente en numero Romano
        """
        try:
            cls.__is_number_valid(cls, number)
            return cls.__number_to_roman(cls, number)
        except ValueError as ex:
            raise ValueError from ex

    def __number_to_roman(self, num):
        """ Función privada con algoritmo para convertir de entero a romano """
        if num == 0:
            return ""
        roman = ""
        for key, value in self.__romanKeys.items():
            num_repetitions = num // key
            roman += value * num_repetitions
            num -= key * num_repetitions
        return roman

    def __is_number_valid(self, number: int):
        """ Función para validar las entradas de los usuarios """
        if not number:
            raise ValueError("Numero nulo")
        if not isinstance(number, int):
            raise ValueError("No es un número")
        if number < 1 or number > 3000:
            raise ValueError("Solo se aceptan numeros entre 1 y 3000")
