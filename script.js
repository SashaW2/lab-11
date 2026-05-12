document
    .getElementById("feedbackForm")
    .addEventListener("submit", function(e) {

    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    const message = document.getElementById("message");

    if(name === "" || email === "") {
        message.textContent = "Заполните все поля";
        return;
    }

    message.textContent = "Форма успешно отправлена";
});