# Iniciar servidor
python manage.py runserver &
# 1 min para que o servidor inicie
sleep(60)
# Interromper processo caso não retorne erros
pkill -f runserver