# Prog-11: Weather report (EP.2)
# 6?3?????21 Name ?

import json
import math

def top_K_max_temp_by_region(data, K):
    region=[]
    for i in data:
        for j in [data[i]['city']['region']]:
            if j not in region:
                region.append(j)
    region.sort()
    Maxtemp_dict={}
    for k in region:
        cpK=K
        alltemp=[]
        need=[]
        for i in data :
            if data[i]['city']['region'] == k:
                for j in range(len(data[i]['list'])):
                    alltemp.append((data[i]['list'][j]['main']['temp'],data[i]['city']['name'],data[i]['list'][j]['dt_txt']))
        alltemp.sort(reverse=True)
        c=0
        while(cpK!=0 and len(alltemp)!=0):
            if alltemp[c][0]==alltemp[c+1][0]:
                c+=1
            else:
                need.append(alltemp[c])
                alltemp.remove(alltemp[c])
                cpK-=1
                c=0
            
        Maxtemp_dict[k] = need
        
    return  Maxtemp_dict
  
def average_temp_by_date(data, region):
    alll=[]
    answer=[]
    for i in data :
        if data[i]['city']['region'] == region or region == 'ALL':
            date=[]
            
            for j in range(len(data[i]['list'])):
                if date.count(data[i]['list'][j]['dt_txt'][0:10]) == 0:
                    date.append(data[i]['list'][j]['dt_txt'][0:10])
                alll.append((data[i]['list'][j]['main']['temp'],data[i]['list'][j]['dt_txt'][0:10]))
            answer=[]

            avg_bydate=[0]*(len(date))
            counter=[0]*(len(date))
            
            for k in alll:
                avg_bydate[date.index(k[1])]+=k[0]
                counter[date.index(k[1])] += 1
            
            for i in range(len(avg_bydate)):
                avg_bydate[i] = avg_bydate[i]/counter[i] 
                answer.append((date[i],avg_bydate[i]))
            
            answer.sort()
    
    return answer

def max_rain_in_3h_periods(data, region, date):
    rain = [0.0]*8
    for i in data:
        if (data[i]['city']['region'] == region or region == 'ALL') :
            for j in range (len(data[i]['list'])):
                if(data[i]['list'][j]['dt_txt'][0:10] == date and type(data[i]['list'][j].get('rain')) == dict ):
                    if rain[int(data[i]['list'][j]['dt_txt'][11:13])//3] == 0:
                        rain[int(data[i]['list'][j]['dt_txt'][11:13])//3]=(data[i]['list'][j]['rain']['3h'])
                    if((data[i]['list'][j]['rain']['3h'])>rain[int(data[i]['list'][j]['dt_txt'][11:13])//3]):
                        rain[int(data[i]['list'][j]['dt_txt'][11:13])//3]=data[i]['list'][j]['rain']['3h']
                    
    answer=[]
    for i in range(0,24,3):
        answer.append((i,rain[i//3]))
    if rain == [0.0]*8:
        return [] 
    else:  
        return answer

def AM_PM_weather_description_by_region(data, date):
    allregion=[]
    result = {}
    for i in data:
        for j in [data[i]['city']['region']]:
            
            if j not in allregion:
                allregion.append(j)
                
    allregion.sort()
    for k in allregion:
        result[k]={}
        weatherAM=[];weatherPM=[]
        counterAM=[];counterPM=[]
        for i in data:
            for j in range(len(data[i]['list'])):
                for z in range(len(data[i]['list'][j]['weather'])):
                    if(data[i]['list'][j]['dt_txt'][0:10] == date and 0 <= int(data[i]['list'][j]['dt_txt'][11:13]) < 12 and data[i]['city']['region']==k):
                        if weatherAM.count(data[i]['list'][j]['weather'][z]['description']) == 0:
                            weatherAM.append(data[i]['list'][j]['weather'][z]['description'])
                            counterAM.append([0,data[i]['list'][j]['weather'][z]['description']])
                        else:
                            counterAM[weatherAM.index(data[i]['list'][j]['weather'][z]['description'])][0]+=1
                    if(data[i]['list'][j]['dt_txt'][0:10] == date and 12<= int(data[i]['list'][j]['dt_txt'][11:13]) <24 and data[i]['city']['region']==k):       
                        if weatherPM.count(data[i]['list'][j]['weather'][z]['description']) == 0:
                            weatherPM.append(data[i]['list'][j]['weather'][z]['description'])
                            counterPM.append([0,data[i]['list'][j]['weather'][z]['description']])
                        else:
                            counterPM[weatherPM.index(data[i]['list'][j]['weather'][z]['description'])][0]+=1 
        
        counterAM.sort(reverse=True)     
        counterPM.sort(reverse=True)
        x=0
        y=0
        while(counterAM !=[]):
            if counterAM[x][0]==counterAM[x+1][0]:
                x+=1
            else:
                result[k]["AM"]=counterAM[x][1]
                break
        while(counterPM !=[]):
            if counterPM[y][0]==counterPM[y+1][0]:
                y+=1
            else:
                result[k]["PM"]=counterPM[y][1]
                break 
    
    return result

def most_varied_weather_provinces(data):
    province=[]
    counterweather=[]
    weather_in_province=set()
    result = set()
    for i in data:
        for j in range(len(data[i]['list'])):
            weather_in_province.add(data[i]['list'][j]['weather'][0]['description'])
        province.append([len(weather_in_province),data[i]['city']['name']])    
        weather_in_province.clear()
    province.sort(reverse=True)
    c=0
    while(province != []):
        if province[c][0]==province[c+1][0]:
            c+=1
        else:
            for k in range(c,-1,-1):
                result.add(province[k][1])
            break
    return result

def main():
    # put your own testing codes in this function
    data = json.load(open('th_weather_39.json'))
    print(AM_PM_weather_description_by_region(data, '2021-04-09'))
main()

