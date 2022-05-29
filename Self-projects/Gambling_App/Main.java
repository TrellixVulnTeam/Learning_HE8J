import java.util.ArrayList;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        System.out.println("Hello, please enter number of players:");
        Scanner sc = new Scanner(System.in);
        int n_Players = Integer.parseInt(sc.nextLine());
        ArrayList<Player> players  = new ArrayList<>();

        for (int i = 0; i < n_Players; i ++) {
            System.out.println("Enter name: first one is banker");
            players.add(new Player(sc.nextLine()));
        }

        boolean exit = false;
        while(!exit ) {
            System.out.println("Round starts");
            System.out.println("Round ends, please enter your value");
            Player banker = players.get(0);
            for (int i = 1; i < n_Players; i++) {
                Player player = players.get(i);
                System.out.println(players.get(i) + "Enter your win/loss: ");
                String amount = sc.nextLine();
                if (amount.startsWith("-")) {
                    double bet = Double.parseDouble(amount.substring(1));
                    player.lose(bet);
                    banker.win(bet);
                } else {
                    player.win(Double.parseDouble(amount));
                    banker.lose(Double.parseDouble(amount));
                }
            }
            for (Player player : players) {
                System.out.println(player);
            }

            System.out.println("continue?");
            String line = sc.nextLine();
            if (line.equals("no")) {
                exit = true;
            }
        }



    }
}