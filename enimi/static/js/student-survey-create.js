window.addEventListener('load', function() {
    let buttonSubjects= $('#subjectsButton');
    let subjectsModal = $('#subjectsModal');
    buttonSubjects.on('click', function(evt) {
        subjectsModal[0].style.display = "block";
    });

    let subjectsCloseButton= $('#subjectsCloseButton');
    subjectsCloseButton.on('click', function(evt) {
        subjectsModal[0].style.display = "none";
    });

    let flexRadioPrograms= $('#flexRadioDefault1');
    let programsModal = $('#programsModal');
    flexRadioPrograms.on('click', function(evt) {
        programsModal[0].style.display = "block";
    });

    let programsCloseButton= $('#programsCloseButton');
    programsCloseButton.on('click', function(evt) {
        programsModal[0].style.display = "none";
    });

    let flexRadioYesTest= $('#flexRadioYesTest');
    let testsModal = $('#testsModal');
    flexRadioYesTest.on('click', function(evt) {
        testsModal[0].style.display = "block";
    });

    let testsCloseButton= $('#testsCloseButton');
    testsCloseButton.on('click', function(evt) {
        testsModal[0].style.display = "none";
    });

    let flexRadioYesOnline= $('#flexRadioYesOnline');
    let onlineModal = $('#onlineModal');
    flexRadioYesOnline.on('click', function(evt) {
        onlineModal[0].style.display = "block";
    });

    let onlineCloseButton= $('#onlineCloseButton');
    onlineCloseButton.on('click', function(evt) {
        onlineModal[0].style.display = "none";
    });

    let flexRadioYesTutor= $('#flexRadioYesTutor');
    let tutorModal = $('#tutorModal');
    flexRadioYesTutor.on('click', function(evt) {
        tutorModal[0].style.display = "block";
    });

    let tutorCloseButton= $('#tutorCloseButton');
    tutorCloseButton.on('click', function(evt) {
        tutorModal[0].style.display = "none";
    });

    let flexRadioYesStudent= $('#flexRadioYesStudent');
    let studentModal = $('#studentModal');
    flexRadioYesStudent.on('click', function(evt) {
        studentModal[0].style.display = "block";
    });

    let studentCloseButton= $('#studentCloseButton');
    studentCloseButton.on('click', function(evt) {
        studentModal[0].style.display = "none";
    });

});
