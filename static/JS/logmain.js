var config = {
    apiKey: "AIzaSyA5134h-5NxqgwCjL6B2iVrWTDr6o_YP3M",
    authDomain: "stop-78245.firebaseapp.com",
    databaseURL: "https://stop-78245.firebaseio.com",
    projectId: "stop-78245",
    storageBucket: "stop-78245.appspot.com",
    messagingSenderId: "210152465471"
  };
firebase.initializeApp(config);

//reference username collection
var messagesRef = firebase.database().ref('messages');
// var passRef = firebase.database().ref('password');


document.getElementById('registerform').addEventListener('submit',registerform);

function registerform(e) {
    e.preventDefault();

    //Get values
    var username = getInputVal('username');
    var password = getInputVal('password');
    saveDetail(username,password);

    // show alert
    document.querySelector('.alert').style.display = 'block';
    //hide the alert after 3 sec
    setTimeout(function () {
        document.querySelector('.alert').style.display = 'none';
    }, 3000)
    // to clear out the thing after you submit
    document.getElementById('afterstaffloginform').reset();
}
function getInputVal(id){
    return document.getElementById(id).value;

}
//save
function saveDetail(username, password) {
    messagesRef.push({
        'username' : username,
        'password' : password
    })
}
