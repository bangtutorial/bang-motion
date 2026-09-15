"""Server statis tanpa cache.

http.server bawaan membiarkan browser menyimpan modul JS pakai heuristik,
jadi edit timeline/scene kadang tidak terlihat setelah reload biasa.
Cache-Control: no-store memaksa browser mengambil berkas segar setiap kali.

Pakai:  python tools/serve.py   (port 5178)
"""
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5178

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, *args):
        pass  # senyap; log request tidak berguna di sini

if __name__ == '__main__':
    print(f'serving on http://127.0.0.1:{PORT} (no-store)')
    ThreadingHTTPServer(('127.0.0.1', PORT), NoCacheHandler).serve_forever()
