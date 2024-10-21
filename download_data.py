import requests, os, json
from datetime import datetime

def get_current_station_status(data_folder = 'data/') : 
    if not os.path.exists(data_folder) :
        os.mkdir(data_folder)
        
    time_str = datetime.now().strftime('%y%m%d%H%M')
    save_filename = f'{data_folder}station_status_{time_str}.json'
    
    req = requests.get('https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_status.json')
    if req.status_code != 200 :
        to_write = {
            'status': req.status_code,
        }
        err = req.raise_for_status()
        if err:
            to_write['error'] = string(err)
        with open(save_filename, 'w') as f:
            json.dump(to_write, f)
        return
    
    j = req.json()

    with open(save_filename, 'w') as f:
        json.dump(j['data']['stations'], f)

if __name__ =='__main__' :
    get_current_station_status()