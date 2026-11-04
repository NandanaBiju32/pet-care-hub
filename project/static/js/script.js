

let buyButtons =
    document.querySelectorAll(".buy-btn");

buyButtons.forEach(button => {

    button.addEventListener("click", () => {

        alert("Redirecting To Payment Page");

    });

});

