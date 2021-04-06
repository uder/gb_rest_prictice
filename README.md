Run React App
set PATH=%PATH%;C:\Program Files\nodejs
cd frontend
npm run start

http://127.0.0.1:3000


Run DRF App
venv\Scripts\python.exe main\manage.py runserver

http://127.0.0.1:8000


Run tests
cd main
..\venv\Scripts\python.exe manage.py test


Get DjangoUser models
First version API
http://127.0.0.1:8000/api/v1/user/
http://127.0.0.1:8000/api/v1/djangouser/
Second version API
http://127.0.0.1:8000/api/v2/user/
http://127.0.0.1:8000/api/v2/djangouser/

Docs 
http://127.0.0.1:8000/redoc/
