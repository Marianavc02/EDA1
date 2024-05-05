import java.util.ArrayList;
import java.util.Scanner;
public class Main{ 
    static ArrayList<Producto> productos=new ArrayList<Producto>();
    public static void agregarProducto(Producto productoParaAgregar){
        if(buscarProducto(productoParaAgregar.getCodigo())==true){
            System.out.println("ese codigo ya existe");
        }else{
            productos.add(productoParaAgregar);
            imprimir();
        }
    
    }

    public static boolean buscarProducto(int codigo){
        for (Producto producto:productos){
            if(producto.getCodigo()==codigo){
                System.out.println("el nombre del producto es: "+producto.getNombre()+" la cantidad en stock es: "+producto.getCantidad()+" el codigo es: "+producto.getCodigo());
                return true;
            }else{
                System.out.println("no hay registro de este producto");
            }
            
        }
        return false;
    }

    public static void actualizarStock(int codigo, int cantidad ){
        for (Producto producto:productos){
            if(cantidad<0){
                System.out.println("no se puede actualizar el stock");
            }else if(producto.getCodigo()==codigo){
                producto.setCantidad(cantidad);
                imprimir();
            }
            
            }
        }

    public static void imprimir(){
        for (Producto producto:productos){
            System.out.println("el nombre del producto es: "+producto.getNombre()+" la cantidad en stock es: "+producto.getCantidad()+" el codigo es: "+producto.getCodigo()); 
        }
    }
    


    public static void main(String[] args) throws Exception {
        Scanner teclado=new Scanner(System.in);
        Producto camisa=new Producto();
        camisa.setNombre("camisa");
        camisa.setCodigo(123);
        camisa.setCantidad(10);
        agregarProducto(camisa);
        buscarProducto(123);
        int opciones=0;
        System.out.println("ingrese 1 para agregar un producto , 2 para actualizar el stock , 3 para buscar un producto");
        opciones=teclado.nextInt();
        teclado.nextLine();
        while(opciones>0||opciones<4){ 
            if(opciones==1){
                System.out.println("ingrese nombre");
                String nombre = teclado.nextLine();
                System.out.println("ingrese codigo");
                int codigo = teclado.nextInt();
                System.out.println("ingrese cantidad");
                int cantidad = teclado.nextInt();
                
                Producto nuevoProducto=new Producto();
                nuevoProducto.setNombre(nombre);
                nuevoProducto.setCodigo(codigo);
                nuevoProducto.setCantidad(cantidad);
                agregarProducto(nuevoProducto);
                break;
            }else if(opciones==2){
                int codigo=0;
                int cantidad=0;
                System.out.println("ingresa el codigo del producto para actualizar el Stock");
                codigo=teclado.nextInt();
                System.out.println("ingrese el nuevo Stock del producto");
                cantidad=teclado.nextInt();
                actualizarStock(codigo, cantidad);
                break;
            }else if(opciones==3){
                int codigo=0;
                System.out.println("ingresa el codigo del producto para actualizar el Stock");
                codigo=teclado.nextInt();
                buscarProducto(codigo);
                break;
            }else{
                System.out.println("ingrese una opcion valida");
                break;
            }


        }
    }
    
}
