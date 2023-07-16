# Project Setup & Database Setup

Here's a step-by-step guide to setting up your Django project:

1) **Install Django**: Begin by installing the Django framework. We'll use a version less than 4, which can be installed with the following command:
```bash
pip3 install 'django<4'
```

2) **Create a Django Project**: Next, create a new Django project. In this case, we'll name it 'django-todo'. Django provides a command for this purpose:
```bash
django-admin startproject django-todo .
```

Upon executing these commands and exploring your file system, you'll observe two new items: `Django_todo` and `manage.py`. These are integral to our project structure:

- **Django_todo**: This is the main project directory.
- **manage.py**: This is an essential command-line utility that we'll use throughout the project.

Within the `Django_todo` directory, you'll discover an `__init__.py` file. This file, automatically created by Django, indicates that this directory should be treated as a package, thus making its modules importable.

Additionally, the folder contains three vital files:

- **settings.py**: This file maintains the global settings for our Django project. Here, you'll specify configurations such as debug mode, the location of HTML templates, and database connection details.

- **urls.py**: This file manages the routing of our application, allowing users to navigate to specific Python functions by entering a particular URL. This is akin to Flask's `app.route` functionality.

- **wsgi.py**: This file facilitates the communication between our web server and Python application. It's a crucial part of the web serving pipeline, enabling the delivery of our application to users.


## ENVIROMENT VARIABLES

Ensure that you have a `.gitignore` file that includes all files and folders that should be ignored by GitHub, such as an `env.py` file. These variables need to be system-wide for our application, so the operating system must be imported.

Setting up default environment variables requires two arguments, the key and the value, both enclosed in quotes. For this project, we need six different variables, so replicate that line six times.

The six variables are as follows:

- **IP**: Set this to `0.0.0.0`
- **PORT**: Set this to `5000` for Flask applications.
- **SECRET_KEY**: This can be any random string you choose.
- **DEBUG**: Set this to `True` for now. However, ensure that you change DEBUG to `False` before submitting your actual project.
- **DEVELOPMENT**: Also set this to `True` for now. We'll use this to differentiate between our local environment and our deployed application later.
- **DB_URL**: This will point to our database, which we don't have yet. But when working locally, we'll use the local Postgres environment. The three slashes signify that our database is local within our workspace. We'll create a new database named `taskmanager`.

## APPS in Django

Django, a high-level Python web framework, organizes its projects into small components known as **apps**. An app can be thought of as a reusable, self-contained collection of code, capable of being utilized across multiple projects to expedite the development process.

For instance, if your project requires an authentication system that handles user login, logout, and password resets, you don't have to build it from scratch. Instead, you can use a pre-built Django app and simply integrate it into your project.

The majority of our work in Django will revolve around these apps, so let's start by creating one. The command for this is `manage.py startapp`.

As we aim to build a to-do list, we'll create an app named `todo`. To do so, enter the following command:

```bash
python3 manage.py startapp todo
```

Upon execution, you'll notice a new folder named `todo` in your file explorer. Inside this folder, you'll find various other files and items related to your new Django app.

## START App


To initialize a Django application, follow these steps:

1. **Create a new Django application**. Open your terminal and execute the following command:

```bash
python3 manage.py startapp todo
```

2. **Create a `templates` folder**: Within your newly created `todo` app directory, create a folder named `templates`.

3. **Define a function in `views.py`**: Open the `views.py` file located in your `todo` app directory and add the following function:

```python
def get_my_list(request):
    return render(request, 'todo/todo_list.html')
```

4. **Update your URLs**: In your main project directory, find the `urls.py` file. Here, import the `get_my_list` function from your views, then add a new path as follows:

```python
from todo.views import get_my_list

urlpatterns = [
    # ...existing paths...
    path('', get_my_list, name="get_my_list"),
]
```

5. **Add your new app to `INSTALLED_APPS`**: Lastly, you need to let Django know that you've created a new application. Open the `settings.py` file in your main project directory and add your new app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # ...existing apps...
    'todo',
]
```

## DJANGO Migrations

Here are the key commands you'll need to understand and execute for handling Django migrations, organized in a step-by-step format:

---

1. **`makemigrations` command**: This command tells Django to create new migrations based on the changes detected in your models. For now, you can use it with a dry run flag to see what would happen without making any actual changes:

   ```bash
   python3 manage.py makemigrations --dry-run
   ```

   Once we begin modifying our models, we will need to run this command without the dry run flag.

-  `makemigrations` does not apply these migrations to the database, it just generates the SQL commands needed to make the changes. The output of this command are migration files - Python scripts that are stored in your codebase.

2. **`showmigrations` command**: This command lists all the migrations in your project, including those for the built-in Django apps like authentication and Django admin. Run the following command to view all migrations:

   ```bash
   python3 manage.py showmigrations
   ```

   You'll `see some migrations that need to be applied`, especially for Django's built-in apps. Applying these migrations will set up the database and enable the creation of an admin user.

3. **`migrate` command**: This command applies or unapplies the migrations. Let's run it with the plan flag to preview what it will do:

   ```bash
   python3 manage.py migrate --plan
   ```

   The initial migrations will set up basic requirements such as the users, groups, and permissions tables, and alter some fields in those tables. To apply all these migrations, just run:

   ```bash
   python3 manage.py migrate
   ```

- Essentially, `migrate` takes the migrations created by `makemigrations` (those SQL commands) and executes them against the database, thereby creating, modifying, or deleting database tables as per the migrations. This command actually alters the database schema.

4. **`createsuperuser` command**: Finally, after all migrations have been applied, create a superuser to manage your database:

   ```bash
   python3 manage.py createsuperuser
   ```

   You will be prompted for a username and password. An email address is optional.

---

## REGISTER Model

In order to manage your model objects via Django's admin site, you need to register the model with the admin site. Here's how to do it for an 'item' model in a 'todo' app:

1. **Open 'admin.py'**: Navigate to the `admin.py` file in your 'todo' app directory.

2. **Import your model**: At the top of your `admin.py` file, import your 'item' model from the `models.py` file in the same directory. Add the following line:

   ```python
   from .models import Item
   ```

   This line translates to: "from the current directory's `models.py` file, import the `Item` class."

3. **Register your model**: After importing your 'item' model, register it with Django's admin site using the `admin.site.register()` function:

   ```python
   admin.site.register(Item)
   ```

   Now, Django's admin site is aware of the 'item' model.

4. **Save your changes**: Remember to save the `admin.py` file after making these changes.

5. **Run your Django server**: You can start your Django project by running the following command in your terminal:

   ```bash
   python3 manage.py runserver
   ```

6. **Access Django's admin site**: Visit the admin panel of your site (usually at `<your_domain>/admin`). You should now see your 'item' model represented as a table in the admin site.

## REVERSE or Unmigrate DB tables

To reverse (or "unmigrate") migrations in Django, you use the `migrate` command followed by the name of the app and the name of the migration you want to revert to. This will undo all migrations up to and including the specified migration.

If you want to roll back all migrations for an app, you can use the `migrate` command followed by the app's name and `zero`. This will unapply all migrations for that app, effectively dropping the corresponding database tables.

Here are the steps:

1. **List all migrations**: First, you need to know which migrations have been applied. Use the `showmigrations` command to list them:

   ```bash
   python3 manage.py showmigrations
   ```

2. **Roll back to a specific migration**: If you want to roll back to a specific migration, use the `migrate` command followed by the name of the app and the name of the migration. For example, to roll back to the '0001_initial' migration of the 'todo' app, you would do:

   ```bash
   python3 manage.py migrate todo 0001_initial
   ```

3. **Unapply all migrations for an app**: To unapply all migrations for a particular app, use the `migrate` command followed by the name of the app and `zero`. For example, to unapply all migrations for the 'todo' app, you would do:

   ```bash
   python3 manage.py migrate todo zero
   ```

Remember to replace 'todo' with the name of your actual app, and '0001_initial' with the actual name of the migration you want to revert to. Always be cautious when rolling back migrations, as this can result in loss of data.

### DEBUG
   OperationalError at /admin/todo/task/
   no such table: todo_task

The error message indicates that there is no table named "todo_task" in your database. This error typically occurs when you try to access a table that hasn't been created yet or when the table has been accidentally deleted.

To resolve this issue, you can follow these steps:

1. Run the following command to create the necessary tables in your database:

```bash
python manage.py migrate
```

This command will apply any pending database migrations and create the required tables.

2. If the migration step doesn't solve the problem, you may need to check if there are any pending migrations that haven't been applied. Run the following command to see a list of pending migrations:

```bash
python manage.py showmigrations
```

Make sure that the migration for the "todo" app is listed.

3. If there are pending migrations, apply them using the following command:

```bash
python manage.py migrate <app_name>
```

Replace `<app_name>` with the actual name of your app, which in this case seems to be "todo."

4. If the migrations are up to date and the table still doesn't exist, it's possible that the table was accidentally deleted. In that case, you can recreate the table by running the following command:

```bash
python manage.py makemigrations <app_name>
```

This command will generate a new migration file for the app. Then, apply the migration with:

```bash
python manage.py migrate <app_name>
```

5. If none of the above steps work, ensure that your database configuration is correctly set up in your Django project's settings file (`settings.py`). Check the database engine, name, user, password, and host to make sure they match your database setup.

By following these steps, you should be able to resolve the "no such table" error and access the `/admin/todo/task/` URL without encountering the error.