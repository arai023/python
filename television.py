class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    
    def power(self):
        self.__status = not self.__status
    
    def mute(self):
        if self.__status:
            self.__muted = not self.__status
    
    def channel_up(self):
        '''
        increase tv channel
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    
    def channel_down(self):
        '''
        decrease tv channel
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    
    def volume_up(self):
        '''
        increase volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
    
    def volume_down(self):
        '''
        decrease volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
    
    def __str__(self) -> str:
        return f"Power = {self.__status}, Channel = {self.__channel} Volume = {self.__volume}"
        

    