# Установка авто-клейма фрагментов Rivalz
### Обновляем пакеты
<code>apt-get update -y; apt upgrade -y</code>
### Устанавливаем утилиту screen
<code>sudo apt-get install screen</code>
### Открывает screen-сессию
<code>screen -S rivalz_auto_claim</code>
### Качаем скрипт
<code>git clone https://github.com/g7AzaZLO/rivalz_fragmentz_autoclaim.git</code>
### Заходим в папку с скриптом
<code>cd rivalz_fragmentz_autoclaim</code>
### Качаем и устанавливаем Python
<code>add-apt-repository -y ppa:deadsnakes/ppa</code></br>
<code>apt-get install python3.12 -y</code></br>
<code>apt install python3-pip -y</code></br>
### Устанавливаем зависимости
<code>pip install -r requirements.txt</code>
### Запускаем скрипт
<code>python app.py</code></br>
![image](https://github.com/user-attachments/assets/4c8f11ea-62a9-487c-bacd-6f4bec423f90)

# Что умеет:
1. Клеймить на ваш кошелек(необходимо вводить сид-фразу)</br>
2. Клеймить на ново-созданный кошелек</br>
ВАЖНО!!!</br>
Не забывайте время от времени пополнять свой кошелек токенами из крана, чтобы был газ для транзакций</br>
Перерыв между пачками клеймов = 12 часов 1 минута</br>
Перерыв между самими клеймами от 5 до 15 секунд

### https://t.me/g7monitor - группа
### https://t.me/g7team_chat - чат
