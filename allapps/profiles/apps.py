from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'allapps.profiles'
    verbose_name = '_Profiles App'

    def ready(self):
        from . import signals
