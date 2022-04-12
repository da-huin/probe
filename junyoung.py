class Junyoung:

    def __init__(self,IQ):
        self._nick_name = 'ness'
        self._address = 'choungjoo'
        self._age = '92'
        self._IQ = IQ
        
    def junyoung(self):
        
        return print(self._nick_name), print(self._address),print(self._age),print(self._IQ)
            
    
    @property
    def IQ(self):
        return self._IQ
    
    @IQ.setter
    def IQ(self,IQ):
        
        self._IQ = IQ


if __name__ == '__main__':
    ness = Junyoung(1)
    ness.junyoung()