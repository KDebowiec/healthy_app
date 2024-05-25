//document.addEventListener("DOMContentLoaded", function() {
//    var registerForm = document.getElementById("register-form-id");
//    registerForm.addEventListener("submit", function(event) {
//        event.preventDefault();
//
//        var modal = document.getElementById("ModelRegister");
//
//        var closeModal = function() {
//            modal.style.display = "none";
//        };
//
//        var showSuccessModal = function() {
//        var successModal = document.getElementById("successModal");
//        successModal.style.display = "block";
//        };
//
//        if (registerForm.checkValidity()) {
//            closeModal();
//            showSuccessModal();
//        }
//    });
//});

document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript loaded successfully");
    $("#register-form-id").on("submit", function(event) {
        event.preventDefault();

        $.ajax({
            url: "/ajax/register/",
            type: "POST",
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    $("#ModelRegister").hide();
                    $("#successModal").show();
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