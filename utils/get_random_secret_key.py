from django.core.management.utils import get_random_secret_key
# Сгенерировать случайный секретный ключ для проекта
secret_key = get_random_secret_key()
print(secret_key)