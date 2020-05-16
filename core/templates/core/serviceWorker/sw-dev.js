/*jshint esversion: 6 */
/* jshint node: true */
importScripts("https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js");
workbox.precaching.precacheAndRoute([]);
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
