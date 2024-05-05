import java.util.Scanner;
import java.util.Random;
class Main{ 

public static void mostarAsientos(Boolean[][] mat){
    int num_filas,num_columnas;
    int i,j;
    i=0;
    j=0;
    num_filas =mat.length;//numero de filas
    num_columnas =mat[0].length;// numero de columnas
    for(i=0;i<num_filas;i=i+1){
        for(j=0;j<num_columnas;j=j+1){
            System.out.print(mat[i][j]+" ");
        }
     System.out.println("");
    }
}

public static void crearMatriz(Boolean[][] mat){
    int filas = mat.length;
    int columnas=mat[0].length;

    for (int i=0;i<filas;i++){
        for(int j=0;j<columnas;j++){
            mat[i][j]=generarBoleanos();
        }
    }
    mostarAsientos(mat);
}

public static boolean generarBoleanos(){
    return Math.random() <0.5;
}

public static void reservarAsientos(int fila , int asiento, Boolean[][] mat){
    if(mat[fila][asiento]==true){
        System.out.println("no se puede realizar la reserva, ya este asiento esta ocupado ");
    }else{
        mat[fila][asiento]=true;
        System.out.println("tu asiento fue reservdo con exito");
        mostarAsientos(mat);
    }
    
    
}
public static void cancelarReserva(int fila , int asiento, Boolean[][] mat){
    if(mat[fila][asiento]==true){
        System.out.println("tu asiento fue cancelado con exito");
        mat[fila][asiento]=false;
        mostarAsientos(mat);
    }else{
        mat[fila][asiento]=false;
        System.out.println("este asiento nunca fue reservado");
    }
    
    } 

    public  static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int m=0;
        int n=0;
        System.out.println("ingresa el numero de filas m");
        m=teclado.nextInt();
        System.out.println("ingresa el numero de columnas n ");
        n=teclado.nextInt();

        Boolean [][]matriz= new Boolean[m][n];
        crearMatriz(matriz);
        System.out.println("ingrese 1 para reservar o 2 para cancelar, 3 para salir");
        int opciones =teclado.nextInt();
        while (opciones>0 || opciones<4){ 
            if(opciones == 1){
                System.out.println("ingrese el numero de la fila que desea");
                int fila = teclado.nextInt();
                System.out.println("ingrese el numeor de la columna que desea reservar");
                int asiento= teclado.nextInt();
                reservarAsientos(fila, asiento, matriz); // Se añade el tercer argumento 'matriz'
                break;
            } else if(opciones == 2){
                System.out.println("ingrese el numero de la fila de su anterior asiento");
                int fila = teclado.nextInt();
                System.out.println("ingrese el numeor de la columna de su anterior asiento");
                int asiento= teclado.nextInt();
                cancelarReserva(fila, asiento, matriz);
                break;  
            }else if(opciones == 3){
                System.out.println("terminado");
                break;
            } else{
                System.out.println("ingrese un valor de opcion valida");
                break;
            }
        }
        
    }
}