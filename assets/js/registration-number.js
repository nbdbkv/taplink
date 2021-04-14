// function getNumber() {
//     let countryCode = document.getElementsByClassName("iti__selected-dial-code")[0].innerText;
//     let inputNumber = document.getElementsByClassName("form__input form__input-tel").item(0).value;
//     let phoneNumber = countryCode + " " + inputNumber
//     document.getElementsByClassName('form__input form__input-tel').item(0).value = phoneNumber.replace(/\s+/g, "")
//     document.getElementsByClassName(".form__btn")
//     alert(phoneNumber)
// }


function getNumber() {
    let countryCode = document.getElementsByClassName("iti__selected-dial-code")[0].innerText;
    let inputNumber = document.getElementsByClassName("form__input form__input-tel").item(0).value;
    let phoneNumber = countryCode + " " + inputNumber
    document.getElementsByClassName('form__input form__input-tel').item(0).value = phoneNumber.replace(/\s+/g, "")
    document.getElementsByClassName(".form__btn")

    $.ajax({
        url: '/validation-number/',
        data: {
            'phone_number': phoneNumber
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                alert("A user with this username already exists.");
            }
        }
    });

}

