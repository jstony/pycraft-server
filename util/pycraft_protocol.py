"""
Pycraft Protocol
- holds pycraft protocol class
"""
from quarry.net.server import ServerProtocol

class PycraftProtocol(ServerProtocol):
    """
    Pycraft Protocol
    - handles stuff inside the server.
    """
    def player_joined(self):
        """
        Player joined
        - on player join, do this
        """
        ServerProtocol.player_joined(self)

        self.send_packet(
            'join_game',
            self.buff_type.pack('iBiBB', 0, 3, 0, 0, 0),
            self.buff_type.pack_string('flat'),
            self.buff_type.pack('?', False))

        self.send_packet(
            'player_position_and_look',
            self.buff_type.pack('dddff?', 0, 255, 0, 0, 0, 0b00000),
            self.buff_type.pack_varint(0))

        self.tasks.add_loop(1.0, self.update_keep_alive)

    def update_keep_alive(self):
        """
        Update keep alive
        - server will bounce you out if not
        """
        self.send_packet('keep_alive', self.buff_type.pack_varint(0))

    def packet_chat_message(self, buff):
        """
        Packet chat message
        - relays chat message to all players
        """
        p_text = buff.unpack_string()
        self.factory.send_chat('<{}>, {}'.format((self.display_name, p_text)))
