#include <iostream>
#include <string>

using namespace std;

struct Alumno {
    string nombre;
    int notas[3];
};


int LeerNota(){                            /*funcion para leeer nota*/
  int nota;
  do{
    cin >> nota;
  }while(nota<0||nota>50);
  return nota;
}

int main(){
  int n=3;                                /*cantidad de estudiantes*/
  Alumno estudiantes[n];                  /*arreglo para registrar los estudiantes*/
  for( int i=0; i<n; i++){
    cout << "nombre de estudiante " << i << endl; 
    cin >> estudiantes[i].nombre;
    for( int j=0; j < 3; j++){
      cout << "nota: " << j << endl;
      cin >> estudiantes[i].notas[j];
    }
  }

  
  Alumno* ptr[n];                         /*apuntador del arreglo*/
  for(int i = 0 ; i < n; i++){
    ptr[i] = &estudiantes[i];
  }  

  for(int i=0; i < n; i++){               /*imprime los datos de cada uno*/ 
    cout << endl;
    cout << "Datos del estudiante "<< i << endl;
    cout << "Nombre : " << ptr[i]->nombre << endl;
    cout << "Notas del estudiante : ";
    for(int j = 0; j < 3; j++){
      cout << ptr[i]->notas[j] << "\t";
    }
    cout << endl;
  }
  cout<<endl;
  
    return 0;
}