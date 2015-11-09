import socketserver

class CEL_UDP_Handler(socketserver.BaseRequestHandler):
    '''
    Test handler for UDP messages from CEL's ZigBee-Ethernet gateway
    which sends datagram messages. This script must be started on the server
    machine which will be parse incoming data
    '''
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{}:{} wrote:".format(self.client_address[0],
                                    self.client_address[1]))
        spl_data = self.parse_data(data)
        print('{} sent value {}'.format(spl_data[0], spl_data[1]))

    def parse_data(self, data):
        data_str = data.decode('utf-8')
        splited_data = [x.strip() for x in data_str.split(':')]

        return splited_data

if __name__ == "__main__":
    PORT = 5555
    ADDRESS = '192.168.22.225'
    localserver = (ADDRESS, PORT)
    server = socketserver.UDPServer(localserver, CEL_UDP_Handler)
    server.serve_forever()
