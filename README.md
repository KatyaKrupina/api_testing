# Проект для тестирования API
Тесты для различных API сервисов: \
https://dog.ceo/dog-api/ \
https://www.openbrewerydb.org/  
https://jsonplaceholder.typicode.com/ 

Запуск тестов:

    docker build -t api/tests .
    docker run --rm --name test_run api/tests
