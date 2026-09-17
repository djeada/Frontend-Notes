import {createServer} from 'node:http';
import {readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {dirname, join} from 'node:path';
import {calculateQuote} from './quote.mjs';

const publicDir = join(dirname(fileURLToPath(import.meta.url)), 'public');
const pages = new Map([['/', ['index.html', 'text/html; charset=utf-8']], ['/styles.css', ['styles.css', 'text/css; charset=utf-8']], ['/app.js', ['app.js', 'text/javascript; charset=utf-8']]]);
function json(res, status, payload) {
  res.writeHead(status, {'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store'});
  res.end(JSON.stringify(payload));
}
export function createAppServer() {
  return createServer(async (req, res) => {
    const path = new URL(req.url, 'http://localhost').pathname;
    if (path === '/api/quote') {
      if (req.method !== 'POST') return json(res, 405, {error: 'Use POST.'});
      try {
        let body = '';
        for await (const chunk of req) {
          body += chunk.toString();
          if (body.length > 4096) return json(res, 413, {error: 'Request too large.'});
        }
        let input;
        try { input = JSON.parse(body); } catch { return json(res, 400, {error: 'Invalid JSON.'}); }
        return json(res, 200, calculateQuote(input));
      } catch (error) {
        if (error instanceof RangeError) return json(res, 400, {error: error.message});
        return json(res, 500, {error: 'Unexpected server error.'});
      }
    }
    if (req.method !== 'GET' || !pages.has(path)) {
      res.writeHead(404, {'content-type': 'text/plain; charset=utf-8'});
      return res.end('Not found');
    }
    const [name, type] = pages.get(path);
    try {
      const content = await readFile(join(publicDir, name));
      res.writeHead(200, {'content-type': type, 'cache-control': 'no-store'});
      res.end(content);
    } catch {
      res.writeHead(500);
      res.end('Cannot load page');
    }
  });
}
if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  createAppServer().listen(Number(process.env.PORT || 4173), '127.0.0.1', () => {
    console.log(`Shipping demo: http://127.0.0.1:${process.env.PORT || 4173}`);
  });
}
