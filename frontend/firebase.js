// firebase.js

import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDlWlkpsmqdDJv5hlilZO5cRyd3dyar-Vs",
  authDomain: "allergycheck-b48a9.firebaseapp.com",
  projectId: "allergycheck-b48a9",
  storageBucket: "allergycheck-b48a9.appspot.com",
  messagingSenderId: "1087274816798",
  appId: "1:1087274816798:web:92c5bcac40478e69af250f"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth };
