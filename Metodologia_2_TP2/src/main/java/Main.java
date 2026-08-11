import notificaciones.*;
/*import servicios.Notificador;*/
import servicios.Notificador;
import turnos.GestorTurnos;
import turnos.Paciente;

public class Main {

    public static void main(String[] args) {

        // Crear registro para guardar tipos de notificaciones
        RegistroNotificaciones registro = new RegistroNotificaciones();

        // registrando tipos de notificación
        registro.registrar("EMAIL", new EmailNotificacion());
        registro.registrar("SMS", new SmsNotificacion());
        registro.registrar("WHATSAPP", new WhatsappNotificacion());
        registro.registrar("TELEGRAM", new TelegramNotificacion());
        registro.registrar("PUSH", new PushNotificacion());

        // Crear notificador para enviar mensajes
        Notificador notificador = new Notificador(registro);

        // Crear gestor de turnos con una notificación inicial por defecto
        GestorTurnos gestor = new GestorTurnos(new EmailNotificacion());

        // Crear paciente de prueba
        Paciente p1 = new Paciente("Matías", 33);

        //Asignando turno nuevo (usa la comunicacion por defecto)
        System.out.println("\n....................................");
        System.out.println("\nMensaje con comunicacion del gestor por defecto");
        gestor.asignarTurno(p1);


        //cambio la notificacion del sistema a sms
        System.out.println("\n....................................");
        System.out.println("\nCambiando a SMS");
        gestor.setNotificacion(registro.obtener("SMS"));

        //Asignar turno nuevo, se envia por SMS
        gestor.asignarTurno(p1);


        System.out.println("\n....................................");
        System.out.println("\nCambiando a WhatsApp");
        gestor.setNotificacion(registro.obtener("WHATSAPP"));
        gestor.asignarTurno(p1);


        System.out.println("\n....................................");
        System.out.println("\nCambiando a Telegram");
        gestor.setNotificacion(registro.obtener("TELEGRAM"));
        gestor.asignarTurno(p1);

        System.out.println("\n....................................");
        System.out.println("\nCambiando a Push");
        gestor.setNotificacion(registro.obtener("PUSH"));
        gestor.asignarTurno(p1);

        System.out.println("\n....................................");
        System.out.println("\nProbando error");
        gestor.setNotificacion(registro.obtener("FAX"));
        gestor.asignarTurno(p1);

        System.out.println("\n....................................\n");
        // Envio de mensajes al usuario, utilizando notificador
        // se especifica metodo y se envia el mensaje.
        //Permite cambiar rapidamente de metodo de mensajes
        notificador.enviar("SMS", "Hola, " + p1 .getNombre()+ ", recorda que tenes un turno hoy!");
        notificador.enviar("WHATSAPP", "Hola, " + p1 .getNombre()+ ", recorda que tenes un turno hoy!");
        notificador.enviar("PUSH", "Hola, " + p1 .getNombre()+ ", recorda que tenes un turno hoy!");
        //FAX da error
        notificador.enviar("FAX", "Hola, " + p1 .getNombre()+ ", recorda que tenes un turno hoy!");
    }
}
