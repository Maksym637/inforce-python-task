# inforce-python-task
- - -
### Prepared by _Maksym Oliinyk_
- - -
### Project description :
Simple Back End part with REST architecture :
- Django + DRF
- JWT
- PostgreSQL
- Testing
- Docker (docker-compose)

(The project settings are in the folder : _restaurant/restaurant/_)
- - - 
### Run application :
1. Run **server** with the command : `python manape.py runserver`
2. Run **tests** with the command : `python manage.py test`

(Do it in dir _restaurant/_)
- - -
### Run application with docker :
1. Run **database** with the command : `docker-compose up database`
2. Run **tests** with the command : `docker-compose up tests`
3. Run **server** with the command : `docker-compose up web`

(Running on http://127.0.0.1:8000/)
- - -
### API endpoints :
- **user :**
  - POST ('register/') : create and submit user to the server.
  ```json
  {
    "username": "U1",
    "email": "user1@gmail.com",
    "password": "1111"
  }
  ```
  - GET ('user/') : retrieves all users from the server.
  ```json
  [
    {
        "id": 1,
        "last_login": null,
        "email": "user1@gmail.com",
        "username": "U1",
        "start_date": "2022-10-25T22:40:09.881381Z",
        "is_staff": false,
        "is_superuser": false,
        "is_active": true,
        "groups": [],
        "user_permissions": []
    }
  ]
  ```

- **login and logout :**
  - POST ('login/') : login form for user.
  ```json
  {
    "email": "user1@gmail.com",
    "password": "1111"
  }
  ```
  - POST ('logout/') : logout form for user.
  ```json
  {
    "refresh_token": "token"
  }
  ```

- **employee :**
  - POST ('employee/create/') : create and submit an employee to the server.
  ```json
  {
    "employee_no": "emp1",
    "user": 1
  }
  ```
  - GET ('employee/') : retrieves all employees from the server.
  ```json
  [
    {
        "id": 1,
        "employee_no": "emp1",
        "created_at": "2022-10-25T22:40:55.414090Z",
        "updated_at": "2022-10-25T22:40:55.414090Z",
        "created_by": null,
        "user": 1
    }
  ]
  ```

- **restaurant :**
  - POST ('restaurant/create/') : create and submit a restaurant to the server.
  ```json
  {
    "name": "Love&Lviv",
    "contact_phone": "+380687731854",
    "address": "St. Street"
  }
  ```
  - GET ('restaurant/') : retrieves all restaurants from the server.
  ```json
  [
    {
        "id": 1,
        "name": "Love&Lviv",
        "contact_phone": "+380687731854",
        "address": "St. Street",
        "created_at": "2022-10-25T22:41:53.325757Z",
        "updated_at": "2022-10-25T22:41:53.325757Z",
        "created_by": null
    }
  ]
  ```

- **menu and vote :**
  - POST ('menu/create/') : create and submit menu to the server.
  ```json
  {
    "votes": 10,
    "restaurant": 1
  }
  ```
  - GET ('meunu/') : retrieves all menus from the server.
  ```json
  [
    {
        "id": 1,
        "file_contant": null,
        "votes": 10,
        "created_at": "2022-10-25T22:42:33.225029Z",
        "updated_at": "2022-10-25T22:42:33.225029Z",
        "created_by": null,
        "restaurant": 1
    }
  ]
  ```
  - POST ('vote/create/') : create and submit vote to the server.
  ```json
  {
    "employee": 1,
    "menu": 1
  }  
  ```
  - GET ('vote/') : retrieves all votes from the server.
  ```json
  [
    {
        "id": 1,
        "voted_at": "2022-10-25T22:43:06.647571Z",
        "employee": 1,
        "menu": 1
    }
  ]
  ```
- - -