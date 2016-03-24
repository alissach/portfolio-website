
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

activepage()


// document.mouseover

// Super Easy Sticky Footer code from: https://github.com/mazer-rakham/superEasyStickyFooter/blob/master/superEasySticky_Footer.js
// function superEasySticky_Footer(SE_windowHeight, SE_space) {
//     $(document).ready(function() {
//         var windowHeight = $(document).height();
//         var footerHeight = $('footer').height();
//         if(SE_windowHeight === undefined) {
//             SE_windowHeight = 50;
//         }
//         if(SE_space === undefined) {
//             SE_space = 20;
//         }
//         $('body, html').css('height', windowHeight - SE_windowHeight);
//         $('body').wrapInner("<div id='#main_wrapping_div' style='min-height:100%; position:relative;'></div>").find('div').css({'padding-bottom' : footerHeight + SE_space});
//         $('footer').css({
//             'position' : 'absolute',
//             'bottom' : 0,
//             'left' : 0,
//             'right' : 0,
//             'height' : 'auto',
//             'display': 'block'
//         });
//     });
// }

// superEasySticky_Footer(15, 175)
//End of sticky footer code