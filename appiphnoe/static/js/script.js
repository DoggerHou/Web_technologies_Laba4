document.addEventListener("DOMContentLoaded", function() {
    // Получаем ссылки на элементы навигационного меню
    var menuLinks = document.querySelectorAll(".menu-link, .phone");

    // Проходимся по каждой ссылке меню
    menuLinks.forEach(function(link) {
        // Добавляем обработчики событий для наведения и ухода мыши
        link.addEventListener("mouseover", function() {
            this.style.color = "white"; // Устанавливаем белый цвет текста при наведении
        });

        link.addEventListener("mouseout", function() {
            // Проверяем, является ли текущая страница страницей, связанной с данной ссылкой
            if (!isCurrentPage(link)) {
                this.style.color = ""; // Возвращаем изначальный цвет текста при уходе мыши, если не находимся на этой странице
            }
        });

        // Проверяем, является ли текущая страница страницей, связанной с данной ссылкой
        if (isCurrentPage(link)) {
            link.style.color = "white"; // Выделяем текущий элемент, если текущая страница совпадает с этой ссылкой
        }
    });

    // Функция для проверки соответствия текущей страницы ссылке
    function isCurrentPage(link) {
        var currentPageURL = window.location.href;
        var linkURL = link.href;
        
        // Учитываем случай, когда ссылка содержит #, но не считаем это частью пути
        if (linkURL.includes("#") && !currentPageURL.includes("#")) {
            linkURL = linkURL.split("#")[0];
        }
        
        return currentPageURL.startsWith(linkURL);
    }
});
