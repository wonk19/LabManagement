// Example / template. Copy values into firebase-config.js
// Firebase Console > Project settings > Your apps > Web app
// Realtime Database rules example:
// { "rules": { ".read": true, ".write": true } }
window.LAB_FIREBASE_CONFIG = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  databaseURL: "https://YOUR_PROJECT-default-rtdb.firebaseio.com",
  projectId: "YOUR_PROJECT",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Google Calendar sync (optional)
// 1) Google Cloud Console > APIs & Services > enable Google Calendar API
// 2) Create OAuth client ID (Application type: Web application)
// 3) Authorized JavaScript origins:
//    - https://wonk19.github.io
//    - http://localhost (optional, local testing)
// 4) Paste the client ID below into firebase-config.js
window.LAB_GOOGLE_CALENDAR = {
  clientId: "YOUR_OAUTH_WEB_CLIENT_ID.apps.googleusercontent.com",
  timeZone: "Asia/Seoul"
};
