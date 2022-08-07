from django.apps import AppConfig


class GuestConfig(AppConfig):
    name = 'Guest'

    def ready(self):
        import Guest.signals
