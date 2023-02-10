window.addEventListener('load', function() {

    let addStudentBtn= $('#addStudentBtn');
    let rateCreateModal = $('#rateCreateModal');

    $('.btn-success').each(function() {
        $(this).on('click', function() {

        // здесь можно получить атрибут каждой кнопки
        const member_id = $(this).attr('data-member_id');
        const event_id = $(this).attr('data-event_id');
        console.log(member_id);
        console.log(event_id);

        rateCreateModal[0].style.display = "block";
        $('.btn-success').attr('data-member_id', member_id);
        $('.btn-success').attr('data-event_id', event_id);

            $('#btnClose').on('click', function(evt) {
                rateCreateModal[0].style.display = "none";
            })

            $('#btnRateCreate').on('click', function(evt) {

                    $.ajax({
                        type: 'POST',
                        url : `http://localhost:8000/ratings/create/event_member/${member_id}/event/${event_id}`,
                        data: {
                            score: $('.nice-select .list .selected').attr('data-value'),
                            comment: $('textarea[name="comment"]').val(),
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                        },

                        error: function(data) {
                            rateCreateModal[0].style.display = "none";
                            alert('Не получилось')
                    },

                    }).done(
                        function(data) {
                            rateCreateModal[0].style.display = "none";
                            $("#td").val(data.result)
                        },



                    )
             });

        });
    });
});
