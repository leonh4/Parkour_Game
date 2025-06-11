class Score:
    def __init__(self, elapsed_seconds, when):
        """
        This function initializes the score object.

        Args:
             elapsed_seconds (int): The elapsed time in seconds.
             when (datetime.datetime) The date and time of the score
        """
        self.elapsed_seconds = elapsed_seconds
        self.when = when

    def __str__(self):
        """
        This function returns a string representation of the score.

        The format of the string representation is:
        MM:ss | timestamp | total seconds

        Returns:
            str: The string representation of the score.
        """
        seconds = self.elapsed_seconds % 60
        minutes = self.elapsed_seconds // 60
        return  f"{minutes:02}:{seconds:02} | {self.when} | {self.elapsed_seconds}"


    def __lt__(self, other):
        """
        This function compares the score object to another score object.

        Args:
            other (Score): The other score object.

        Returns:
            bool: True if the score's elapsed seconds is less than the other's elapsed seconds, False otherwise.
        """
        return self.elapsed_seconds < other.elapsed_seconds