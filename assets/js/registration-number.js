console.log("hello")

window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier('sign-in-button', {
    'size': 'invisible',
    'callback': (response) => {
        // reCAPTCHA solved, allow signInWithPhoneNumber.
        onSignInSubmit();
    }
});

function validateNumber() {
    let countryCode = document.getElementsByClassName("iti__selected-dial-code")[0].innerText;
    let inputNumber = document.getElementsByClassName("form__input form__input-tel").item(0).value;
    let phoneNumber = countryCode + " " + inputNumber
    let phone_number = document.getElementsByClassName('form__input form__input-tel').item(0).value = phoneNumber.replace(/\s+/g, "")
    $.ajax({
        url: '/validate-number/',
        data: {
            'phone_number': phone_number
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                alert("Пользователь с таким номером уже существует");
            }else{
                console.log('pre')
                const phoneNumber = phone_number;
                console.log(phone_number)
                const appVerifier = window.recaptchaVerifier;
                console.log('recaptcha')
                firebase.auth().signInWithPhoneNumber(phoneNumber, appVerifier)
                    .then((confirmationResult) => {
                        // SMS sent. Prompt user to type the code from the message, then sign the
                        // user in with confirmationResult.confirm(code).
                        window.confirmationResult = confirmationResult;
                        window.location.href = '/registration-submit/'
                        console.log('sent')
                    }).catch((error) => {
                    // Error; SMS not sent
                    console.log(error)
                });
            }
        }
    });
    return phone_number
}

function sendConfirmCode() {
    const code = getCodeFromUserInput();
    confirmationResult.confirm(code).then((result) => {
        // User signed in successfully.
        const user = result.user;
        // ...
    }).catch((error) => {
        // User couldn't sign in (bad verification code?)
        // ...
    });
}