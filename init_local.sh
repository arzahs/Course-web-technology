sudo apt-get update
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3.4 /usr/bin/python
sudo rm /usr/bin/python2.7
sudo ln -s /usr/bin/python3.4 /usr/bin/python2.7
sudo pip3 install django
sudo pip3 install mysqlclient
sudo pip3 install pymysql
