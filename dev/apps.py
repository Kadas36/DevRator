from django.apps import AppConfig


class DevConfig(AppConfig):
    name = 'dev'

    def ready(self):
        import dev.signals
