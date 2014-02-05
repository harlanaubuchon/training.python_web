import socket
import sys
import os
import mimetypes

HOME_DIR = "."
HOME_PATH = os.getcwd()

def response_ok(body, mimetype):
    """returns a basic HTTP response"""
    resp = []
    resp.append("HTTP/1.1 200 OK")
    resp.append("Content-Type: %s" % mimetype)
    resp.append("")
    resp.append(body)
    return "\r\n".join(resp)


def response_method_not_allowed():
    """returns a 405 Method Not Allowed response"""
    resp = []
    resp.append("HTTP/1.1 405 Method Not Allowed")
    resp.append("")
    return "\r\n".join(resp)

def response_not_found():
    """returns a 404 Resource does not exist response"""
    resp = []
    resp.append("HTTP/1.1 404 Not Found")
    resp.append("")
    return "\r\n".join(resp)    


def parse_request(request):
    first_line = request.split("\r\n", 1)[0]
    method, uri, protocol = first_line.split()
    print >>sys.stderr, 'parse_request - %s' % request
    if method != "GET":
        raise NotImplementedError("We only accept GET")
    print >>sys.stderr, 'request %s is okay' % method
    return uri


def server():
    address = ('127.0.0.1', 8888)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print >>sys.stderr, "making a server on %s:%s" % address
    sock.bind(address)
    sock.listen(1)
    
    try:
        while True:
            print >>sys.stderr, 'waiting for a connection'
            conn, addr = sock.accept() # blocking
            try:
                print >>sys.stderr, 'connection - %s:%s' % addr
                request = ""
                while True:
                    data = conn.recv(1024)
                    request += data
                    if len(data) < 1024 or not data:
                        break

                try:
                    uri = parse_request(request)

                except NotImplementedError:
                    print >>sys.stderr, 'parse exception'
                    response = response_method_not_allowed()
                
                try:
                    body, mimetype = resolve_uri(uri)
                    response = response_ok(body, mimetype)
                
                except ValueError:
                    print >>sys.stderr, '404'
                    response = response_not_found()

                print >>sys.stderr, 'sending response'
                conn.sendall(response)

            finally:
                conn.close()
            
    except KeyboardInterrupt:
        sock.close()
        return

## <a class="icon dir" href="file:///home/webroot/">webroot/</a>
def resolve_uri(uri):
    ## URI represents a directory
    path = HOME_DIR + uri
    content = ""
    mimetype = 'text/plain'

    if uri.find('.') > 0:
        if os.path.isfile(path) == True:
            with open(HOME_DIR + uri) as file_handle:
                content = file_handle.read()
                mimetype = mimetypes.guess_type(uri)[0]
            print >>sys.stderr, 'file data found for - %s' % uri
    
    elif uri.find('.') < 0:
        if os.path.isdir(path) == True:
            dir_contents = os.listdir(HOME_DIR + uri)
            for i in dir_contents:
                content += i + "\r\n"
            print >>sys.stderr, 'directory found for - %s' % uri

    else:
        #if os.path.isdir(path) == False and os.path.isfile(path) == False:
        print >>sys.stderr, 'No File/Dir found'
        raise ValueError('No File/Dir found')

  
    return content, mimetype


if __name__ == '__main__':
    server()
    sys.exit(0)
