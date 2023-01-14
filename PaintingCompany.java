package week_18;


import java.text.DecimalFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import javax.swing.JOptionPane;

public class PaintingCompany {
	
	static int getRooms() {
		String rooms = JOptionPane.showInputDialog("How many rooms to paint?");
		int roomNum = Integer.parseInt(rooms);
		return roomNum;
	}
	
	static int getSquareFeet(int roomNum) {
		int totalSquareFeet = 0;
		for (int i = 0; i < roomNum; i++) {
			String sFeet = JOptionPane.showInputDialog("Enter the square feet for room number " + (i+1));
			int squareFeet = Integer.parseInt(sFeet);
			totalSquareFeet += squareFeet;
		}
			
		return totalSquareFeet;
	}
	
	static int getPricePerGallon() {
		
		String price = JOptionPane.showInputDialog("Enter the price of paint per gallon.");
		int pricePerGallon = Integer.parseInt(price);
		return pricePerGallon;
	}
	
	static int getGallons(int totalSquareFeet) {
		int gallons = totalSquareFeet / 115;
		return gallons;
	}

	static int getPaintCost(int pricePerGallon, int gallons) {
		int paintCost = pricePerGallon * gallons;
		return paintCost;
	}
	
	static int getHours(int gallons) {
		int hours = gallons * 8;
		return hours;
	}
	
	static double getLabor(double hours) {
		double labor = hours * 18;
		return labor;
	}
	
	static double getTotal(double labor, double paintCost) {
		double total = labor + paintCost;
		return total;
	}
	
	public static void main(String[] args) {
		
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy @ HH:mm"); // create a DateTimeFormatter object with the specified pattern
		LocalDateTime now = LocalDateTime.now(); // get the current date and time
	    String username = System.getProperty("user.name"); // get the username of the user running the program
		String currentDirect = System.getProperty("user.dir"); // get the current working directory
		
		
		
		// print out the current working directory
	    System.out.println("Working Directory " + currentDirect);
	    // print out the username of the user running the program
	    System.out.println("Programmer: " + username);
	    // print out the current date and time
	    System.out.println("Lab 18.2: " + dtf.format(now));
	    
	    int roomNum = getRooms();
	    int totalSquareFeet = getSquareFeet(roomNum);
	    int pricePerGallon = getPricePerGallon();
	    int gallons = getGallons(totalSquareFeet);
	    int paintCost = getPaintCost(pricePerGallon, gallons);
	    int hours = getHours(gallons);
	    double labor = getLabor(hours);
	    double total = getTotal(labor, paintCost);
	    DecimalFormat df = new DecimalFormat(".00");
	    JOptionPane.showMessageDialog(null, "The total estimated cost is $" + df.format(total));

	    
	    
	    
	     
	}
}

