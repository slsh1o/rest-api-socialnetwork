from django.utils import timezone


class RequestTimeAPIMixin:
    """Save or update time of a request of the user."""
    def initial(self, request, *args, **kwargs):
        request_time = timezone.now()

        user = request.user
        user.request_last_time = request_time
        user.save(update_fields=['request_last_time'])

        super().initial(request, *args, **kwargs)
