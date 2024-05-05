import java.util.Scanner;
public class ejercicio2 {

    public static void VerCitas (CitasMedicas[]medico){
        for(int i=0;i<medico.length;i++){
            if(medico[i]==null){
                System.out.println(" no tiene citas asignadas");
            }else{
                System.out.println("el nombre es: "+medico[i].getPaciente()+" la cita es a las:  "+medico[i].getHora()+" con el medico: "+medico[i].getMedico());
            }
        }
        
    }

    public static void asignarCitas(CitasMedicas[]medico,String nombre, int hora, String paciente){
        for(int i=0 ;i<medico.length;i++){
           if(medico[i]==null){
                CitasMedicas nuevaCita=new CitasMedicas(nombre,hora,paciente);
                medico[i]=nuevaCita;
                break;
           }else if(medico[i].getHora()==hora){
            System.out.println("esta hora ya esta reservada");
            }
        }
        VerCitas(medico);
    }

    public static void cancelacion(CitasMedicas[]medico,int hora){
        boolean cancelo=false;
        for(int i =0;i<medico.length;i++){
            
            if(medico[i]!=null && medico[i].getHora()==hora){
                medico[i]=null;
                cancelo=true;
            }
        }
        if(cancelo==false){
            System.out.println("en ese horario nunca hubo una cita asiganda");
        }
        VerCitas(medico);
    }

    public static void main(String[] args) throws Exception {
        Scanner teclado= new Scanner (System.in);
        CitasMedicas[] arrayMedico1 = new CitasMedicas[8];
        CitasMedicas[] arrayMedico2 = new CitasMedicas[8];
        CitasMedicas[] arrayMedico3 = new CitasMedicas[8];
        

        CitasMedicas paciente1 = new CitasMedicas("laura",2,"jose garcia");
        CitasMedicas paciente2 = new CitasMedicas("juan",1,"diego suarez");
        CitasMedicas paciente3 = new CitasMedicas("mario",3,"manuela davila");
        arrayMedico1[0]=paciente1;
        arrayMedico2[0]=paciente2;
        arrayMedico3[0]=paciente3;
        int opciones=0;
        System.out.println("ingrese 1 para asignar cita, 2 ver disponibilidad del medico , 3 cancelar cita");
        opciones=teclado.nextInt();
        teclado.nextLine();
        while(opciones>0||opciones<4){
            if(opciones==1){
                int doctor=0;
                System.out.println("ingrese 1 para asignar con la doctora laura, 2 con el doctor juan , 3 con el doctor mario");
                doctor=teclado.nextInt();
                if(doctor==1){
                    int hora=0;
                    String paciente="";
                    System.out.println("ingrese la hora (numero entero) en la que desea la cita ");
                    hora=teclado.nextInt();
                    teclado.nextLine();
                    System.out.println("ingrese el nombre del paciente ");
                    paciente=teclado.nextLine();
                    asignarCitas(arrayMedico1,"laura",hora,paciente);
                    
                }else if(doctor==2){
                    int hora=0;
                    String paciente="";
                    System.out.println("ingrese la hora (numero entero) en la que desea la cita ");
                    hora=teclado.nextInt();
                    System.out.println("ingrese el nombre del paciente ");
                    paciente=teclado.nextLine();
                    asignarCitas(arrayMedico2,"juan",hora,paciente);
                    
                }else if (doctor==3){
                    int hora=0;
                    String paciente="";
                    System.out.println("ingrese la hora (numero entero) en la que desea la cita ");
                    hora=teclado.nextInt();
                    System.out.println("ingrese el nombre del paciente ");
                    paciente=teclado.nextLine();
                    asignarCitas(arrayMedico3,"mario",hora,paciente);
                
                }
                break;
    
            }else if(opciones==2){
                int doctor=0;
                System.out.println("ingrese 1 para ver disponibilidad con la doctora laura, 2 con el doctor juan , 3 con el doctor mario");
                doctor=teclado.nextInt();
                if(doctor==1){
                    VerCitas(arrayMedico1);
                }else if(doctor==2){
                    VerCitas(arrayMedico2);  
                }else if (doctor==3){
                    VerCitas(arrayMedico3);
                }
                break;

            }else if (opciones==3){
                int doctor=0;
                int hora=0;
                System.out.println("ingrese 1 para cancelar con la doctora laura, 2 con el doctor juan , 3 con el doctor mario");
                doctor=teclado.nextInt();
                if(doctor==1){
                    System.out.println("ingrese la hora (numero entero) en la que tenia su cita");
                    hora=teclado.nextInt();
                    cancelacion(arrayMedico1,hora);
                }else if(doctor==2){
                    System.out.println("ingrese la hora (numero entero) en la que tenia su cita");
                    hora=teclado.nextInt();
                    cancelacion(arrayMedico2,hora);  
                }else if (doctor==3){
                    System.out.println("ingrese la hora (numero entero) en la que tenia su cita");
                    hora=teclado.nextInt();
                    cancelacion(arrayMedico3,hora);
                }
                break;
            }else{
                System.out.println("ingrese un valor de opcion valido");
                break;
            }
        }
       

        



    }
}
