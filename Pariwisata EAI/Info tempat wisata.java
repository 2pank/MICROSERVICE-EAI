import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class TouristAttraction {
    private String name;
    private String description;

    public TouristAttraction(String name, String description) {
        this.name = name;
        this.description = description;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }
}

class TouristInformationSystem {
    private Map<String, TouristAttraction> attractions;

    public TouristInformationSystem() {
        attractions = new HashMap<>();
    }

    public void addAttraction(String name, String description) {
        attractions.put(name, new TouristAttraction(name, description));
    }

    public void displayAttractions() {
        System.out.println("Tourist Attractions:");
        for (TouristAttraction attraction : attractions.values()) {
            System.out.println("Name: " + attraction.getName());
            System.out.println("Description: " + attraction.getDescription());
            System.out.println();
        }
    }

    public TouristAttraction getAttraction(String name) {
        return attractions.get(name);
    }
}

public class Main {
    public static void main(String[] args) {
        TouristInformationSystem touristInformationSystem = new TouristInformationSystem();
        
        // Menambahkan tempat-tempat wisata
        touristInformationSystem.addAttraction("Eiffel Tower", "A wrought-iron lattice tower on the Champ de Mars in Paris.");
        touristInformationSystem.addAttraction("Statue of Liberty", "A colossal neoclassical sculpture on Liberty Island in New York Harbor.");
        touristInformationSystem.addAttraction("Taj Mahal", "An ivory-white marble mausoleum on the right bank of the Yamuna river in Agra.");

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Welcome to Tourist Information System!");
            System.out.println("1. Display Attractions");
            System.out.println("2. Get Attraction Information");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    touristInformationSystem.displayAttractions();
                    break;
                case 2:
                    System.out.print("Enter attraction name: ");
                    scanner.nextLine(); // Clear the buffer
                    String attractionName = scanner.nextLine();
                    TouristAttraction attraction = touristInformationSystem.getAttraction(attractionName);
                    if (attraction != null) {
                        System.out.println("Name: " + attraction.getName());
                        System.out.println("Description: " + attraction.getDescription());
                    } else {
                        System.out.println("Attraction not found!");
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
