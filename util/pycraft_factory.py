"""
Pycraft Factory
- houses pycraft factory class
"""
from quarry.net.server import ServerFactory
from util.pycraft_protocol import PycraftProtocol

class PycraftFactory(ServerFactory):
    """
    Pycraft Factory
    - handles factory
    """
    protocol = PycraftProtocol
    motd = "PycraftServer says hello!"

    def send_chat(self, message):
        """
        Send chat
        - handles when chat is sent
        """
        data = self.buff_type.pack_chat(message) + self.buff_type.pack('B', 0)

        for player in self.players:
            player.send_packet("chat_message", data)
