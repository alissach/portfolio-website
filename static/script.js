
function activepage() {
    var activepageurl = location.pathname.slice(1); // get active page url
    console.log("Current page: " + activepageurl);
    if (activepageurl == "home") {
        document.getElementById("home").className= "active";
    }
    else if (activepageurl == "aboutme") {
        document.getElementById("aboutme").className="active";
    }
    else if (activepageurl == "blog") {
        document.getElementById("blog").className="active"; 
    }
    else if (activepageurl == "login") {
        document.getElementById("login").className="active";
    }
}

// Calling functions
activepage()
