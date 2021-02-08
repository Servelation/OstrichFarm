from django.core.management import call_command

def my_backup():
    try:
        call_command('python manage.py dbbackup')
    except:
        pass