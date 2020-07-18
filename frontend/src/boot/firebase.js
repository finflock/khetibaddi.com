// Firebase App (the core Firebase SDK) is always required and must be listed first
import * as firebase from "firebase/app";

// Add the Firebase products that you want to use
import "firebase/auth";
import "firebase/database";

// PUT YOUR OWN FIREBASE CONFIGURATION HERE
var firebaseConfig = {
    apiKey: "xxxxx-xxxxxxxxxxx-xxxxxx",
    authDomain: "xxxxx-xxxxxxxxxxx-xxxxxx",
    databaseURL: "xxxxx-xxxxxxxxxxx-xxxxxx",
    projectId: "xxxxx-xxxxxxxxxxx-xxxxxx",
    storageBucket: "xxxxx-xxxxxxxxxxx-xxxxxx",
    messagingSenderId: "xxxxx-xxxxxxxxxxx-xxxxxx",
    appId: "xxxxx-xxxxxxxxxxx-xxxxxx",
    measurementId: "xxxxx-xxxxxxxxxxx-xxxxxx"
};
// Initialize Firebase
let firebaseApp = firebase.initializeApp(firebaseConfig);
let firebaseAuth = firebaseApp.auth()
let firebaseDb = firebaseApp.database()

export { firebaseAuth, firebaseDb }
