import socket
from qrcode_terminal import draw


def find_ip():
    '''
    Returns local IP address of the machine.
    '''
    socket_lib = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # this sees if device is connected to internet
    socket_lib.connect(("8.8.8.8", 80))
    ip_address = socket_lib.getsockname()[0]
    socket_lib.close()
    return ip_address


def initialize():
    host = find_ip()
    port = 3000

    draw(f"http://{host}:{port}")
