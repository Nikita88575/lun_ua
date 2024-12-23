(function($) {
    $(function(){

        $('.sidenav').sidenav();
        $('.parallax').parallax();
    });
})(jQuery);

let messageBlock = document.getElementById("notification-messages");
if (messageBlock) {
    messageBlock.style.visibility = "visible";
    setTimeout(function () {
        messageBlock.classList.add("hidden");
        setTimeout(function () {
            messageBlock.style.visibility = "hidden";
            messageBlock.classList.remove("hidden");
        }, 3000);
    }, 3000);
}