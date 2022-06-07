Firebase is a backend as a service
Firebase hosting only hosts static content - maybe like frontend, so cannot host backend

People prefer to use Django cause there is more control and also Firebase might disappear someday right

Django uses Structured data, Firebase uses NoSQL

```js
import { initializeApp } from "firebase/app";  
import { getFirestore } from "firebase/firestore";
  
// TODO: Replace the following with your app's Firebase project configuration  
// See: https://firebase.google.com/docs/web/learn-more#config-object  
const firebaseConfig = {    // ...  
};  
  
// Initialize Firebase  
const app = initializeApp(firebaseConfig);  
  
 
// Initialize Cloud Firestore and get a reference to the service  
const db = getFirestore(app);  

```

```js
useEffect(()=>{
 // this is where the code runs ..
 const unsubscribe=database
    .collection("people")
    .onSnapshot((snapshot)=>
      set People(snapshot.docs.map((doc)=>doc.data()))
   );
  return()=>{
   // this is the cleanup ...
    unsubscribe();
 };
},[]);
```

Remember to cleanup, onsnapshot returns a function