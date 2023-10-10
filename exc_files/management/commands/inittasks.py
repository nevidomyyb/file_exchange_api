from typing import Any
from rocketry import Rocketry
from django.core.management import BaseCommand
from file_manager.models import FileExchange
import datetime
import os
from asgiref.sync import sync_to_async

#Functions to handle with logs
def verify_and_create_archive(archive_name):
    try:
        a = open(f"./logs/{archive_name}", 'rt')
        a.close()
    except FileNotFoundError:
        if not os.path.isdir("./logs"):
            os.mkdir('./logs')
            print("Dir 'logs' created.")
            try: 
                a = open(f"./logs/{archive_name}", 'wt+')
            except:
                print(f"Fail at file creation: {archive_name}")
            else:
                a.close()
def register_log(archive_name, o, m):
    try:
        a = open(f"./logs/{archive_name}", 'at')
    except:
        print("Fail at register in log")
    else:
        hora_atual = datetime.datetime.now()
        a.write(f"{hora_atual}: [{o}]: {m}\n")
        a.close()

## Begin of scheduler codes
app = Rocketry(execution="async")

def delete_old_instances():
    instances = FileExchange.objects.all()
    register_log('logs.txt', 'system', 'Teste')
    for i in instances:
        time_now = datetime.datetime.now().timetz()
        time = i.creation_at.timetz()
        register_log('logs.txt', 'system', f'Time now: {time_now} | time: {time}')

@app.task('every 1 minute')
async def do_delete_old_instances():
    await sync_to_async(delete_old_instances)()

class Command(BaseCommand):
    help = "Setup the periodic tasks runner"

    def handle(self, *args, **options):
        verify_and_create_archive('logs.txt')
        self.stdout.write(self.style.SUCCESS('Rocketry launched'))
        app.run()