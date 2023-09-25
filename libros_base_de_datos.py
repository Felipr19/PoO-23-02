class BaseDeDatosLibros:
    facultad_ingenieria_libros = dict()
    facultad_medio_ambiente_libros = dict()
    facultad_educacion_libros = dict()
            
    with open ('Bases de Datos\Inventario_libros.txt', 'r') as Inventario_Libros:
        for loading_books_by_faculties in Inventario_Libros.readlines():

            splited = loading_books_by_faculties.split(',')

            #Upload the books to dictionaries
            if splited[0] == 'Ingenieria':
                facultad_ingenieria_libros[splited[1]] = splited
            elif splited[0] == 'Medio Ambiente':
                facultad_medio_ambiente_libros[splited[1]] = splited
            elif splited[0] == 'Educacion':
                facultad_educacion_libros[splited[1]] = splited

        print('-----Libros Ingenieria-----')
        print(facultad_ingenieria_libros)
            
            
if __name__ == '__main__':
    consulta = BaseDeDatosLibros()
    