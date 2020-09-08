# Проект для тестирования API
Тесты для различных API сервисов: \
https://dog.ceo/dog-api/ \
https://www.openbrewerydb.org/  
https://jsonplaceholder.typicode.com/ 

Прогон тестов можно запустить с помощью pytest при настроенном окружении или 
через Dockerfile:

    docker build -t api/tests .
    docker run api/tests
