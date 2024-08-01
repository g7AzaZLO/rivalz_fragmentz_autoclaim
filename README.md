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
<code>python app.py</code>
