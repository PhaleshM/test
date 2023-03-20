## Django REST Framework Complete Authentication API
### Video Link:- https://youtu.be/lo7lBD9ynVc

## To Run this Project follow below:

```bash
mkvirtualenv authenv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### There is a File "DjangoAuthAPI.postman_collection" which has Postman Collection You can import this file in your postman to test this API


```
<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBXo_BrI5MytD-3XDlqVxGr1TYXa27ez5w",
    authDomain: "hack-882f8.firebaseapp.com",
    projectId: "hack-882f8",
    storageBucket: "hack-882f8.appspot.com",
    messagingSenderId: "1031213559260",
    appId: "1:1031213559260:web:8aef94aea7c32160ccb319",
    measurementId: "G-8PBEQJ0E31"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>
```