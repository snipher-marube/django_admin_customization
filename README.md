# Django Admin Site Customization

## What is this?

This is a Django project that demonstrates how to customize the Django admin site.


## What is the Django admin site?

The Django admin site is a built-in Django app that allows you to create, read, update, and delete (CRUD) records in your database. It is a great tool for managing your database, but it is not meant to be used as a public-facing website. It is meant to be used by site administrators only.

## Why customize the Django admin site?

The Django admin site is a great tool for managing your database, but it is not meant to be used as a public-facing website. It is meant to be used by site administrators only. If you want to use the Django admin site as a public-facing website, you will need to customize it to make it look more like a public-facing website.



## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment:

    ```sh
    $ python3.11 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

1. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

1. Create a superuser and populate the database:

    ```sh
    (venv)$ python manage.py createsuperuser
    (venv)$ python manage.py populate_db
    ```
	
1. Run the development server:

    ```sh
    (venv)$ python manage.py runserver
    ```
    
1. Your Django admin site should be accessible at [http://localhost:8000/secretadmin/](http://localhost:8000/secretadmin/).
