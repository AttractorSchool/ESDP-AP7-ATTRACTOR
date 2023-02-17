window.addEventListener('load', function() {

    const commentModal = $('#commentModal');

    $('.btn-success').each(function() {
        $(this).on('click', function() {

        const rate_id = $(this).attr('data-rate_id');

        const rate_comment = $(this).attr('data-rate_comment');

        commentModal[0].style.display = "block";

        $(".comment").html(rate_comment);

        $('#btnClose').on('click', function(evt) {
            commentModal[0].style.display = "none";
        })

        });
    });
});
