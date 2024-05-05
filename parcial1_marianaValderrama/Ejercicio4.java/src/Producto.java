public class Producto{

    String nombre;
    int codigo;
    int cantidad;
  
    public void setNombre(String nuevoNombre){
      nombre=nuevoNombre;
  
    }
  
    public void setCodigo(int nuevoCodigo){
      codigo=nuevoCodigo;
  
    }
  
    public void setCantidad(int nuevaCantidad){
     cantidad=nuevaCantidad; 
    }
  
    public int getCantidad(){
      return this.cantidad;
    }
    public String getNombre(){
      return this.nombre;
    }
    public int getCodigo(){
        return this.codigo;
    }
    
  }
