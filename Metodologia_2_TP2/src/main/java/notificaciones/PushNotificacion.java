package notificaciones;

public class PushNotificacion implements Notificacion {
    @Override
    public void enviar(String mensaje) {
        System.out.println("Enviando Push Notification: " + mensaje);
    }
}