from service import Service
from message import Message

#store a list of vouchers by peers. Attempt to construct a voucher chain to a arbitary node
#wrap messages in encryption/decryption upon request


class SECservice(Service):
    """Handler of Chord behavoir and internal messages"""
    def __init__(self):
        super(Service, self).__init__()
        self.service_id = "SEC"
        self.priority = 1 #normal priority

    def handle_message(self, msg):
        if not msg.service == self.service_id:
            raise Exception("Mismatched service recipient for message.")
        return True

    def attach_to_console(self):
        ### return a list of command-strings
        return []

    def handle_command(self, comand_st, arg_str):
        ### one of your commands got typed in


