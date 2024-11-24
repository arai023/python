class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''The TV begins with the following settings:
            - Power is off
            - Mute is off
            - Volume is set to the minimum volume
            - Channel is set to the minimum channel number
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    
    def power(self) -> None:
        '''
        Switches the power status of the TV
        '''
        self.__status = not self.__status
    
    def mute(self) -> None:
        '''
        If the TV is on, the mute status can be changed
        '''
        if self.__status:
            self.__muted = not self.__status
    
    def channel_up(self) -> None:
        '''
        increases tv channel by 1
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    
    def channel_down(self) -> None:
        '''
        decreases tv channel by 1
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    
    def volume_up(self) -> None:
        '''
        increases volume by 1
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
    
    def volume_down(self) -> None:
        '''
        decreases volume by 1
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
    
    def __str__(self) -> str:
        '''
        Shows tv status
        '''
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
        

    