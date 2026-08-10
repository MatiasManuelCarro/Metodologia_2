package notificaciones;
import notificaciones.ErrorNotificacion;
import notificaciones.Notificacion;

import java.util.HashMap;
import java.util.Map;


public class RegistroNotificaciones {


    private Map<String, Notificacion> registro = new HashMap<>();


    public void registrar(String tipo, Notificacion notificacion) {
        registro.put(tipo.toUpperCase(), notificacion);
    }


    public Notificacion obtener(String tipo) {
        return registro.getOrDefault(tipo.toUpperCase(), new ErrorNotificacion());
    }
}
