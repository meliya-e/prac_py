import sys
import socket
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer, _get_best_family

def get_local_ip():
    """Получает IP-адрес основного сетевого интерфейса."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def test(HandlerClass=SimpleHTTPRequestHandler,
         ServerClass=ThreadingHTTPServer,
         protocol="HTTP/1.0", port=8000, bind="0.0.0.0"):
    """Запускает HTTP-сервер."""
    ServerClass.address_family, addr = _get_best_family(bind, port)
    HandlerClass.protocol_version = protocol
    with ServerClass(addr, HandlerClass) as httpd:
        local_ip = get_local_ip()  # Теперь тут корректный IP
        print(
                f"Serving HTTP on {local_ip} port {port} "
                f"(http://{local_ip}:{port}/) ..."
        )
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    bind = sys.argv[2] if len(sys.argv) > 2 else "0.0.0.0"
    test(port=port, bind=bind)

