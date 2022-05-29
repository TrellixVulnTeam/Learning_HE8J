public class Player {
    private String name;
    private double balance;

    public Player(String name) {
        this.name = name;
    }

    public void win(double bet) {
        this.balance += bet;
    }

    public void lose(double bet) {
        this.balance -= bet;
    }

    @Override
    public String toString() {
        return "Player{" +
                "name='" + name + '\'' +
                ", balance=" + balance +
                '}';
    }
}
