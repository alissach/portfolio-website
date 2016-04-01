// Mark the active page on the navbar
function activepage() {
    var activepageurl = location.pathname; // get active page url
    console.log("Current page: " + activepageurl);
    if (activepageurl === "/index") {
        document.getElementById("index").className= "active";
    }
    else if (activepageurl === "/") {
        document.getElementById("index").className="active";
    }
    else if (activepageurl === "/projects") {
        document.getElementById("projects").className="active";
    }
    else if (activepageurl === "/blog") {
        document.getElementById("blog").className="active"; 
    }
    else if (activepageurl === "/resume") {
        document.getElementById("resume").className="active";
    }
    else if (activepageurl === "/contact") {
        document.getElementById("contact").className="active";
    }
}

// Lightbox (blog page)
$('.thumbnail').click(function(){
    $('.modal-body').empty("hello");
    var title = $(this).parent('a').attr("title");
    $('.modal-title').html(title);
    $($(this).parents('div').html()).appendTo('.modal-body');
    $('.modal.fade').modal({show:true});
});


// Change jumbotron class to something else (AKA hide jumbotron on index.html page)
function show_jumbotron(){
    var activepageurl = location.pathname; // get active page url
    console.log("activepageurl: " + activepageurl);
    if (activepageurl === "/index") {
        document.getElementById("navigation").className = "classnm";
        document.getElementsByTagName("h1")[0].className= "";
    }
    else if (activepageurl === "/") {
        document.getElementById("navigation").className = "classnm";
        document.getElementsByTagName("h1")[0].className= "";
        console.log("active page url === /");
    }
}

// Calling functions
activepage()
console.log("called activepage")
show_jumbotron()
