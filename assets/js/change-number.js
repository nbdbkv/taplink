let p = document.querySelector('p');
let phoneNumberGlobal = ""

window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier("sign-in-button", {
    'size': 'invisible',
    'callback': (response) => {
        onSignInSubmit();
    }
});

let appVerifier = window.recaptchaVerifier;

validateNumber = () => {
    let countryCode = document.getElementsByClassName("iti__selected-dial-code")[0].innerHTML;
    let inputNumber = document.getElementById("input_number").value;
    let formNumber = countryCode + inputNumber
    let phoneNumber = formNumber.replace(/\s+/g, "")
    phoneNumberGlobal = phoneNumber
    $.ajax({
        url: $("#number").attr("data-url"),
        data: {
            'phone_number': phoneNumber
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                alert("Пользователь с таким номером уже существует");
            } else {
                getConfirmCode()
            }
        }
    });
}


getConfirmCode = () => {
    firebase.auth().signInWithPhoneNumber(phoneNumberGlobal, appVerifier).then((confirmationResult) => {
        window.confirmationResult = confirmationResult;
        document.getElementById("number").style.display="none";
        document.getElementById("submit").style.display="block";
        p.textContent = phoneNumberGlobal.replace(/(\d)(?=(\d{3})+$)/g, '$1 ');
    }).catch((error) => {
        grecaptcha.reset(window.recaptchaWidgetId);

        // Or, if you haven't stored the widget ID:
        window.recaptchaVerifier.render().then(function(widgetId) {
            grecaptcha.reset(widgetId);
        });
    });
}


sendConfirmCode = () => {
    const code = document.getElementById("input_code").value;
    window.confirmationResult.confirm(code).then((result) => {
        const user = result.user;
        jQuery("#phone_number").val(phoneNumberGlobal);
        document.getElementById('submit-button').click()
    }).catch((error) => {
        alert('Неправильный код')
    });
};
