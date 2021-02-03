import random


def run():
    symbols = {
        1: 'a',
        2: 'A',
        3: 'b',
        4: 'B',
        5: 'c',
        6: 'C',
        7: 'd',
        8: 'D',
        9: 'e',
        10: 'E',
        11: 'f',
        12: 'F',
        13: 'g',
        14: 'G',
        15: 'h',
        16: 'i',
        17: 'I',
        18: 'j',
        19: 'J',
        20: 'k',
        21: 'K',
        22: 'l',
        23: 'L',
        24: 'm',
        25: 'M',
        26: 'n',
        27: 'N',
        28: 'o',
        29: 'O',
        30: 'p',
        31: 'P',
        32: 'q',
        33: 'Q',
        34: 'r',
        35: 'R',
        36: 's',
        37: 'S',
        38: 't',
        39: 'T',
        40: 'u',
        41: 'U',
        42: 'v',
        43: 'V',
        44: 'w',
        45: 'W',
        46: 'x',
        47: 'X',
        48: 'y',
        49: 'Y',
        50: 'z',
        51: 'Z',
        52: 'H',
        53: '0',
        54: '1',
        55: '2',
        56: '3',
        57: '4',
        58: '5',
        59: '6',
        60: '7',
        61: '8',
        62: '9',
        63: '!',
        64: '¡',
        65: '?',
        66: '¿',
        67: '|',
        68: '@',
        69: '#',
        70: '~',
        71: '€',
        72: '$',
        73: '%',
        74: '&',
        75: '/',
        76: '*',
        77: '-',
        78: '+',
        79: '_',
        80: '\\',
        81: '¬',
        82: '(',
        83: ')',
        84: '[',
        85: ']',
        86: '{',
        87: '}',
        88: ':',
        89: ',',
        90: '.',
        91: ';',
        92: '=',
        93: '<',
        94: '>'
        }

    print('********** Generador de contraseñas **********')
    caracteres = int(input('Introduce la cantidad de carácteres que quieres que tenga: '))

    cadena = []

    for number in range(caracteres):
            cadena.append(symbols[random.randint(1, 94)])
        
    password = ''.join(cadena)
    print('Tu nueva contraseña es: {}'.format(password))




if __name__ == '__main__':
    run()