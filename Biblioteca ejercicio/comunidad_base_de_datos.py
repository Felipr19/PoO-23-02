class ComunidadBaseDeDatos:
    
    def cargar_bases_de_datos (self): #el self va a ser de consultas ej: consulta_1()
        
        estudiantes_datos = dict()
        docentes_datos = dict()
        administrativos_datos = dict()
    
        with open('Bases de Datos\Administrativos_base_de_datos.txt', 'r') as administrativos_base_datos:
            
            for reading_administrativos in administrativos_base_datos.readlines(): 
                spliter = reading_administrativos.split(',')   
                administrativos_datos[spliter[1]] = reading_administrativos #[1] es el nombre
        
        with open('Bases de Datos\Estudiantes_base_de_datos.txt', 'r') as estudiantes_base_datos:
            
            for reading_estudiantes in estudiantes_base_datos.readlines():
                spliter = reading_estudiantes.split(',')
                estudiantes_datos[1] = reading_estudiantes
        
        with open('Bases de Datos\Docentes_base_de_datos.txt', 'r') as docentes_base_datos:
            
            for reading_docentes in docentes_base_datos.readlines():
                spliter = reading_estudiantes.split(',')
                docentes_datos[1] = reading_docentes
        
    def añadir_administrativo_docente_estudiante(self, cargo ,datos):  #datos-> tuple, cargo separado por comas-> str
        with open ('Bases de Datos\{cargo}_base_de_datos.txt'.format(cargo= cargo), 'w') as añadidor_de_comunidad:

            añadidor_de_comunidad.write(("{cargo}, {datos}").format(cargo= cargo, datos= datos))
          
            

            
if __name__ == '__main__':
    consulta = ComunidadBaseDeDatos()
    consulta.añadir_administrativo_docente_estudiante("Docentes", "Santiago, Ingenieria de sistemas")
    consulta.cargar_bases_de_datos()
            
    