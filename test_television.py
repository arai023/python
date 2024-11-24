import pytest
from television import *


class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
    
    def test_power(self):
        #turn on TV
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        #Turn off TV
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        #muted
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        #unmuted
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        #TV off
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"


    def test_channel_up(self):
        #TV off
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        #TV on
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test_channel_down(self):
        #TV off
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        #TV on
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 0"
        #decrease channel
        self.tv.channel_down()
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 0"

    
    def test_volume_up(self):
        #TV off
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        #TV on and increase volume to max
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 2"

    
    
    def test_volume_down(self):
        #TV off
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        #Turn TV on and increase volume to max and then decrease
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        #decrease volume to minimum
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
