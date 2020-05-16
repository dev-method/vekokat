/*jshint esversion: 6 */
/* jshint node: true */
importScripts("https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js");
workbox.precaching.precacheAndRoute([
  {
    "url": "static/core/css/prod/prod-style-newdesign.css",
    "revision": "e0089998f5c915d35cdeecceea66d8c0"
  },
  {
    "url": "static/core/css/prod/prod-style.css",
    "revision": "7bdff88fef009f0cb5c7e7314dc530f8"
  },
  {
    "url": "static/core/plugins/prod/base.js",
    "revision": "0fa9defac2d548c9579dc5bce1d7387a"
  },
  {
    "url": "static/core/plugins/prod/main.js",
    "revision": "f001df6f2fa3cbf9aea8ddda558eda7b"
  },
  {
    "url": "static/core/plugins/react/bundle-prod.js",
    "revision": "0d948234fdb728a1424ef9a71d89143f"
  },
  {
    "url": "static/core/plugins/react/bundle.js",
    "revision": "924d43ed14c442233ecee22990685b93"
  },
  {
    "url": "static/core/pwa/base.html",
    "revision": "d4fc08cc57238978b5c536662c2eed7f"
  },
  {
    "url": "static/core/pwa/icons/icon150x150.png",
    "revision": "fc6b116f960409ae0840b6be1ba0bd66"
  },
  {
    "url": "static/core/pwa/icons/icon180x180.png",
    "revision": "29a094741b64ddab45e5117cca59b21e"
  },
  {
    "url": "static/core/pwa/icons/icon192x192.png",
    "revision": "3d2b69452dd7b828a8fb672261b5333c"
  },
  {
    "url": "static/core/pwa/icons/icon310x150.png",
    "revision": "43679a7efaac0be62c08c9cbd7a392a5"
  },
  {
    "url": "static/core/pwa/icons/icon310x310.png",
    "revision": "c879c27d62d20f8a30ac93f7f6e3f8ae"
  },
  {
    "url": "static/core/pwa/icons/icon512x512.png",
    "revision": "ae3a2533d415f7aee89f28b72a6cad9f"
  },
  {
    "url": "static/core/pwa/icons/icon70x70.png",
    "revision": "d11416548d8353f7e3a6596131f50642"
  },
  {
    "url": "static/core/pwa/new_icons/icon150x150.png",
    "revision": "7372478bd388e0747814682b4310041c"
  },
  {
    "url": "static/core/pwa/new_icons/icon180x180.png",
    "revision": "a92ddd18a4510a7fe15d07789725182b"
  },
  {
    "url": "static/core/pwa/new_icons/icon192x192.png",
    "revision": "64b6634eb0cfdb57fc42feedbfb42834"
  },
  {
    "url": "static/core/pwa/new_icons/icon310x150.png",
    "revision": "e1b12ad1c0d76ec7e0421e6d2f4e6d9b"
  },
  {
    "url": "static/core/pwa/new_icons/icon310x310.png",
    "revision": "ac9dcaa6f31598398d3478c6574d7f54"
  },
  {
    "url": "static/core/pwa/new_icons/icon512x512.png",
    "revision": "ac52212317ad2d75850780b5d2c2a081"
  },
  {
    "url": "static/core/pwa/new_icons/icon70x70.png",
    "revision": "f7219f31765722627f125b69d7c24607"
  },
  {
    "url": "static/core/pwa/sw-register-dev.js",
    "revision": "a237db333c9ff50bfd5c062062acb2d0"
  }
]);
workbox.googleAnalytics.initialize();

workbox.routing.registerRoute(
  new RegExp('https://use.fontawesome.com/112094bd1f.js'),
  new workbox.strategies.NetworkFirst()
);

workbox.routing.registerRoute(
  new RegExp('https://cdnjs.cloudflare.com/ajax/libs/vanilla-lazyload/8.7.1/lazyload.min.js'),
  new workbox.strategies.NetworkFirst()
);

workbox.routing.registerRoute(
  new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
  new workbox.strategies.NetworkFirst({
    cacheName: 'google-fonts',
    plugins: [
      new workbox.cacheableResponse.Plugin({
        statuses: [0, 200],
      }),
    ]
  })
);
workbox.routing.registerRoute(
  new RegExp('https://www.google.com/maps/(.*)'),
  new workbox.strategies.NetworkFirst({
  })
);
workbox.routing.registerRoute(
  new RegExp('https://maps.googleapis.com/maps/(.*)'),
  new workbox.strategies.NetworkFirst({
  })
);

workbox.routing.registerRoute(
  // Cache image files
  /.*\.(?:png|jpg|jpeg|svg|gif)/,
  // Use the cache if it's available
  new workbox.strategies.NetworkFirst({
    // Use a custom cache name
    cacheName: 'image-cache',
    plugins: [
      new workbox.expiration.Plugin({
        // Cache only 20 images
        maxEntries: 30,
        // Cache for a maximum of a week
        maxAgeSeconds: 7 * 24 * 60 * 60,
      })
    ],
  })
);

workbox.routing.registerRoute(
  /.*\.(?:ttf|otf)/,
  new workbox.strategies.NetworkFirst({
    cacheName: 'font-cache',
  })
);

workbox.routing.registerRoute(
  new RegExp('\/'),
  new workbox.strategies.NetworkFirst()
);
workbox.routing.registerRoute(
  new RegExp('contacts\/$'),
  new workbox.strategies.NetworkFirst()
);
