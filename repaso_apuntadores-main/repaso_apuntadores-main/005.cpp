#include <iostream>
#include <string>

using namespace std;

struct Alumno {
    string nombre;
    int notas[3];
};


int LeerNota(){
  int nota;
  do{
    cin >> nota;
  }while(nota<0||nota>50);
  return nota;
}

int main(){
  Alumno estudiantes[3];
  for( int i=0; i<3; i++){
    cout << "nombre de estudiante " << i << endl; 
    cin >> estudiantes[i].nombre;
    for( int j=0; j<3; j++){
      cout << "nota: " << j << endl;
      cin >> estudiantes[i].notas[j];
    }
  }

  
  Alumno* ptr[3];
  for(int i = 0 ; i < 3; i++){
    ptr[i] = &estudiantes[i];
  }  

  for(int i=0; i < 3; i++){
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