import requests


username = 'test_user'
email = 'test_user@mail.com'
password = 'tuser'

refresh_token = ''
access_token = ''

base_url = 'http://localhost:8000/api/'


def _print_result(response):
    print(f'Result of the request:\n'
          f'Status: {response.status_code}\n'
          f'Body:')
    for k, v in response.json().items():
        print(f'"{k}": "{v}"')
    print('-' * 10)


def register_user():
    payload = dict(username=username, email=email, password=password, password_confirm=password)
    res = requests.post(base_url + 'jwtauth/register/', data=payload)
    if res.status_code == 201:
        print(f'User `{username}` registered')
        return


def login_user():
    payload = dict(username=username, password=password)
    res = requests.post(base_url + 'jwtauth/login/', data=payload)
    print(f'Login as `{username}`')
    if res.status_code == 200:
        return res.json()


def refresh_tokens():
    payload = dict(refresh=refresh_token)
    res = requests.post(f'{base_url}jwtauth/refresh/', data=payload)
    _print_result(res)
    if res.status_code == 200:
        return res.json()['access']


def create_post(title, content):
    payload = dict(title=title, content=content)
    headers = dict(Authorization=f'Bearer {access_token}')
    res = requests.post(base_url + 'posts/', data=payload, headers=headers)
    _print_result(res)
    if res.status_code == 201:
        return res.json()


def list_posts():
    headers = dict(Authorization=f'Bearer {access_token}')
    res = requests.get(base_url + 'posts/', headers=headers)
    print('-' * 10)
    if res.status_code == 200:
        print(f'Result of the request:\n'
              f'Status: {res.status_code}\n'
              f'Body:')
        for post in res.json():
            for k, v in post.items():
                print(f'"{k}": "{v}"')
            print('-' * 10)


def like_unlike_post(post_id):
    headers = dict(Authorization=f'Bearer {access_token}')
    res = requests.get(base_url + f'posts/{post_id}/like/', headers=headers)
    _print_result(res)


def analytics_all_likes():
    headers = dict(Authorization=f'Bearer {access_token}')
    res = requests.get(f'{base_url}analytics/likes/', headers=headers)
    print(f'Result of the request:\n'
          f'Status: {res.status_code}\n'
          f'Body:')
    for post in res.json():
        for k, v in post.items():
            print(f'"{k}": "{v}"')
        print('-' * 10)


def analytics_user_activity(user_id):
    headers = dict(Authorization=f'Bearer {access_token}')
    res = requests.get(base_url + f'analytics/user/{user_id}/', headers=headers)
    _print_result(res)


if __name__ == '__main__':
    # SET UP
    print('Hello. This is my short showcase of the test project.\n\n'
          'This script will show you all features step by step.\n\n'
          'On each step script will tell what it going to do,\n'
          'give you `>Endpoint` with http method of next request\n'
          'and short description about what should be in response.')
    input('Press Enter to continue')
    print()
    # register -> login
    print(f'>Endpoint POST: /api/jwtauth/register/')
    print('When reached: register new `User`')

    register_user()
    print()
    print('>Endpoint POST: /api/jwtauth/login/')
    print('When reached: return `refresh` & `access` jwt tokens')

    refresh_token, access_token = login_user().values()
    print()

    # create a few posts -> like them
    print('/\\' * 10)
    print('Now script will create 3 new posts:\n')
    print('>Endpoint POST: /api/posts/')
    print('When reached: create new `Post`')
    input('Press Enter')
    print()

    # create_post('First post', 'Content of first post')
    # create_post('Another one', 'Object of this task is to create a simple REST API.')
    # create_post('Requirements', 'Implement token authentication (JWT is preferred). Yes I did it)')

    print('/\\' * 10)
    print('Like this posts:\n')
    print('>Endpoint GET: /api/posts/post_id/like/')
    print('When reached: like or unlike post with passed `post_id`')
    input('Press Enter')
    print()
    [like_unlike_post(n) for n in range(1, 4)]
    print()

    # show analytics
    print('/\\' * 10)
    print('Display analytics about amount of likes:\n')
    print('>Endpoint GET: /api/analytics/likes/')
    print('When reached: show how many likes was made aggregated by day')
    input('Press Enter')
    print()

    analytics_all_likes()
    print()

    print('/\\' * 10)
    print('Time to unlike posts:\n')
    print('>Endpoint GET: /api/posts/post_id/like/')
    print('Same endpoint and http method as for like post above')
    input('Press Enter')
    print()

    [like_unlike_post(n) for n in range(1, 4)]
    print()

    print('/\\' * 10)
    print('Show analytics about user activity:\n')
    print('>Endpoint GET: /api/analytics/user/user_id/')
    print('When reached: show time of last login and request of the user with passed `user_id`')
    input('Press Enter')
    print()

    analytics_user_activity(1)
    print('\nAll features from the task was shown.\nThank you for your attention :D\n')

    # list posts
    # print('>Endpoint GET: /api/posts/')
    # print('Return list of all posts')
    # list_posts()
