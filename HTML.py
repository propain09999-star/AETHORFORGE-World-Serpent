<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <link rel="manifest" href="manifest.json">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="theme-color" content="#00ff9d">
  <title>AETHORFORGE</title>
  <style>
    /* Safe Area for 2026 Notchless Screens */
    body {
      padding-top: env(safe-area-inset-top);
      padding-bottom: env(safe-area-inset-bottom);
      /* ... paste the CSS from the Obsidian UI here ... */
    }
  </style>
</head>
<body>
  <script>
    // Native Service Worker Registration
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('sw.js');
      });
    }

    // Native Installation Trigger
    let deferredPrompt;
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredPrompt = e;
      // Optional: Show "Install to Home Screen" UI
    });
  </script>
</body>
</html>
