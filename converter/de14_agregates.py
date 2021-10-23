

def filter_total_zero(data):
    keys = list(data.keys())
    for k in keys:
        v= data[k]
        total = v['total']
        if total==0.0:
            del data[k]


def agregate_by_person_type(ref_sheet,type_col, amount_col, min_col_number, max_col_number,row_number, codes): 
    data={
    }
    risk_data={
        # "Alto":{"total":0},
        # "Bajo":{"total":0},
        # "Medio":{"total":0},
    }
    total = 0
    risk_total =0

    def init_risk(risk, data):
        if risk not in data.keys():
            risk_data[risk] = {
                "total":0,
                'amount':0
            }

    def init_data(k, data):
        if k not in data.keys():
            if k in codes.keys():
                val = codes[k]
                data[k]={
                    "total":0,
                    'user' : val['user'],
                    'risk' : val['risk'],
                    'amount':0
                }

    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
        userType= row[type_col].value
        transaction = str(row[amount_col].value).strip(' ')
        transaction = float(transaction)
        #print(f'{userType} {transaction}')
        
        if userType in codes.keys():
            init_data(userType, data)
            data[userType]["total"]+=transaction
            data[userType]["amount"]+=1
            total+=transaction
            risk = codes[userType]['risk']
            init_risk(risk, risk_data)
            # if risk in risk_data.keys():
            risk_data[risk]['total']+=transaction
            risk_data[risk]['amount']+=1
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

def agregate_by_single_col(ref_sheet, row_name, key_col, amount_col, 
    max_col_number,row_number, codes, ignore_key= False): 
    data={
    }
    total = 0
    def init_data(k, data):
        if k not in data.keys():
                val = codes[k]
                data[k]={
                    "total":0,
                    'amount':0,
                    row_name : val[row_name],
                }

    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=0):
        key= str(row[key_col].value)
        transaction = str(row[amount_col].value).strip(' ')
        transaction = float(transaction)

        #print(f"{key} {transaction}")
        # monedad = row[23].value
        if ignore_key:
            name= key
            key= key.replace("."," ")
            codes[key]= {
                row_name: name
            }
        
        if key in codes.keys():
            init_data(key, data)
            data[key]["total"]+=transaction
            data[key]['amount']+=1
            total+=transaction
        else:
            print(f"user type not found {key}")


    for t in data.values():
        t['perc']= t['total']/total*100
 
    temp={
        "agregates" : data,
        "total": total,
    } 
    

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

        break    

    # filter_total_zero(data)
    


    # for t in data.values():
    #     t['perc']= t['total']/total*100
    

       
    temp={
        "agregates" : data,
        "total": total,
        
    } 
    #TODO agregar total de las transacciones
    # agregar cuenta de cada tipo   

    return temp 





def agregate_by_services(ref_sheet,service_col, amount_col,  min_col_number, max_col_number,row_number, codes): 
    data={}
    total = 0
    risk_total =0
    phases={}
    def init_services(k, data):
        if k not in data.keys():
            val = codes[k]
            data[k]={
                "total":0,
                'service' : val['service'],
                'phase':val['phase'],
                'amount':0
            }
   
    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
        service= str(row[service_col].value)
        transaction = str(row[amount_col].value).strip(' ')
        transaction = float(transaction)
        # monedad = row[11].value
        #print(f'{service} {transaction}')
        
        if service in codes.keys():
            init_services(service, data)
            phase=  data[service]["phase"]
            data[service]["total"]+=transaction
            data[service]["amount"]+=1
            total+=transaction
            if phase not in phases.keys():
                phases[phase]={
                    'total': 0,
                    'amount':0
                }
            phases[phase]['total']+=transaction
            phases[phase]['amount']+=1

        else:
            print(f"operation type not found {service}")
    # filter_total_zero(data)
    # filter_total_zero(phases)
    for t in data.values():
        t['perc']= t['total']/total*100
    for t in phases.values():
        t['perc']= t['total']/total*100
       
    temp={
        "agregates" : data,
        "total": total,
        "phases": phases
    } 
    return temp 



def agregate_by_provinces(ref_sheet,service_col, amount_col,  min_col_number, max_col_number,row_number, codes): 
    data={}
    total = 0
    risk_total =0
    temp_risks={}
    risks= ["Delito Precedente 1","Delito Precedente 2",
    "Delito Precedente 3"]

    for risk in risks:
        temp_risks[risk]={
            'total':0,
            'agregates':{

            }
        }
    
    def init_delito(key, temp):
         if key not in temp.keys():
                    temp[key]={
                        'total': 0,
                    }
    def init_delito_by_locality(key, temp):
         name = codes[key]['nombre']
         if key not in temp.keys():
                    temp[key]={
                        'total': 0,
                        'nombre': name,
                        'amount':0
                    }
    

    def init_services(k, data):
        if k not in data.keys():
            if service in codes.keys():
                val = codes[k]
            else:
                val = {
                    'nombre': 'desconocido'
                }
            data[k]={
                "total":0,
                'nombre' : val['nombre'],
                'amount':0,
                'delitos': {}
            }
            for risk in risks:
                data[k]['delitos'][risk]={
                    'agregates':{}
                }

   
    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
        service= str(row[service_col].value)
        transaction = str(row[amount_col].value).strip(' ')
        transaction = float(transaction)
        # monedad = row[11].value
        service = service.strip(' ')
        diff = 6- len(service)
        if  diff> 0:
            s='0'*diff
            service = s+service

        init_services(service, data)
        # phase=  data[service]["phase"]
        # print(f" {service} {transaction}")
        data[service]["total"]+=transaction
        data[service]["amount"]+=1
        total+=transaction
        if service not in codes.keys():
             print(f"not found=> {service} {transaction}")

        else :
            temp = data[service]['delitos']
            #temp[service]['total']+=transaction
            for risk in risks:
                    r = codes[service][risk]
                    
                    if r is not None:
                        init_delito_by_locality(service, temp_risks[risk]['agregates'])
                        t=temp_risks[risk]['agregates'][service]
                        t['total'] += transaction
                        t['amount']+=1
                        temp_risks[risk]['total']+=transaction

                    if r is None:
                        r= 'Ninguno'
                    # init_delito(r, temp_risks[risk]['agregates'])
                    # t=temp_risks[risk]['agregates'][r]
                    # t['total'] += transaction

                    # init_delito(r, temp[risk]['agregates'])
                    # t=temp[risk]['agregates'][r]
                    # t['total'] += transaction
   
    # filter_total_zero(data)
    # filter_total_zero(phases)
    for t in data.values():
        t['perc']= t['total']/total*100
        temp = t['delitos']
        total_t = t['total']
        #print(total_t)
        for risk in risks:
            for d in temp[risk]['agregates'].values():
                d['perc']= d['total']/total_t*100

    for risk in risks:
        risk_total=temp_risks[risk]['total']
        for t in temp_risks[risk]['agregates'].values():
            t['perc']= t['total']/risk_total*100
       
    temp={
        "agregates" : data,
        "total": total,
        "risks": temp_risks
    } 
    return temp 





def agregate_by_economic_activity(ref_sheet, user_col, amount_col,  min_col_number, max_col_number,row_number, codes): 
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
        
        activity = str(row[user_col].value)
        transaction = str(row[amount_col].value).strip(' ')
        transaction = float(transaction)
        
        #print(f"{activity} {transaction} ")
        # activity = None
        # if user_id in user_codes.keys():
        #     activity = user_codes[user_id]['ciiu']
       
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
       
    } 
     
    #TODO agregar total de las transacciones
    # agregar cuenta de cada tipo   

    return temp 





def agregate_by_suspicious_activity(ref_sheet, user_col, amount_col, min_col_number, max_col_number,row_number, codes, user_codes): 
    
   
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
       
        transaction = row[amount_col].value
        client_id = row[user_col].value.strip(' ')
        client = {}
        activity = None
        if client_id in user_codes.keys():
            activity = user_codes[client_id]['ciiu']
            client = {
                'name' : user_codes[client_id]['name'],
                'lastname' : user_codes[client_id]['lastname'], 
            }
        
        # print(f"{activity}")
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
            print(f"operation type not found {activity} {client_id}")
        
            
    
    
    
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




def agregate_by_client_type(ref_sheet,type_col, amount_col, min_col_number, max_col_number,row_number, codes): 
    data={
    }
    risk_data={
        # "Alto":{"total":0},
        # "Bajo":{"total":0},
        # "Medio":{"total":0},
    }
    total = 0
    risk_total =0

    def init_risk(risk, data):
        if risk not in data.keys():
            risk_data[risk] = {
                "total":0,
                'amount':0
            }

    def init_data(k, data):
        if k not in data.keys():
            if k in codes.keys():
                val = codes[k]
                # print(val)
                data[k]={
                    "total":0,
                    'type' : val['type'],
                    'risk' : val['risk'],
                    'amount':0
                }

    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
        userType= str(row[type_col].value).strip(' ')
        transaction = str(row[amount_col].value).strip(' ')

        # print(f'{userType} {transaction}')
        transaction = float(transaction)
        
        
        if userType in codes.keys():
            init_data(userType, data)
            data[userType]["total"]+=transaction
            data[userType]["amount"]+=1
            total+=transaction
            risk = codes[userType]['risk']
            init_risk(risk, risk_data)
            # if risk in risk_data.keys():
            risk_data[risk]['total']+=transaction
            risk_data[risk]['amount']+=1
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


def agregate_by_average(ref_sheet, user_col, amount_col,name_col,other_col, min_col_number, max_col_number,row_number): 

    total = 0
    total_transactions =0
    risk_total =0
    phases={}
    data = {}
    def init_client(key, temp, info):
        if key not in temp.keys():
                    temp[key]={
                        'total': 0,
                        'amount':0, 
                        'name': info['name'],
                        'other': info['other']
                    }
                    
    for row in ref_sheet.iter_rows(min_row=row_number,
                            max_col=max_col_number,
                            min_col=min_col_number):
       
        transaction = str(row[amount_col].value).strip(' ')
        transaction = float(transaction)
        client_id = row[user_col].value.strip(' ')
        name = row[name_col].value.strip(' ')
        other=''
        if other_col>=0:
            other = str(row[other_col].value).strip(' ')

        #print(f'{client_id} {name} {transaction} {other}')
        # break
       
        client = {
            'name' : name,
            'other': other
        }
        init_client(client_id, data, client )
        total+=transaction
        total_transactions+=1
        data[client_id]['total']+=transaction
        data[client_id]['amount']+=1


            
            
      
        
            
    
    
    average = total/total_transactions
    for t in data.values():
        t['average'] = t['total']/ t['amount']
        t['avg_o_act_avg']= t['average'] > average
        t['total_o_act_avg']= t['total'] > average
    # if True:
    #     return data
    temp={
        "agregates" : data,
        "total": total,
        "average":average,
        "amount":total_transactions
        
    } 
     
    #TODO agregar total de las transacciones
    # agregar cuenta de cada tipo   

    return temp 