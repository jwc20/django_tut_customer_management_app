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

### Part 3

- In the accounts folder, create a templates folder.
- In the templates folder, create another accounts folder
- Create a dashboard template in the accounts folder.
- Modify the view to render the dashboard template.
- Repeat the steps to create customer and products template.

(Template Inheritance)

- Create a main template where all other templates will inherit from.
- Modify all templates so they inherit from the main template.
- Create a navbar template and include it in the main template.

(Copy/Paste from video)

- Use bootstrap to style navbar (Use cdn link).
  [cdn](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

- Modify navbar template using bootstrap.
- Modify dashboard template.
- Create status template.
- Add styling for status component in the main template.
- Modify products template.
- Modify customer template.

### Part 4

- Create static folder and folders for css, js, and images inside it.
- Create main.css inside css folder.
- Configure settings.py to load static file and import static file main.css in main.html.

- Add logo to images folder.
- Configure settings to load images and import logo file in navbar.html
