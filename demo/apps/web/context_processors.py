from django.conf import settings


def add_sigurd_profile(request):
    context = {"ACTIVE_SIGURD_PROFILE": settings.ACTIVE_SIGURD_PROFILE}
    return context
