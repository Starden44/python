class Television:
    """A class representing a television standard functionality.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initializes the television with default settings.
        Sets the television to be powered off, unmuted, with the volume at the minimum level, and the channel at the minimum channel.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__prev_volume = self.__volume

    def power(self) -> None:
        """Method to toggle the power state of the television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Method to toggle the mute state of the television."""
        if self.__status == True:
            self.__muted = not self.__muted
            self.__volume = self.MIN_VOLUME if self.__muted else self.__prev_volume

    def channel_up(self) -> None:
        """Method to increase the tv channel by 1.
        """
        if self.__status == True:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """Method to decrease the tv channel by 1.
        """
        if self.__status == True:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
    def volume_up(self) -> None:
        """Method to increase the tv's volume by one.
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
            self.__prev_volume = self.__volume

    def volume_down(self) -> None:
        """Method to decrease the tv's volume by one.
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
            self.__prev_volume = self.__volume

    def __str__(self) -> str:
        """Returns a string representation of the television's current state."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"