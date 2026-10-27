// Offline cache: the game files are cached on install; fonts are cached the first time they load.
const CACHE = 'olive-press-v1';
const FILES = ['./', 'index.html', 'three.min.js', 'manifest.webmanifest', 'icons/icon-192.png', 'icons/icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  // network first for the page so updates show up, cache first for everything else
  const isPage = e.request.mode === 'navigate';
  e.respondWith(
    isPage
      ? fetch(e.request).then(r => { const copy = r.clone(); caches.open(CACHE).then(c => c.put('index.html', copy)); return r; }).catch(() => caches.match('index.html'))
      : caches.match(e.request).then(hit => hit || fetch(e.request).then(r => {
          if (r.ok || r.type === 'opaque') { const copy = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); }
          return r;
        }))
  );
});
