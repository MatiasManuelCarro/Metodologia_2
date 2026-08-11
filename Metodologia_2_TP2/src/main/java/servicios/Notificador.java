package servicios;

import notificaciones.Notificacion;
import notificaciones.RegistroNotificaciones;

public class Notificador {

    private RegistroNotificaciones registro;

    public Notificador(RegistroNotificaciones registro) {
        this.registro = registro;
    }

    public void enviar(String tipo, String mensaje) {
        Notificacion n = registro.obtener(tipo);
        n.enviar(mensaje);
    }
}