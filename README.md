# VK spy bot
Бот, который поможет вам отслеживать статус пользователя во ВКонтакте. Он не идеальный, но рабочий 🙃
*****
## Настройка бота: ##
1. Убедитесь, что на вашем компьютере установлена актуальная версия Python, если нет, скачайте его на [официальном сайте](python.org)
2. Скачайте необходимые библиотеки:
    * Откройте консоль и вставьте туда команду, написанную ниже, если у вас Windows
    ```
    pip install requests bs4 telebot
    ```
    или эту, если у вас MacOS
    ```
    pip3 install requests bs4 telebot
    ```
    * Дождитесь окончания загрузки и закройте консоль
3. Получить токен вашего бота Telegram
    * Отправить [Bot Father'у](https://t.me/BotFather) команду /start
    * Отправить ему команду /newbot, чтобы перейти к созданию нового бота
    * Придумать боту имя (не никнейм)
    * Придумать никнейм для бота. Обратите внимание, что никнейм бота должен заканчиваться на -bot. Например, firtsbot, DrLivseyBot
    * BotFather пришлёт вам токен бота в формате 1234567890:ABCDEFG-HIJKLMNOPQRSTUVWXYZABCDEFGH
    * Скопировать токен бота и вставить его в соответствующее поле файла config.py
    ```python
    TOKEN = "вставьте свой токен сюда"
    ```
4. Получить ваш ID в телеграм
    * После того, как вы вставили токен в файл config.py, запустите файл getID.py
    * Пока файл работает, отправьте вашему боту команду /start для начала работы
    * Бот, в ответ на вашу команду отправит ваш личный ID
    * Скопируйте ID и вставьте его в соответствующее поле файла config.py
    ```python
    ID = "вставьте свой ID сюда"
    ```
    * Теперь можно остановить работу файла getID.py, он больше не понадобится
***
## Использование бота: ##
1. Запустите основной файл bot.py
2. Перейдите в телеграм и ещё раз отправьте боту команду /start для получения дополнительной инструкции. Примечание: инструкцию можно получить всегда, отправив команду /help
3. Отправьте боту ID человека во ВКонтакте, за статусом которого вы бы хотели следить. ID должен быть вида id1, id123456, ohhithere, medwu
4. Теперь, пока вы не остановите работу скрипта, бот будет просматривать 2 раза в минуту изменение статуса онлайн и оффлайн, если он изменится, вы получите сообщение от бота прямо в телеграм
***
### Если вам понравился скрипт, пожалуйста, оцените его :> ###
Если вы нашли баг/ошибку, пожалуйста, сообщите
