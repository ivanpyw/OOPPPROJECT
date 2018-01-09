function myFunction(e) {
//   if (confirm("Are you sure you want to tend to this patient?") == true) {
//
//     if (confirm("Double confirm?")== true)
//       if (e.style.backgroundColor == "white")
//         e.style.backgroundColor = "yellow";
//       else if (e.style.backgroundColor == "yellow")
//         e.style.backgroundColor = "red";
//       else if (e.style.backgroundColor == "red")
//         e.style.backgroundColor = "white";
//       else
//         e.style.backgroundColor = "white";
//
//   } else {
//     txt = "You pressed Cancel!";
//   }
//
//
// }
    if (e.style.backgroundColor=="red"){
      if(confirm("Are you sure you want to tend to this patient?")== true)
        if (confirm("Double confirm?") == true)
          e.style.backgroundColor = "yellow";
    }
    else if (e.style.backgroundColor =="yellow") {
      if(confirm("Have you assisted the patient?")== true)
        if (confirm("Double confirm?")==true)
          e.style.backgroundColor ="white";
    }
    else if (e.style.backgroundColor =="white"){
      e.style.backgroundColor = "red"
    }
}




var blocks = document.getElementsByClassName("foo");
for (i = 0; i < blocks.length; i++) {
  blocks[i].addEventListener("click", function() {
    myFunction(this);
  });
}