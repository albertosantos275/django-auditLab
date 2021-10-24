import subprocess
import datetime
from os.path import expanduser
from converter.main_django import create_report
from auditLab.celery import app

@app.task
def launch_create_report(info):
    start_time=datetime.datetime.timestamp(datetime.datetime.utcnow())
    temp_name= f"{int(start_time)}.json"
    input_dir= info['absolute_files_path']
    file_type= info['file_type_code']
    output_file= info['result_storage_path']+f"/{temp_name}"
    home_dir=expanduser('~')
    print(input_dir,output_file, output_file)

    create_report(input_dir,output_file, 'if01')

   