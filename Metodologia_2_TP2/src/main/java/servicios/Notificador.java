package servicios;

import notificaciones.*;

import java.util.Map;

public class Notificador {

    private Map<String, Notificacion> tipoNotificacion;

    public Notificador() {
        tipoNotificacion = Map.of(
                "EMAIL", new EmailNotificacion(),
                "SMS", new SmsNotificacion(),
                "WHATSAPP", new WhatsappNotificacion(),
                "TELEGRAM", new TelegramNotificacion(),
                "PUSH", new PushNotificacion()
        );
    }

    public void enviar(String tipo, String mensaje) {
        tipoNotificacion
                .getOrDefault(tipo, new ErrorNotificacion())
                .enviar(mensaje);
    }
}