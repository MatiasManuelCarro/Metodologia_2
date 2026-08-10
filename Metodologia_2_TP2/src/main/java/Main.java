import notificaciones.*;
import servicios.Notificador;
import turnos.GestorTurnos;
import turnos.Paciente;

public class Main {

    public static void main(String[] args) {

        // Crear registro
        RegistroNotificaciones registro = new RegistroNotificaciones();

        // registrando tipos de notificación
        registro.registrar("EMAIL", new EmailNotificacion());
        registro.registrar("SMS", new SmsNotificacion());
        registro.registrar("WHATSAPP", new WhatsappNotificacion());
        registro.registrar("TELEGRAM", new TelegramNotificacion());
        registro.registrar("PUSH", new PushNotificacion());


        // Crear gestor de turnos con una notificación inicial
        GestorTurnos gestor = new GestorTurnos(new EmailNotificacion());

        // Crear paciente de prueba
        Paciente paciente = new Paciente("Matías", 33);

        System.out.println("\n....................................");
        System.out.println("\nPrueba con Email");
        gestor.asignarTurno(paciente);

        System.out.println("\n....................................");
        System.out.println("\nCambiando a SMS");
        gestor.setNotificacion(registro.obtener("SMS"));
        gestor.asignarTurno(paciente);

        System.out.println("\n....................................");
        System.out.println("\nCambiando a WhatsApp");
        gestor.setNotificacion(registro.obtener("WHATSAPP"));
        gestor.asignarTurno(paciente);

        System.out.println("\n....................................");
        System.out.println("\nCambiando a Telegram");
        gestor.setNotificacion(registro.obtener("TELEGRAM"));
        gestor.asignarTurno(paciente);

        System.out.println("\n....................................");
        System.out.println("\nCambiando a Push");
        gestor.setNotificacion(registro.obtener("PUSH"));
        gestor.asignarTurno(paciente);

        System.out.println("\n....................................");
        System.out.println("\nProbando error");
        gestor.setNotificacion(registro.obtener("FAX"));
        gestor.asignarTurno(paciente);
    }
}
