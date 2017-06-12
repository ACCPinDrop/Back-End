# PinDrop Restful API

## Getting Started

- Download this repository to your machine.
- Unzip the repository file.
- Open a Shell/Terminal/Comand-Line.
- Go inside of your new folder `( cd Back-End-rapiModels )`.
- Run python manage.py makemigrations.
- Run python manage.py migrate.
- Create a new Super User `( run python manage.py createsuperuser )`.
- Start your server `( run python manage.py runserver )`.
- Go to your Django administration page `( http://127.0.0.1:8000/admin/ )` and login.

## Inserting data to our databases

>   As you probably noticed we don't have any data inside our models so lets add some data:

> I have created a new function called `create_data` to populate our databases. You just have to access the __`/create_data`__ url to trigger the `create_data` function `( http://127.0.0.1:8000/create_data )`

#### Or...

> > You can type in your shell `python manage.py createdata`.

## Deleting data from our databases

>   I have created a new function called `delete_data` to delete our databases. You just have to access the __`/delete_data`__ url to trigger the `delete_data` function `( http://127.0.0.1:8000/create_data )`.

#### Or...

> > You can type in your shell `python manage.py deletedata`.


## Now you can test the tables and fields. 

>   Please, feel free to analyze the tables and fields and give us `( BackEnd Team )` some feedback. There are many things to improve within our models and we only can do it together! **`( http://127.0.0.1:8000/all )`**

### Each Table

- http://127.0.0.1:8000/all/events
- http://127.0.0.1:8000/all/groups
- http://127.0.0.1:8000/all/organizers
- http://127.0.0.1:8000/all/locations
- http://127.0.0.1:8000/all/categories



