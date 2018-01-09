var config = {
    apiKey: "AIzaSyCoOz2yyO2jD1-EtjZVGMAqhRACS9Vp35o",
    authDomain: "oopp-project.firebaseapp.com",
    databaseURL: "https://oopp-project.firebaseio.com",
    projectId: "oopp-project",
    storageBucket: "oopp-project.appspot.com",
    messagingSenderId: "943341036937"
};
firebase.initializeApp(config);

//reference username collection
var messagesRef = firebase.database().ref('messages');
// var passRef = firebase.database().ref('password');


document.getElementById('medicine').addEventListener('submit',medicine);

function medicine(e) {
    e.preventDefault();

    //Get values
    var meds = getInputVal('meds');
    var amt = getInputVal('amt');
    saveDetail(meds,amt);

    // show alert
    document.querySelector('.alert').style.display = 'block';
    //hide the alert after 3 sec
    setTimeout(function () {
        document.querySelector('.alert').style.display = 'none';
    }, 3000)
    // to clear out the thing after you submit
    document.getElementById('medicine').reset();
}
function getInputVal(id){
    return document.getElementById(id).value;

}
//save
function saveDetail(meds, amt) {
    messagesRef.push({
        'meds' : meds,
        'amt' : amt
    })
}
