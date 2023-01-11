window.addEventListener('load', function() {
    let buttonRegister= $('#add-modal-register-answer-btn');
    let registerEmailYesNoChoice = $('#registerModal');
    buttonRegister.on('click', function(evt) {
        registerEmailYesNoChoice[0].style.display = "block";
    });

    let buttonRegisterLeft= $('#add-modal-register-answer-btn-left');
    buttonRegisterLeft.on('click', function(evt) {
        registerEmailYesNoChoice[0].style.display = "block";
    });



    let buttonRegisterModalOpenYes= $('#register-yes-modal-form');
    let modalFormYes = $('#registerModalFormYes');
    buttonRegisterModalOpenYes.on('click', function(evt) {
        registerEmailYesNoChoice[0].style.display = "none";
    });

});
