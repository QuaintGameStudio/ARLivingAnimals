import http.server, ssl

server_address = ('0.0.0.0', 8080)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving HTTPS on https://192.168.1.8:8080 ...")
httpd.serve_forever()
