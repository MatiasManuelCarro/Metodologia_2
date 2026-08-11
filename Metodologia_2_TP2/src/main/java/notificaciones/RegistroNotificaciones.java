package notificaciones;
import notificaciones.ErrorNotificacion;
import notificaciones.Notificacion;

import java.util.HashMap;
import java.util.Map;


public class RegistroNotificaciones {


    //hashmap con los tipos de comunicaciones
    private Map<String, Notificacion> registro = new HashMap<>();


    public void registrar(String tipo, Notificacion notificacion) {
        registro.put(tipo.toUpperCase(), notificacion);
    }


    //obtiene el tipo de notifacion
    public Notificacion obtener(String tipo) {
        return registro.getOrDefault(tipo.toUpperCase(), new ErrorNotificacion());
    }

    //envia el mensaje al tipo de comunicacion seteado
    public void enviar(String tipo, String mensaje) {
        Notificacion n = obtener(tipo);
        n.enviar(mensaje);
    }


}
