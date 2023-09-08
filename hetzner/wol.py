
#__all__ = ['WOL']


class WOL(object):
    def __init__(self, server):
        self.conn = server.conn

    def send_wol(self):
        result = self.conn.put('/wol/{0}'.format(str(self.number)), None)
        return result
