document.addEventListener("DOMContentLoaded", function() {
    var paragraphs = document.querySelectorAll(".news-text p");
    var title = document.querySelector(".news-title");

    // Функция для изменения цвета текста и фона заголовка
    function changeTitleStyle(textColor, backgroundColor) {
        title.style.color = textColor;
        title.style.backgroundColor = backgroundColor;
    }

    // Скрываем текст внутри <p> при загрузке страницы
    paragraphs.forEach(function(paragraph) {
        paragraph.style.display = "none";
    });

    // Добавляем обработчик события для разворачивания/сворачивания текста при клике на заголовок h2
    title.addEventListener("click", function() {
        paragraphs.forEach(function(paragraph) {
            paragraph.style.display = (paragraph.style.display === "none") ? "block" : "none";
        });

        // Изменяем цвет текста и фона заголовка при открытии
        if (title.style.backgroundColor !== "gray") {
            changeTitleStyle("white", "gray");
        } else {
            // Возвращаем исходные стили при закрытии
            changeTitleStyle("black", "transparent");
        }
    });

    // Добавляем обработчик события для закрытия текста при двойном клике на заголовок h2
    title.addEventListener("dblclick", function(event) {
        event.stopPropagation();
        paragraphs.forEach(function(paragraph) {
            paragraph.style.display = "none";
        });

        // Возвращаем исходные стили при закрытии
        changeTitleStyle("black", "transparent");
    });
});



const image = document.querySelector('.images-news');

    image.addEventListener('mouseover', () => {
        image.style.transform = 'scale(1.05)';
    });

    image.addEventListener('mouseout', () => {
        image.style.transform = 'scale(1)';
    });