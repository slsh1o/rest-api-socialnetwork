# REST API test task

## Installing
To install simply clone this repo and run `pip install -r requirements.txt`. Then apply the migrations.

## Presentation
Start server and run `python bot.py` script for short showcase of the api routes.

## API
* `POST api/jwtauth/register/` - register new user. __Params__: `username`, `email`, `password`, `password_repeat`.
* `POST api/jwtauth/login/` - obtain `access` and `refresh` tokens. __Params__: `username`, `password`.
* `POST api/jwtauth/refresh/` - get refreshed `access` token. __Params__: `refresh` token.
* `POST api/posts/` - create new post. __Params__: `title`, `content`.
* `GET api/posts/` - list all posts.
* `GET api/posts/<int:post_id>/like/` - like or unlike post.
* `GET api/analytics/user/<int:pk>/` - show time of user's last login and request to the api.
* `GET api/analytics/likes/` - show amount of likes aggregated by day. _Optionaly_ `?date_from=&date_to=` can be passed via url to specify range of days.
