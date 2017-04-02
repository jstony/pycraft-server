"""
MinecraftServer
- Minecraft Server written in Python :)
"""
from util import Logger, PycraftFactory
from twisted.internet import reactor

PORT = 25565

print Logger().success('Server is listening on port :' + str(PORT))

factory = PycraftFactory()
factory.listen('', PORT)

reactor.run()
