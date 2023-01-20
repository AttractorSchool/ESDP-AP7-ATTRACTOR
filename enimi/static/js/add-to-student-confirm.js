window.addEventListener('load', function() {

    let addStudentBtn= $('#addStudentBtn');
    let addToStudentConfirmModal = $('#addToStudentConfirmModal');

    $('.btn-success').each(function() {
        $(this).on('click', function() {
            console.log('asdasdasd')
        // здесь можно получить атрибут каждой кнопки
        const id = $(this).attr('data-id');
        console.log(id)
        addToStudentConfirmModal[0].style.display = "block";
        $('.btn-success').attr('data-id', id);
        let url = `cabinet_tutors/add_user_to_my_students/${id}/`;
        console.log(url)


            $('#addStudentBtnConfirmCancel').on('click', function(evt) {
                   addToStudentConfirmModal[0].style.display = "none";
             });

            $('#addStudentBtnConfirm').on('click', function(evt) {
                    $.ajax({
                        type: 'GET',
                        url : `http://localhost:8000/cabinet_tutors/add_user_to_my_students/${id}/`,
                        data: {
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                        },

                        error: function(data) {
                            addToStudentConfirmModal[0].style.display = "none";
                            alert('Пользователь ранее был добавлен в ученики!')


                    },

                    }).done(
                        function(data) {
                            addToStudentConfirmModal[0].style.display = "none";
                            alert('Пользователь добавлен в ученики!')
                        },



                    )
             });

        });
    });
});
