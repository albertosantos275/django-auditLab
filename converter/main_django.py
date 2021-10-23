
import datetime
import time
from  . import if01, ca01, fdo03b, de11
from  . import de13, de15, de14, tp01, fd01
import os
import sys
from os.path import expanduser
from .  import merge_excel
import json
#concat files
#call processer 
#save output file


print("changing path")
home = expanduser("~")
my_path=f"{home}/converter/"
os.chdir(my_path)



start_time=datetime.datetime.timestamp(datetime.datetime.utcnow())
parsers ={
    'if01' :if01.parse,
    'ca01': ca01.parse,
    'fd03b':fdo03b.parse,
    'de11' : de11.parse,
    'de13': de13.parse,
    'de15' : de15.parse,
    'de14': de14.parse,
    'tp01': tp01.parse,
    'fd01': fd01.parse,
}

# input_paths =  sys.argv[1].split(",")
# outputfile=sys.argv[2]
# filetype = sys.argv[3]
# 'unmodified/if1.xlsx','modified/if1.xlsx','if01'


# Give the location of the file
def dump_json(data, filename):
    with open(filename, "w") as fp:
        json.dump(data, fp)

def remove_file(myfile):
    try:
        os.remove(myfile)
    except OSError as e:  
        print ("Error: %s - %s." % (e.filename, e.strerror))

def do_convert(input_file, output_file, parser_type):
    filename = input_file
    r = None
    if filename !=None:
        #temp_output = filename.replace(".xlsx","_m.xlsx")
        if parser_type in parsers.keys():
            r=parsers[parser_type](filename, output_file)
        # remove_file(filename)
        # remove_file(temp_output)
    return r


def create_report(input_paths,outputfile, filetype):
    print('Creating report ....', input_paths)
    try:
        start_time=datetime.datetime.timestamp(datetime.datetime.utcnow())
        temp_name= f"{home}/{int(start_time)}.xlsx"
        print(temp_name)
        merge_excel.concat_files(input_paths,temp_name)
        temp_outputfile = outputfile.replace(".json",".xlsx")
        result= do_convert(temp_name,temp_outputfile, filetype)
        dump_json(result,outputfile)
        remove_file(temp_name)

        # d={"status": "done",
        # "error":"none",
        # "inputfile" : inputfile,
        # "outputfile":  outputfile,
        # "filetype" : filetype,
        # "doneAt": start_time,
        # "result" : result
        # }
        # print(d)
        
    except Exception as ex:
        print(ex)
    
