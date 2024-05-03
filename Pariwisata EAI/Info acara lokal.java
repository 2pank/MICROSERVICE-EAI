import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class LocalEvent {
    private String name;
    private String description;
    private String date;
    private String venue;

    public LocalEvent(String name, String description, String date, String venue) {
        this.name = name;
        this.description = description;
        this.date = date;
        this.venue = venue;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public String getDate() {
        return date;
    }

    public String getVenue() {
        return venue;
    }
}

class LocalEventInformationSystem {
    private Map<String, LocalEvent> events;

    public LocalEventInformationSystem() {
        events = new HashMap<>();
    }

    public void addEvent(String name, String description, String date, String venue) {
        events.put(name, new LocalEvent(name, description, date, venue));
    }

    public void displayEvents() {
        System.out.println("Local Events:");
        for (LocalEvent event : events.values()) {
            System.out.println("Name: " + event.getName());
            System.out.println("Description: " + event.getDescription());
            System.out.println("Date: " + event.getDate());
            System.out.println("Venue: " + event.getVenue());
            System.out.println();
        }
    }

    public LocalEvent getEvent(String name) {
        return events.get(name);
    }
}

public class Main {
    public static void main(String[] args) {
        LocalEventInformationSystem eventInformationSystem = new LocalEventInformationSystem();
        
        // Menambahkan acara lokal
        eventInformationSystem.addEvent("Local Music Concert", "Enjoy a night of live music by local bands.", "2024-05-20", "City Park");
        eventInformationSystem.addEvent("Art Exhibition", "View stunning artworks by local artists.", "2024-06-10", "Art Gallery");
        eventInformationSystem.addEvent("Food Festival", "Taste delicious local cuisine from various vendors.", "2024-07-15", "Downtown Square");

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Welcome to Local Event Information System!");
            System.out.println("1. Display Events");
            System.out.println("2. Get Event Information");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    eventInformationSystem.displayEvents();
                    break;
                case 2:
                    System.out.print("Enter event name: ");
                    scanner.nextLine(); // Clear the buffer
                    String eventName = scanner.nextLine();
                    LocalEvent event = eventInformationSystem.getEvent(eventName);
                    if (event != null) {
                        System.out.println("Name: " + event.getName());
                        System.out.println("Description: " + event.getDescription());
                        System.out.println("Date: " + event.getDate());
                        System.out.println("Venue: " + event.getVenue());
                    } else {
                        System.out.println("Event not found!");
                    }
                    break;
                case 3:
                    System.out.println("Exiting...");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}
