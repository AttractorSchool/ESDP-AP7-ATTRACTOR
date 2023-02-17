window.addEventListener('load', function() {

    let addStudentBtn= $('#addStudentBtn');
    let rateCreateModal = $('#rateCreateModal');

    $('.btn-success').each(function() {
        $(this).on('click', function() {

        // здесь можно получить атрибут каждой кнопки
        const member_id = $(this).attr('data-member_id');
        const event_id = $(this).attr('data-event_id');
        $("#id_comment").val("");

        rateCreateModal[0].style.display = "block";
        $('#btnRateCreate').attr('data-member_id', member_id);
        $('#btnRateCreate').attr('data-event_id', event_id);
        $(".nice-select").attr('data-member_id', member_id);
        $('textarea[name="comment"]').attr('data-member_id', member_id);

            $('#btnClose').on('click', function(evt) {
                rateCreateModal[0].style.display = "none";
            })

            $('#btnRateCreate').on('click', function(evt) {

                    $.ajax({
                        type: 'POST',
                        url : `http://localhost:8000/ratings/create/event_member/${member_id}/event/${event_id}`,
                        data: {
                            score: $('.nice-select.form-select[data-member_id="' + member_id + '"] .list .selected').attr('data-value'),
                            // score: $('.nice-select .list .selected').attr('data-value'),
                            comment: $('textarea[data-member_id="' + member_id + '"]').val(),
                            // comment: $('textarea[name="comment"]').val(),
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                        },

                        error: function(data) {
                            rateCreateModal[0].style.display = "none";
                            // alert('Не получилось')
                    },

                    }).done(
                        function(data) {
                            $("#id_comment").val("");

                            // const tdElements = document.querySelectorAll("td");
                            //     tdElements.forEach((tdElement) => {
                            //       if ($(tdElement).data("id") === member_id) {
                            //         $(tdElement).html(data.rate);
                            //         return;
                            //       }
                            //     });

                            // const targetTdElement = $("td").filter(function() {
                            //       if ($(this).data("id") == member_id) {
                            //         $(this).text(data.rate);
                            //       }
                            //     });

                            // $('td[data-id="+ member_id +"]').html(data.rate);
                            $('#member_' + member_id).html(data.rate);
                            // $('#member_' + member_id).text(data.rate)
                            rateCreateModal[0].style.display = "none";

                        },



                    )
             });

        });
    });
});
