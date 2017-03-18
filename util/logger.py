"""
Logger
- logs stuff to the console!
"""
from util import ConsoleColors

class Logger(str):
    """
    Logger class
    - class that houses the logger funcs
    """
    def success(self, message):
        """
        Success
        - prints success (green) color chat.
        """
        return ConsoleColors.GREEN + '[SUCCESS]: ' + message + '\n\n\n'
    def error(self, message):
        """
        Error
        - prints error (red) color chat.
        """
        return ConsoleColors.RED + '[ERROR]' + message + '\n\n\n'
