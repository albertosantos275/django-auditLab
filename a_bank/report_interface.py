import subprocess
import datetime
from os.path import expanduser



def launch_create_report(info):
    start_time=datetime.datetime.timestamp(datetime.datetime.utcnow())
    temp_name= f"{int(start_time)}.json"
    input_dir= info['absolute_files_path']
    file_type= info['file_type_code']
    output_file= info['result_storage_path']+f"/{temp_name}"
    home_dir=expanduser('~')
    try:
        args=["python3",f"{home_dir}/converter/main_django.py", input_dir,output_file, file_type]
        cp = subprocess.run(args)
    except Exception as e:
        print(e)
    return output_file

#code for testing
# info={
#   'absolute_files_path':"/scratch/excels",
#     'file_type_code':'if01',
#     'result_storage_path':'/scratch/results'

# }

# s=launch_create_report(info)
# print(s)