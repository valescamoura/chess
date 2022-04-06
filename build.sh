# Iniciar servidor
python manage.py runserver &
# 2 min para que o servidor inicie
sleep 120
# Interromper processo caso não retorne erros
pkill -f runserver