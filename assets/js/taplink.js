function copytext(el) {
    var $tmp = $("<textarea>");
    $("body").append($tmp);
    $tmp.val($(el).text()).select();
    document.execCommand("copy");
    $tmp.remove();
}

$('.copy__icon').on('click', function () {
    copytext('#taplink-link');
    $('.taplink__copy').addClass('active');
    setTimeout(function () {
        $('.taplink__copy').removeClass('active');
    }, 3000);
})

setText = () => {
    $("#set_text").val($(".ql-editor")[0].innerHTML)
    $('#submit-text').click()
};

setWhatsApp = () => {
    let countryCode = $(".iti__selected-dial-code")[0].innerHTML
    let inputNumber = $("#set_whatsapp").val();
    if (inputNumber == "") {
        countryCode = ""
    } else {
        $("#set_whatsapp").val((countryCode + inputNumber).replace(/[^0-9\.]+/g, ""))
    }
    $('#submit-messenger').click()
}

