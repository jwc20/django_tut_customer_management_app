# django_tut_customer_management_app

[Tutorial](https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)

### Part 1

```
python3 -m venv venv
. ./venv/bin/activate.fish

pip3 install django

django-admin startproject crm1
cd crm1
python3 manage.py runserver

python3 manage.py startapp accounts
```

### Part 2

- Create views for home, product, and customers for the accounts app.
- Create the urls in the accounts app.
- Connect the urls from the crm1 project to the accounts app.
