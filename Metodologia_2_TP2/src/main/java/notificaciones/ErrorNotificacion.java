package notificaciones;

public class ErrorNotificacion implements Notificacion {
    @Override
    public void enviar(String mensaje) {
        System.out.println("Tipo de notificación no soportado");
    }
}
