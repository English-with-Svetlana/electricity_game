"""Local HTTP resource verification; does not replace interactive browser QA."""
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from urllib.request import urlopen
import hashlib, json, re
ROOT = Path(__file__).resolve().parent.parent
class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, url):
        if not url.startswith('/electricity_game/'):
            return str(ROOT / '__outside_project_path__')
        return str(ROOT / url.split('?', 1)[0][len('/electricity_game/'):])
    def log_message(self, *args):
        pass
server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
Thread(target=server.serve_forever, daemon=True).start()
try:
    base = 'http://127.0.0.1:%d/electricity_game/' % server.server_port
    manifest = (ROOT / 'release-assets.js').read_text()
    urls = list(json.loads(manifest.split('Object.freeze(', 1)[1].rsplit(');', 1)[0]).values())
    outer_html = urlopen(base).read().decode()
    game_url = re.search(r'src="(game\.html\?v=[a-f0-9]+)"', outer_html).group(1)
    with urlopen(base + game_url) as response:
        game_bytes = response.read()
        assert hashlib.sha256(game_bytes).hexdigest()[:20] == game_url.split('?v=')[1]
    html = game_bytes.decode()
    urls += re.findall(r'(?:href|src)="((?:style\.css|script\.js|release-assets\.js)\?v=[a-f0-9]+)"', html)
    assert len(urls) >= 84
    for resource in urls:
        with urlopen(base + resource) as response:
            assert response.status == 200
            content = response.read()
            assert hashlib.sha256(content).hexdigest()[:20] == resource.split('?v=')[1], resource
    assert urlopen(base + '.nojekyll').read() == b''
    print('PASS: stable outer entry, versioned game document, .nojekyll, and %d versioned resources under /electricity_game/; all content hashes match.' % len(urls))
finally:
    server.shutdown()
    server.server_close()
