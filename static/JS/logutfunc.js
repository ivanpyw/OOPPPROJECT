document
    .getElementById("logoutf")
    .addEventListener("click", function( e ){ //e => event

       if (confirm('Are you sure to logout?') == true)
            {
                // They clicked Yes
                return window.location = '/index/';

            }
       else
            {
                // They clicked no
                return false;
            }
    });