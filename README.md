Сервис обратной связи (Feedback)

Напишите REST­сервис который обслуживает обращения пользователей в
обратную связь и уведомляет операторов о новыз обращениях. Пример такого
сервиса: раздел “Обратная связь” на любом сайте.

Функции сервиса
1. Обращение в обратную связь для авторизованных пользователей.
2. Обращение в обратную связь для не авторизованных пользователей.
3. Возможность прикрепить файл к обращению.
4. Возможность послать пользователю на email ответ по его вопросу.

Требования для запроса от авторизованного пользователя
● ФИО пользователя, его email, мобильный телефон и другие доступные данные
должны быть заполнены автоматически и прикреплены к отправляемому в
службу поддержки email, возможность их изменить должна быть заблокирована


Требования для запроса от не авторизованного пользователя
● Должна быть возможность приёма и обработки ФИО пользователя, его email,
мобильного телефона и других доступных данных и их прикрепление к
отправляемому в службу поддержки email

Требования к файлу
● Размер файла не должен быть менее 50 Kb
● Размер файла не должен превышать 2Mb
○ Если размер меньше, показываем сообщение: "Размер файла мал для распознавания изображения."
○ Если размер больше, показываем сообщение: "Размер файла превышает максимальный размер (2 мегабайта)"
● Формат файла должен быть один из: JPG, BMP, PNG, TIFF
○ Если формат иной, показываем сообщение: "Некорректный формат файла, поддерживаемые форматы: JPG, BMP, PNG, TIFF"

Требование к реализации
● Можно использовать любой web­framework python
● Можно использовать любое хранилище данных

Требования к передаче решения
● Время на решение тестового задания ­ 1­3 дня
● Результат присылать в виде ссылки на github (или аналоги)