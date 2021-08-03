import os

#os.chdir('C:\\Users\\BAJAME')
#print(os.getcwd())

#os.path.abspath(dir)

#for key in os.environ.keys():
#    print(key);

import pdb


def condicion(elem,pista):
    loc_pista = elem.find(pista) # localizaciòn de la pista
    return loc_pista != -1;

def find_file_pista (dir,pistas,condicion):
    list_phats = [];
    for satelite in pistas:
        #pdb.set_trace()
        pista = pistas[satelite]["pista"];
        for elem in os.listdir(dir):
            if condicion(elem,pista):
               path_elem = os.path.join(dir,elem)
               pistas[satelite]["path"] = path_elem
               list_phats.append(path_elem)
               break
    return list_phats

def identificar_satelite (pistas,satelite):
    return int(pistas[satelite]["nombre"][-1])

pistas = {
    "satelite1":{
        "nombre":"VRSS-1",
        "pista":'OMS_TDRS_VRSS-1',
        "path": None },

    "satelite2": {
       "nombre":"VRSS-2",
       "pista": 'OMS_TDRS_VRSS-2',
       "path":None }
    }


if __name__ == '__main__':

    dir = 'C:\\Users\\BAJAME\\Anaconda3\\envs\\updatestkescenario\\mapp\\updatestkescenario\\EPH'
    list_phats = find_file_pista(dir,pistas,condicion);
    for satelite in pistas:
        #pdb.set_trace()
        file_eph = pistas[satelite]["path"]
        n_satelite = identificar_satelite(pistas,satelite);

    print(list_phats)
    print(pistas)

    #for satelite in pistas:
    #    print(pistas[satelite]["path"])


