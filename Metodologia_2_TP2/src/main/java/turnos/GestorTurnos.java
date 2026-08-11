package turnos;

import notificaciones.Notificacion;

public class GestorTurnos {

    private Notificacion notificacion;

    public GestorTurnos(Notificacion notificacion) {
        this.notificacion = notificacion;
    }

    public void asignarTurno(Paciente paciente) {

        String mensaje = "Turno asignado a " + paciente.toString();

        notificacion.enviar(mensaje);
    }

    //establece la notificacion por defecto del gestor, permitiendo al sistema cambiar de metodo
    public void setNotificacion(Notificacion nuevaNotificacion) {
        this.notificacion = nuevaNotificacion;
    }
}