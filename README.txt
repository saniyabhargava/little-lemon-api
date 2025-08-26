Little Lemon Web Application (Django + DRF + MySQL)

Run locally:
1) py -m venv .venv && .venv\Scripts\activate
2) pip install -r requirements.txt  (or install: django, djangorestframework, djangorestframework-simplejwt, PyMySQL, python-dotenv)
3) Create MySQL DB and set .env as in README
4) python manage.py migrate
5) python manage.py runserver

Static HTML pages:
- /           (Home)
- /about/
- /menu-page/
- /book/

API base URL: /api/

Authentication (JWT):
- POST /api/registration/           (public)  -> {"username","password","email"}
- POST /api/token/                  (public)  -> {"username","password"} returns access/refresh
- POST /api/token/refresh/          (public)  -> {"refresh"} returns new access

Menu API:
- GET    /api/menu/                 (public)
- GET    /api/menu/{id}/
- (Create/Update menu via admin UI recommended)

Bookings API (auth required):
- GET    /api/bookings/
- POST   /api/bookings/             body: {"name","guests","booking_date","booking_time","special_requests"}
- GET    /api/bookings/{id}/
- PUT    /api/bookings/{id}/
- PATCH  /api/bookings/{id}/
- DELETE /api/bookings/{id}/

Testing:
- python manage.py test
- Insomnia steps: Register -> Token -> Menu (GET) -> Bookings (CRUD with Bearer token)
