$(function() {
    var formContainer = $("#add_notice"),
        formLaunchTrigger = $("#add-notification");

    formLaunchTrigger.click(function(event) {
        event.preventDefault();
        formContainer.simplebox();
    });
});
