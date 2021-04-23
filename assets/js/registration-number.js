let p = document.querySelector('p');
let phoneNumberGlobal = ""
jQuery("#phone_number").val(localStorage.getItem('phoneNumberLS'));

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
        url: '/validate-number/',
        data: {
            'phone_number': phoneNumber
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                alert("Пользователь с таким номером уже существует");
                document.getElementById("disable_button").disabled = true;
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
        console.log(error)
    });
}


sendConfirmCode = () => {
    const code = document.getElementById("input_code").value;
    window.confirmationResult.confirm(code).then((result) => {
        const user = result.user;
        localStorage.setItem('phoneNumberLS', user.phoneNumber)
        window.location.href = "/registration/"
    }).catch((error) => {
        console.log(error)
        alert('Неправильный код')
    });
};
