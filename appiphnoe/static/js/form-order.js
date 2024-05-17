/*
Реализация AJAX с помощью асинхронного метода fetch. Современный вариант реализации AJAX.
*/

var sendbtn = document.getElementById("sendbtn");    // выбираем DOM-елемент (кнопку)

// Привязываем к элементу обработчик события "click"
sendbtn.addEventListener("click", function (e) {
    /* Инструкция preventDefault позволяет переопределить стандартное поведение браузера,
    если ее убрать, то браузер по-умолчанию обновит страницу после отправки данных формы */
    e.preventDefault();
    // Получаем данные полей формы
    let fname = document.getElementsByName("firstName")[0].value;
    let lname = document.getElementsByName("lastName")[0].value;
    let phone = document.getElementsByName("phone")[0].value
    let email = document.getElementsByName("email")[0].value
    // Преобразуем полученные данные в JSON
    var formdata = JSON.stringify({ firstname: fname, lastname: lname, phone: phone, email: email });
    
    // Отправляем запрос через fetch (необходимо выставить соответствующий заголовок (headers)!)
    fetch("/api/contactrequest",
    {
        method: "POST",
        body: formdata,
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then( response => {
        // fetch в случае успешной отправки возвращает Promise, содержащий response объект (ответ на запрос)
        // Возвращаем json-объект из response и получаем данные из поля message
        response.json().then(function(data) {
            console.log(data)
            let statfield = document.getElementById("statusfield");
            statfield.textContent = data.message;
            //statfield.textContent.bold();
            alert(data.message);
        });
    })
    .catch( error => {
        alert(error);
        console.error('error:', error);
    });

});





// document.addEventListener("DOMContentLoaded", function() {
//     var submitButton = document.querySelector('.contacts-form button[type="submit"]');
    
//     submitButton.addEventListener("click", function(event) {
//         event.preventDefault(); // Предотвращаем отправку формы
        
//         var firstName = document.querySelector('.contacts-form input[name="firstName"]').value;
//         var lastName = document.querySelector('.contacts-form input[name="lastName"]').value;
        
//         // Ваш код для отображения alert с введенными данными
//         alert(firstName + " " + lastName + ", " + "ваш заказ принят!");
//     });
// });
