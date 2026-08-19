#!/usr/bin/env python3
import http.server, socketserver, os, mimetypes

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

with socketserver.ThreadingTCPServer(('0.0.0.0', 4173), H) as httpd:
    httpd.allow_reuse_address = True
    httpd.serve_forever()
