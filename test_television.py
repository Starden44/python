import pytest
from television import *

class Test:

    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        self.tv1 = None

    def test_television_power(self):
        # Tests power functionality
        assert self.tv1._Television__status == False
        self.tv1.power()
        assert self.tv1._Television__status == True
        self.tv1.power()
        assert self.tv1._Television__status == False

    def test_television_mute(self):
        # Tests mute won't work when TV is off
        assert self.tv1._Television__muted == False
        self.tv1.mute()
        assert self.tv1._Television__muted == False

        # Turn the TV on and test mute functionality
        self.tv1.power()
        self.tv1.mute()
        assert self.tv1._Television__prev_volume == self.tv1._Television__volume
        assert self.tv1._Television__muted == True
        assert self.tv1._Television__volume == self.tv1.MIN_VOLUME

    def test_television_volume_up_down(self):
        # Ensure the TV is initially off and volume cannot be changed
        assert self.tv1._Television__volume == self.tv1.MIN_VOLUME
        self.tv1.volume_up()
        assert self.tv1._Television__volume == self.tv1.MIN_VOLUME
        self.tv1.volume_down()
        assert self.tv1._Television__volume == self.tv1.MIN_VOLUME


        # Test initial volume state and volume up functionality
        self.tv1.power()
        assert self.tv1._Television__volume == self.tv1.MIN_VOLUME
        self.tv1.volume_up()
        assert self.tv1._Television__volume == self.tv1.MIN_VOLUME + 1
        self.tv1.volume_up()
        assert self.tv1._Television__volume == self.tv1.MAX_VOLUME
        self.tv1.volume_up()
        assert self.tv1._Television__volume == self.tv1.MAX_VOLUME

        # Test volume down functionality
        self.tv1.volume_down()
        assert self.tv1._Television__volume == self.tv1.MAX_VOLUME - 1
        self.tv1.volume_down()
        assert self.tv1._Television__volume == self.tv1.MIN_VOLUME
        self.tv1.volume_down()
        assert self.tv1._Television__volume == self.tv1.MIN_VOLUME

    def test_television_channel_up_down(self):
        # Ensure the TV is initially off and channel cannot be changed
        assert self.tv1._Television__channel == self.tv1.MIN_CHANNEL
        self.tv1.channel_up()
        assert self.tv1._Television__channel == self.tv1.MIN_CHANNEL
        self.tv1.channel_down()
        assert self.tv1._Television__channel == self.tv1.MIN_CHANNEL

        # Test initial channel state and up channel
        self.tv1.power()
        assert self.tv1._Television__channel == self.tv1.MIN_CHANNEL
        self.tv1.channel_up()
        assert self.tv1._Television__channel == self.tv1.MIN_CHANNEL + 1
        self.tv1.channel_up()
        assert self.tv1._Television__channel == self.tv1.MIN_CHANNEL + 2
        self.tv1.channel_up()
        assert self.tv1._Television__channel == self.tv1.MAX_CHANNEL
        self.tv1.channel_up()
        assert self.tv1._Television__channel == self.tv1.MIN_CHANNEL

        # Test channel down from min channel
        self.tv1.channel_down()
        assert self.tv1._Television__channel == self.tv1.MAX_CHANNEL
        self.tv1.channel_down()
        assert self.tv1._Television__channel == self.tv1.MAX_CHANNEL - 1
        self.tv1.channel_down()
        assert self.tv1._Television__channel == self.tv1.MAX_CHANNEL - 2
        self.tv1.channel_down()
        assert self.tv1._Television__channel == self.tv1.MIN_CHANNEL

if __name__ == "__main__":
    pytest.main()