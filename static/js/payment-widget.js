window.addEventListener('load', function() {

    $('#orderButton').on('click', function(evt) {
        const payModal = $('#payModal');
        payModal[0].style.display = "block";
    });



    this.pay = function () {

        const id = $('#payButton').attr('data-id');
        const email = $('#user-email').attr('data-email');
        const price = parseInt($('#service-price').attr('data-price'));
        console.log(price)
        console.log(id)
        console.log(email)


     const widget = new cp.CloudPayments();
        widget.pay('auth', // или 'charge'
            { //options
                publicId: 'test_api_00000000000000000000002', //id из личного кабинета //Идентификатор сайта, который находится в ЛК
                description: 'Оплата услуги "ТОП" в enimi.kz', //назначение
                amount: price, //сумма
                currency: 'KZT', //валюта
                accountId: 'user@example.com', //идентификатор плательщика (необязательно)
                invoiceId: id, //номер заказа  (необязательно)
                email: email, //email плательщика (необязательно)
                skin: "mini", //дизайн виджета (необязательно)
                autoClose: 3, //время в секундах до авто-закрытия виджета (необязательный)
            },
            {
                onSuccess: function (options) { // success
                    //действие при успешной оплате
                    const id = $('#payButton').attr('data-id');
                    $.ajax({
                        url: `http://localhost:8000/payments/order_status_update/${id}/`,
                        data: {
                                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                                },
                        type: 'POST',

                    }).done(function(data) {
                        window.location.href = 'http://localhost:8000/payments/orders_list/';
                    })

                },
                onFail: function (reason, options) { // fail
                    //действие при неуспешной оплате
                    window.location.href = 'http://localhost:8000/payments/orders_list/';
                },
                onComplete: function (paymentResult, options) { //Вызывается как только виджет получает от api.cloudpayments ответ с результатом транзакции.
                    //например вызов вашей аналитики Facebook Pixel
                }
            }
        )
    };


    $('#payButton').click(pay);


});