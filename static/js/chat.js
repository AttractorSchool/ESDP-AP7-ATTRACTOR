

$(document).ready(function() {
    $('.chat').on('click', function(e) {
    let pk_response = e.target.id;
    console.log("HHHHHHРРРРРРРРРРРРРРРРРРРРРРРРРРР")
    console.log(pk_response)
         console.log("AAAAHHHHHHРРРРРРРРРРРРРРРРРРРРРРРРРРР")

    fetch(`/cabinet_tutors/1/tutor-on-students-responses/chat_messages/${pk_response}/`)
    .then((response) => {
        return response.text();

    })
    .then((data) => {
        console.log(data)
        obj = document.getElementById('message-modal-body');
        obj.innerHTML = data
    });

    })
    })

