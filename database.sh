sudo /etc/init.d/mysql start
mysql -uroot -e "create database qa"
python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate
