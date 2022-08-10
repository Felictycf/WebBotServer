pip3 install django
pip3 install mysqlclinet
这里去数据库创建一个tst的库
python manage.py migrate
python manage.py makemigrations
启动服务器
 python manage.py runserver
# 启动报错用这个
python -m pip install django-cors-headers