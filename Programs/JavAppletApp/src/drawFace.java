import java.awt.*;
import java.applet.Applet;
import java.util.Scanner;
import java.awt.geom.*;

public class drawFace extends Applet {
	int R, G, B;
	public void init() {
		Scanner cin = new Scanner(System.in);
		System.out.print("Input an R, G, and a B value with a space between: ");
		R = cin.nextInt();
		G = cin.nextInt();
		B = cin.nextInt();
	}
	public void paint(Graphics g) {
		setSize(800, 800);
		Graphics2D g2 = (Graphics2D) g;
		Ellipse2D e = new Ellipse2D.Double(100, 100, 500, 500);
		g2.setColor(new Color(R, G, B));
		g2.fill(e);
		g2.setColor(Color.black);
		e = new Ellipse2D.Double(200, 200, 50, 50);
		g2.fill(e);
		e = new Ellipse2D.Double(500, 200, 50, 50);
		g2.fill(e);
		e = new Ellipse2D.Double(225, 400, 300, 50);
		g2.fill(e);
	}
}
