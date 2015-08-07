class Caesar:
    def __init__(self):
        self.__letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self, texto_plano, key = 3):
        '''(Caesar, str, int) -> str
        Retorna o texto_plano cifrado com a cifra de Cesar,
        utlizando a chave key, cujo padrao e 3.
        '''
        cipher_text = ''
        texto_plano = texto_plano.upper()
        for ch in texto_plano:
            if ch in self.__letters:
                idx = self.__letters.find(ch) + key
                if idx >= 26:
                    idx -= 26
                cipher_text += self.__letters[idx]
        return cipher_text

    def decrypt(self, texto_cifrado,  key = 3):
        ''' (Caesar, str, int) -> str
        Retorna em texto plano o texto_cifrado decifrado com a
        cifra de Cesar, utilizando a chave key, cujo padrao e 3.
        '''
        plain_text = ''
        texto_cifrado = texto_cifrado.upper()
        for ch in texto_cifrado:
            if ch in self.__letters:
                idx = self.__letters.find(ch) - key
                plain_text += self.__letters[idx]
        return plain_text.lower()