from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    """ A class that is responsible for processing incoming requests from clients """

    def do_GET(self):
        """ Method for handling incoming GET requests """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open('contacts.html', 'r', encoding='utf-8') as f:
            content = f.read()
        self.wfile.write(bytes(content, 'utf-8'))


if __name__ == '__main__':
    web_server = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print('Server stopped')
