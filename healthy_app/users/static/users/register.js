document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript loaded successfully");
    $("#register-form-id").on("submit", function(event) {
        event.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            type: "POST",
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
//                    bootstrap.Modal('#ModelRegister', options)
                    $("#ModelRegister").toggle();
                    $("#successModal").modal();
                    $("#successModal").toggle();
                } else {
                    alert("Registration failed: " + JSON.stringify(response.errors));
                }
            },
            error: function() {
                alert("An error occurred. Please try again.");
            }
        });
    });

    $(".close").on("click", function() {
        $(".modal").hide();
    });
});