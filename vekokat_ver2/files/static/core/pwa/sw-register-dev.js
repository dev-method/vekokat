if (!('serviceWorker' in navigator)) {
  console.log('Service worker not supported');
}

navigator.serviceWorker.register('/sw.js', {
    scope: '/'
})
.then(function(registration) {
  console.log('Registered at scope:', registration.scope);
})
.catch(function(error) {
  console.log('Registration failed:', error);
});
