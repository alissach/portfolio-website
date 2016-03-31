// Mark the active page on the navbar
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


// Lightbox (blog page)
$('.thumbnail').click(function(){
    $('.modal-body').empty("hello");
    var title = $(this).parent('a').attr("title");
    $('.modal-title').html(title);
    $($(this).parents('div').html()).appendTo('.modal-body');
    $('.modal.fade').modal({show:true});
});


// Calling all functions
activepage()
