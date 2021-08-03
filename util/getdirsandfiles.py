import os
import pdb

class get_dirs_files():
    
    def get_dirs(self, dir_escenarios):
       #dir_escenarios = "D:\\Mis documentos\\Jorge\\ABAE\\OMS\\Escenaros_2"
      
       with os.scandir(dir_escenarios) as ficheros:
          subdirectorios = [fichero.name for fichero in ficheros 
          if fichero.is_dir()]

          _subdirectorios = [os.path.join( dir_escenarios, subdirectorio) for subdirectorio in subdirectorios]
       
       return _subdirectorios

    def get_file_ext(self, subdirectorio, ext='.sc', type_path="relativa"):
         
        with os.scandir(subdirectorio) as ficheros:
             ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith(ext)]
        
        if type_path == "relativa":
            _ficheros = [os.path.join( subdirectorio, fichero) for fichero in ficheros]
        elif type_path == "absoluta":
            _ficheros = ficheros
        else:
            _ficheros = None
        
        return _ficheros

    def get_files_ext(self, subdirectorios, ext='.sc'):
        
        ficheros = []
        for subdirectorio in subdirectorios:
            fichero = self.get_file_ext(subdirectorio,ext,type_path="relativa")
            if len(fichero) > 0:
                ficheros += fichero
        return ficheros
            

if __name__ == "__main__":
    
    buscador = get_dirs_files()
    dir_escenarios = "D:\\Mis documentos\\Jorge\\ABAE\\OMS\\Escenaros_2"
    subdirectorios = buscador.get_dirs(dir_escenarios) 
    print(subdirectorios)

    subdirectorio = subdirectorios[0]
    subdirectorio = os.path.join(dir_escenarios,subdirectorio)
    fichero_sc = buscador.get_file_ext(subdirectorio)
    print(fichero_sc)

    ficheros_sc = buscador.get_files_ext(subdirectorios, ext='.sc')
    print(ficheros_sc)

