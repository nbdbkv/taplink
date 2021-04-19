const p = document.querySelector('p');
let userPhoneNumberGlobal = ""

window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier("sign-in-button", {
    'size': 'invisible',
    'callback': (response) => {
        onSignInSubmit();
    }
});

let appVerifier = window.recaptchaVerifier;

validateNumber = () => {
    let countryCode = document.getElementsByClassName("iti__selected-dial-code")[0].innerHTML;
    let inputNumber = document.getElementsByClassName("form__input form__input-tel").item(0).value;
    let formNumber = countryCode + inputNumber
    let phoneNumber = formNumber.replace(/\s+/g, "")
    userPhoneNumberGlobal = phoneNumber
    $.ajax({
        url: '/validate-number/',
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
    firebase.auth().signInWithPhoneNumber(userPhoneNumberGlobal, appVerifier).then((confirmationResult) => {
        window.confirmationResult = confirmationResult;
        document.getElementById("number").style.display="none";
        document.getElementById("submit").style.display="block";
        p.textContent = userPhoneNumberGlobal.replace(/(\d)(?=(\d{3})+$)/g, '$1 ');
    }).catch((error) => {
        console.log(error)
    });
}


sendConfirmCode = () => {
    const code = document.getElementsByClassName("form__input").item(1).value;
    window.confirmationResult.confirm(code).then((result) => {
        const user = result.user;
        window.location.href = "/registration/"
    }).catch((error) => {
        console.log(error)
    });
};
