$(document).on("click", ".navbar-burger", () => {
    let burger = $('.burger');
    let menu = $('.navbar-menu');
    burger.toggleClass('is-active');
    menu.toggleClass('is-active');
})

$(document).on("click", ".btn-register", () => {
    $.ajax({
        url: '/v1/register',
        type: 'POST',
        data: {
            name: $("[name='name']").val(),
            surname: $("[name='surname']").val(),
            user_email: $("[name='user_email']").val(),
            password: $("[name='user_password']").val()
        }
    })
})

$(document).on("click", ".btn-login", () => {
    $.ajax({
        url: '/v1/login',
        type: 'POST',
        data: {
            user_email: $("[name='user_email']").val(),
            password: $("[name='user_password']").val()
        },
        dataType: 'json',
        success: (resp) => {
            if(resp.data) {
                window.location.href = '/me'
            }
        }
    })
})