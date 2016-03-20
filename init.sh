sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
cd ~/web/ask
gunicorn ask.wsgi:application -b 0.0.0.0:8000 &
#gunicorn -b 0.0.0.0:8080 hello
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart -b 0.0.0.0:8080 hello:app
#gunicorn ask.wsgi:application -b 0.0.0.0:8000 &
#sudo /etc/init.d/mysql start
#mysql -uroot -e "create database qa"
#python manage.py loaddata --app=qa demodata.json
# sudo rm /usr/bin/python
# sudo ln -s /usr/bin/python3.4 /usr/bin/python
# sudo rm /usr/bin/python2.7
# sudo ln -s /usr/bin/python3.4 /usr/bin/python2.7
#сначало init_locale, потом настраиваем базу данных, а потом запускаем сервер
