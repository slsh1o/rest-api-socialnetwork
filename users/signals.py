from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


User = get_user_model()


@receiver(user_logged_in, sender=User)
def track_user_logged_in(sender, user, **kwargs):
    """
    Catch `user_logged_in` signal.

    Aimed to set time when user logged in via api/jwtauth/login/
    """
    user_model = User.objects.get(id=user.id)
    user_model.update_last_jwt_login()
