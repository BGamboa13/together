$(document).ready(function () {
    // Toggle mobile menu visibility
    $(".lg\\:hidden button").on("click", function () {
        $("div[role='dialog']").toggleClass("translate-x-full");
        $("div[aria-modal='true']").toggleClass("hidden");
    });

    // Close mobile menu when close button is clicked
    $(".lg\\:hidden button[aria-hidden='true']").on("click", function () {
        $("div[role='dialog']").toggleClass("translate-x-full");
        $("div[aria-modal='true']").toggleClass("hidden");
    });
});


