import requests, os, json
from datetime import datetime

data_folder = os.path.dirname(__file__) +'/data/'
def get_current_station_status(data_folder = data_folder) : 
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
            to_write['error'] = str(err)
        with open(save_filename, 'w') as f:
            json.dump(to_write, f)
        return
    
    j = req.json()

    with open(save_filename, 'w') as f:
        json.dump(j['data']['stations'], f)

def get_station_information(data_folder = data_folder):
    filepath = f'{data_folder}station_status.json'
    url = 'https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json'
    if os.path.exists(filepath):
        with open(filepath) as f:
            return json.load(f)['data']['stations']
    else:
        req = requests.get(url)
        if req.status_code == 200 :
            station_information = req.json()
            with open(filepath, 'w') as f:
                json.dump(station_information, f, indent=2)
            return station_information['data']['stations']
        else:
            raise Exception(f'Could not download: {req.raise_for_status()}')

if __name__ =='__main__' :
    get_current_station_status()
    get_station_information()