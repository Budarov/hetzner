#__all__ = ['wol']


class WOL(object):
    def __init__(self, server):
        self.conn = server.conn
        self.server = server

    def send_wol(self):
        result = self.conn.post('/wol/{0}'.format(str(self.server.number)), None)
        return result
