import socket
import sys


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print >>log_buffer, "making a server on {0}:{1}".format(*address)
    sock.bind(address)
    sock.listen(1)
    
    try:
        while True:
            print >>log_buffer, 'waiting for a connection'
            conn, addr = sock.accept() # blocking
            try:
                print >>log_buffer, 'connection - {0}:{1}'.format(*addr)
                while True:
                    data = conn.recv(1024)
                    request += data
                    if len(data) < 1024 or not data:
                        break

                req_ok =  parse_request(data)
                print >>log_buffer, 'sending response'
                if req_ok == True:
                    response = response_ok()
                    conn.sendall(response)

            finally:
                conn.close()
            
    except KeyboardInterrupt:
        sock.close()
        return

def response_ok():
    """returns a basic HTTP response"""
    resp = []
    resp.append("HTTP/1.1 200 OK")
    resp.append("Content-Type: text/plain")
    resp.append("")
    resp.append("this is a pretty minimal response")
    return "\r\n".join(resp)

def parse_request(request):
    if request[:3] != "GET":
        raise NotImplementedError("We only accept GET")
    print >>sys.stderr, "request is okay"
    return True


def response_method_not_allowed():
    
    return "not ok"    

if __name__ == '__main__':
    server()
    sys.exit(0)
