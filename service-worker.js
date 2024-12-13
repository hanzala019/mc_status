// Cache name
const CACHE_NAME = "static";

// Files to cache
const urlsToCache = [
    "https://hanzala019.github.io/mc_status/index.html",
    "https://hanzala019.github.io/mc_status/offline.html",
    "https://hanzala019.github.io/mc_status/static/icons/icon-256.png",
    "https://hanzala019.github.io/mc_status/static/icons/icon-512.png",
    "https://hanzala019.github.io/mc_status/static/screenshots/Screenshot-wide.png",
    "https://hanzala019.github.io/mc_status/static/screenshots/Screenshot-narrow.png"
];

// Install the service worker
self.addEventListener("install", event => {
    console.log("installed")
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log("Opened cache");
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener("activate", event => {
    console.log("Service Worker Activated", event);
    // Force the service worker to take control of the page immediately
    // event.waitUntil(self.clients.claim());
});

self.addEventListener("push", event => {
    if (event.data) {
        const payload = event.data.json();
        console.log("payload: ",payload)
        self.registration.showNotification(payload.title, {
            body: payload.body,
            icon:"https://hanzala019.github.io/mc_status/static/icons/icon-512.png",
            badge:"https://hanzala019.github.io/mc_status/static/icons/icon-256.png"
            
        });
    } else {
        console.log("Push event but no data.");
    }
});


self.addEventListener("fetch", event => {
    if(event.request.method === "GET"){
    event.respondWith(
        fetch(event.request)
            .then(response => {
                // Return the cached response if available
                if (response) {
                    const resClone = response.clone()
                    caches.open(CACHE_NAME).then(cache=> cache.put(event.request,resClone))
                    console.log("cache response: ", response)
                    return response;
                }
            })
                // If network request fails, fall back to the offline page
                
                    .catch((e) => {
                        console.log(e)
                        return caches.match(e.request).then(res=> res)
                    })
           
    )}
});

// self.addEventListener("fetch", event => {
//     event.respondWith(
//        fetch(event.request)
//        .then(res => {
//         const resClone = res.clone()
//        })
//        .catch(()=>{
//         console.log(e.request)
//         caches.match(e.request)  
//        })
//     );
// });

