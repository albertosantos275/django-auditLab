

def filter_total_zero(data):
    keys = list(data.keys())
    for k in keys:
        v= data[k]
        total = v['total']
        if total==0.0:
            del data[k]


def agregate_by_person_type(ref_sheet, min_col_number, max_col_number,row_number, codes): 
    data={

    }
    risk_data={
        "Alto":{"total":0},
        "Bajo":{"total":0},
        "Medio":{"total":0},
    }
    total = 0
    risk_total =0
    for k in codes.keys():
        val = codes[k]
        data[k]={
            "total":0,
            'user' : val['user'],
            'risk' : val['risk']
        }
    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
        userType= row[0].value
        transaction = row[9].value
        monedad = row[10].value
        
        if monedad == "DOP": 
            if userType in data.keys():
                data[userType]["total"]+=transaction
                total+=transaction
                risk = codes[userType]['risk']
                if risk in risk_data.keys():
                    risk_data[risk]['total']+=transaction
                    risk_total+=transaction
            else:
                print(f"user type not found {userType}")

    filter_total_zero(data)

    for t in data.values():
        t['perc']= t['total']/total*100

    for t in risk_data.values():
        t['perc']= t['total']/risk_total*100

        
    temp={
        "agregates" : data,
        "total": total,
        "risk_total":risk_total,
        "risk": risk_data
    } 
    #TODO agregar total de las transacciones
    # agregar cuenta de cada tipo   

    return temp 




def agregate_by_operation(ref_sheet, min_col_number, max_col_number,row_number, codes): 
    data={

    }
   
    total = 0
    risk_total =0
    for k in codes.keys():
    
        val = codes[k]
        data[k]={
            "total":0,
            'operation' : val['operation'],
        }
   
    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
        operation= str(row[6].value)
        transaction = row[10].value
        monedad = row[11].value
        
        
        if monedad == "DOP": 
            if operation in data.keys():
              
                data[operation]["total"]+=transaction
                total+=transaction
                
            else:
                print(f"operation type not found {operation}")
            

    filter_total_zero(data)
    

    for t in data.values():
        t['perc']= t['total']/total*100
    

       
    temp={
        "agregates" : data,
        "total": total,
        
    } 
    #TODO agregar total de las transacciones
    # agregar cuenta de cada tipo   

    return temp 





def agregate_by_services(ref_sheet, min_col_number, max_col_number,row_number, codes): 
    data={

    }
   
    total = 0
    risk_total =0
    phases={}
    for k in codes.keys():
    
        val = codes[k]
        data[k]={
            "total":0,
            'service' : val['service'],
            'phase':val['phase']
        }
   
    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
        service= str(row[7].value)
        transaction = row[10].value
        monedad = row[11].value
        
        if monedad == "DOP": 
            if service in data.keys():
                phase=  data[service]["phase"]
                data[service]["total"]+=transaction
                total+=transaction
                if phase not in phases.keys():
                    phases[phase]={
                        'total': 0,
                    }
                phases[phase]['total']+=transaction

            else:
                print(f"operation type not found {service}")
            

    filter_total_zero(data)
    filter_total_zero(phases)
    
    for t in data.values():
        t['perc']= t['total']/total*100
    for t in phases.values():
        t['perc']= t['total']/total*100
       
    temp={
        "agregates" : data,
        "total": total,
        "phases": phases
    } 
    #TODO agregar total de las transacciones
    # agregar cuenta de cada tipo   

    return temp 







def agregate_by_economic_activity(ref_sheet, min_col_number, max_col_number,row_number, codes): 
    data={

    }
   
    total = 0
    risk_total =0
    phases={}
    data = {}
    risks= ["Riesgo 1","Riesgo 2","Riesgo 3","Delito Precedente 1","Delito Precedente 2",
    "Delito Precedente 3"]
    for k in risks:
    
        data[k]={
            
             "agregates":{}
        }

    def init_delito(key, temp):
         if key not in temp.keys():
                    temp[key]={
                        'total': 0,
                    }

    # if True:
    #     return data
   
    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
        activity= str(row[26].value)
        transaction = row[10].value
        monedad = row[11].value
        
        if monedad == "DOP": 
            if activity in codes.keys():
                # print(activity)
                total+=transaction
                for risk in risks:
                    r1=  codes[activity][risk]
                    # data[service]["total"]+=transaction
                    
                    if r1==None:
                        r1='Desconocido'
                        
                    init_delito(r1,data[risk]['agregates'])
                    data[risk]['agregates'][r1]['total']+=transaction
            else:
                print(f"operation type not found {activity}")
            
    
    filter_total_zero(data["Riesgo 1"]['agregates'])
    #filter_total_zero(phases)
    for risk in risks:
        for t in data[risk]['agregates'].values():
            t['perc']= t['total']/total*100
  
    temp={
        "agregates" : data,
        "total": total,
        "phases": phases
    } 
     
    #TODO agregar total de las transacciones
    # agregar cuenta de cada tipo   

    return temp 





def agregate_by_suspicious_activity(ref_sheet, min_col_number, max_col_number,row_number, codes): 
    
   
    total = 0
    risk_total =0
    phases={}
    data = {}
    

    def init_activity(key, temp, info):
         if key not in temp.keys():
                    temp[key]={
                        'total': 0,
                        'transactions':0,
                        'clients':0,
                        'agregates':{},
                        'activity' : info['activity'] 
                    }
    def init_client(key, temp, info):
        if key not in temp.keys():
                    temp[key]={
                        'total': 0,
                        'transactions':0, 
                        # 'average':0 ,
                        'name': info['name'],
                        'lastname': info['lastname']
                    }
                    

    # if True:
    #     return data
   
    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
        activity= str(row[26].value)
        transaction = row[10].value
        monedad = row[11].value
        client_id = row[2].value.strip(' ')
        client = {
            'name' : row[3].value.strip(' '),
            'lastname' : row[4].value.strip(' '),
            
        }
        

        
        if monedad == "DOP": 
            if activity in codes.keys():
                # print(activity)
                info = codes[activity]
                total+=transaction
                init_activity(activity, data, info)
                data[activity]['total']+=transaction
                data[activity]['transactions']+=1

                init_client(client_id, data[activity]['agregates'], client )
                temp = data[activity]['agregates'][client_id]
                temp['total'] += transaction
                temp['transactions']+=1
                
            else:
                print(f"operation type not found {activity}")
        
            
    
    
    
    for activity in data.values():
        # print(activity)
        clients = len(activity['agregates'].keys())
        activity['clients'] = clients
        average = activity['total']/clients
        activity['average'] = average
        for t in activity['agregates'].values():
            t['average'] = t['total']/ t['transactions']
            t['avg_o_act_avg']= t['average'] > average
            t['total_o_act_avg']= t['total'] > average
    # if True:
    #     return data
    temp={
        "agregates" : data,
        "total": total,
        
    } 
     
    #TODO agregar total de las transacciones
    # agregar cuenta de cada tipo   

    return temp 