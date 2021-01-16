importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.0.0/workbox-sw.js');

const OFFLINE_URL = '{{ offline_url }}';
const appShell = [
    '{{ icon_url }}',
    '{{ manifest_url }}',
    '{{ home_url }}',
    '{{ offline_url }}',
].map((partialUrl) => `${location.protocol}//${location.host}${partialUrl}`);

/*
// Precache the shell.
workbox.precaching.precacheAndRoute(appShell.map(url => ({
    url,
    revision: null,
})));

// Serve the app shell from the cache.
workbox.routing.registerRoute(({url}) => appShell.includes(url), new workbox.strategies.CacheOnly());

workbox.routing.registerRoute(
    ({url}) => !appShell.includes(url),
    new workbox.strategies.StaleWhileRevalidate({
        cacheName: 'dynamic-cache',
        plugins: [new workbox.expiration.ExpirationPlugin({
            maxEntries: 50,
            maxAgeSeconds: 31536000
        })],
    })
);
*/

// Handle offline.
workbox.routing.setCatchHandler(({ event }) => {
    console.log(event)
    switch (event.request.method) {
        case 'GET':
            return caches.match(OFFLINE_URL);
        default:
            return Response.error();
    }
});
