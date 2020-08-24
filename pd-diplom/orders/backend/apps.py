from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'backend'
    verbose_name = 'Бэкэнд'

    def ready(self):
        """
        импортируем сигналы
        """
