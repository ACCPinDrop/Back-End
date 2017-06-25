# PinDrop Restful API

### Requirements

> - Python - 3.6.1v
> - Virtualenv - 15.1.0v
> - PostgreSQL(9.3.17v):
>   - TABLE_NAME = postgres
>   - USER_NAME = postgres
>   - PASSWORD = 132465
>   - PORT = 5432



### Getting Started

> - Download this repository to your machine.
> - Unzip the repository file.
> - Open a Shell/Terminal/Comand-Line.
> - Go inside of your new folder **`( cd Back-End-rapiModels )`**.
> - Create a new virtual environment named **'env'** using the [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) tool. **`( virtualenv env --no-site-package )`**
> - [Activate](https://virtualenv.pypa.io/en/stable/userguide/#activate-script) your new virtual environment. Use their [user Guide](https://virtualenv.pypa.io/en/stable/userguide/) if needed. 
> - [Install](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/#other-notes) the the necessary packages using the requirements.txt file. Remember, you must to be in the same repository as the requirements.txt file. **`( pip install -r requirements.txt )`**
> - Run **python manage.py migrate** .
> - Create a new Super User **`( python manage.py createsuperuser )`**.
> - Start your server **`( python manage.py runserver )`**.
> - Go to your Django administration page **( http://127.0.0.1:8000/admin/ )** and login.



### Inserting data to our databases

> As you probably noticed we don't have any data inside our models so lets add some data:

> I have created a new function called **`create_data`** to populate our databases. You just have to access the __`/create_data`__ url to trigger the **`create_data`** function **( http://127.0.0.1:8000/create_data )**.

*Or...*

> You can type in your shell **`python manage.py createdata`** .



### Deleting data from our databases

>   I have created a new function called **`delete_data`** to delete our databases. You just have to access the __`/delete_data`__ url to trigger the **`delete_data`** function **( http://127.0.0.1:8000/delete_data )**.

*Or...*

> You can type in your shell **`python manage.py deletedata`** .



### Now you can test the tables and fields. 

>   Please, feel free to analyze the tables and fields and give us **`( BackEnd Team )`** some feedback. There are many things to improve within our models and we only can do it together!



## Requets

#### GET / *POST*

- http://127.0.0.1:8000/categories/
- http://127.0.0.1:8000/locations/
- http://127.0.0.1:8000/organizers/
- http://127.0.0.1:8000/groups/
- http://127.0.0.1:8000/events/

#### *PUT* / *DELETE*

- http://127.0.0.1:8000/categories/id/
- http://127.0.0.1:8000/locations/id/
- http://127.0.0.1:8000/organizers/id/
- http://127.0.0.1:8000/groups/id/
- http://127.0.0.1:8000/events/id/


