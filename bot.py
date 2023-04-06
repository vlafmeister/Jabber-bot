
from slixmpp import ClientXMPP


class Bot(ClientXMPP):
    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)


    def start(self, event):
        self.send_presence()
        self.get_roster()

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            message_text = msg['body']
            reply = "You said: {}".format(message_text)
            msg.reply(reply).send()

if __name__ == '__main__':
    xmpp = Bot("your_jabber_id", "your_password")
    xmpp.connect()
    xmpp.process()
