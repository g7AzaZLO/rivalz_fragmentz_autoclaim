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
### Прописываем кошельки
Необходимо в файл wallets.txt прописать приватные ключи ваших кошельков, на которые собираетесь клеймить</br>
Каждый приватник на новой строке</br>
Открыть файл можно текстовым редактором нано</br>
<code>nano wallets.txt</code></br>
### Запускаем скрипт
<code>python app.py</code></br>

ВАЖНО!!!</br>
Не забывайте время от времени пополнять свой кошелек токенами из крана, чтобы был газ для транзакций</br>
https://rivalz2.hub.caldera.xyz/ - кран</br>
Перерыв между пачками клеймов = 12-12.5 часов</br>
Перерыв между самими клеймами от 5 до 15 секунд</br>

Чтобы выйти из screen сесcии и не прервать работу скрипта. Жмем ctrl+a, после чего D</br>
Чтобы зайти в screen сессию с сриптом <code>screen -r rivalz_auto_claim</code>

https://t.me/g7monitor - группа G7</br>
https://t.me/g7team_chat - чат G7</br>
