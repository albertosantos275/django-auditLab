import json 
import openpyxl
from  . import ca01_agregates 

def load_json(input_file):
    with open(input_file) as fp:
        data = json.load(fp)
        return data


person_types = None
operation_types = None
service_types = None
divisa_types = None
economic_activities = None
localidades = None
payment_types = None
vinculacion_type = None
default_bank = None
def load_references():
    global person_types , operation_types, service_types
    global divisa_types,economic_activities, localidades
    global payment_types, vinculacion_type, default_bank
    person_types = load_json('ref_person_types.json')
    operation_types = load_json('ref_operations.json')
    service_types = load_json('ref_services.json')
    divisa_types = load_json('ref_divisas.json')
    economic_activities = load_json('ref_activity_economic.json')
    localidades = load_json('ref_localidades.json')
    payment_types = load_json('ref_pay_type.json')
    vinculacion_type =  load_json('ref_vinculacion_type.json')
    default_bank =   load_json('ref_default_bank.json')


def compute_agregates(ref_sheet):
    
    by_person= ca01_agregates.agregate_by_person_type(ref_sheet,0, 25,2, person_types)
    #ref_sheet, row_name, key_col, amount_col, 
    #max_col_number,row_number, codes
    by_divisa = ca01_agregates.agregate_by_single_col(ref_sheet,'divisa',23,3,24,2, divisa_types)
    by_payment = ca01_agregates.agregate_by_single_col(ref_sheet,'name',15,3,24,2, payment_types)
    by_vinculacion = ca01_agregates.agregate_by_single_col(ref_sheet,'name',21,3,24,2, vinculacion_type)
   
    #by_operation  = ca01_agregates.agregate_by_operation(ref_sheet,0, 12,2, operation_types, default_bank)
    by_service  = ca01_agregates.agregate_by_services(ref_sheet,1,3,0, 25,2, service_types)
    by_province  = ca01_agregates.agregate_by_provinces(ref_sheet,12,3,0, 25,2, localidades)
                                                                    #user_col, amount_col,  min_col_number, max_col_number,row_number
    by_activity  = ca01_agregates.agregate_by_economic_activity(ref_sheet,8,3,0, 25,2, economic_activities, default_bank)
    by_suspicious  = ca01_agregates.agregate_by_suspicious_activity(ref_sheet,8,3,0,25,2, economic_activities, default_bank)

    agregates ={
        "by_person":by_person,
        "by_divisa":by_divisa,
        "by_payment": by_payment,
        "by_vinculacion" : by_vinculacion,

        # "by_operations": by_operation,
        "by_service": by_service,
        "by_province": by_province,
         
        "by_activity":by_activity,
         "by_suspicious":by_suspicious 
    }

    return agregates

    
def translate_row(ref_sheet, field, col_number, row_number, codes):
     for row in ref_sheet.iter_rows(min_row=row_number,
                            min_col=col_number,max_col=col_number):
        
        code  = row[0].value
        
        
        if code == None:
            continue
        code = str(code)
        
        if code in codes.keys():
            row[0].value= codes[code][field]
        else:
            print(code)

def translate(ref_sheet):
    translate_row(ref_sheet,'user',10, 2,person_types )
    # translate_row(ref_sheet,'operation',7, 2,operation_types )
    translate_row(ref_sheet,'service',2, 2,service_types )
    translate_row(ref_sheet,'divisa',24, 2,divisa_types )
    translate_row(ref_sheet,'nombre',13, 2,localidades )
    translate_row(ref_sheet,'name',22, 2,vinculacion_type )
    translate_row(ref_sheet,'name',16, 2,payment_types )
    # translate_row(ref_sheet,'user',13, 2,person_types )
    # translate_row(ref_sheet,'user',18, 2,person_types )
    # translate_row(ref_sheet,'activity',27, 2,economic_activities )
    # translate_row(ref_sheet,'activity',30, 2,economic_activities )
    # translate_row(ref_sheet,'activity',33, 2,economic_activities )

        
def parse(input_file, output_file):
    load_references()
    workbook = openpyxl.load_workbook(input_file)
    ref_sheet = workbook.active
    #TODO , do preprocessing like converting to pesos
    agregates = compute_agregates(ref_sheet)
    translate(ref_sheet)

    output_file_agregates= output_file.split(".")[0]
    output_file_agregates+=".json"
    
    # with open(output_file_agregates,"w") as fp:
    #     json.dump(agregates, fp)
    workbook.save(output_file)
    return agregates

# r= parse('ca01.xlsx', 'ca01_m.xlsx')
# print(r["by_suspicious"])

