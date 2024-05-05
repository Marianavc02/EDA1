public class CitasMedicas {
    public String medico;
    public int hora;
    public String paciente;

    public CitasMedicas(){
        medico = " ";
        hora = 0;
        paciente = " ";
      }

    public CitasMedicas(String medico,int hora,String paciente){
        this.medico=medico;
        this.hora=hora;
        this.paciente=paciente;
    }

    public void VerCitas (){
        
        System.out.println("el nombre es: "+getPaciente()+" la cita es a las:  "+getHora()+" con el medico: "+getMedico());
    }
    public void setMedico(String nombre){
        this.medico=nombre;
    }

    public String getMedico(){
        return medico;
    }

    public void setHora(int hora){
        this.hora=hora;
    }

    public int getHora(){
        return hora;
    }

    public void setPaciente(String paciente){
        this.paciente=paciente;
    }
    public String getPaciente(){
        return paciente;
    }
    

    
}
