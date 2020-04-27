# REST API test task

## Installing
To install simply clone this repo and run `pip install -r requirements.txt`.

## Presentation
Run `python bot.py` script while running server for short showcase of api routes.

## API
* `POST api/jwtauth/register/` - register new user.
* `POST api/jwtauth/login/` - obtain `access` and `refresh` tokens.
* `POST api/jwtauth/refresh/` - get refreshed `access` token.
* `POST api/posts/` - create new post.
* `GET api/posts/` - list all posts.
* `GET api/posts/<int:post_id>/like/` - like or unlike post.
* `GET api/analytics/user/<int:pk>/` - show time of user's last login and request to the api.
* `GET api/analytics/likes/` - show amount of likes aggregated by day. Optionaly `?date_from=&date_to=` can be passed via url to specify range.
