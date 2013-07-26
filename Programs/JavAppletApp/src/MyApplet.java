import java.applet.Applet;
import java.util.*;

//import java.awt.Graphics;
//import java.awt.Graphics2D;
//import java.awt.Rectangle;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Scanner;
public class MyApplet extends Applet implements MouseListener {
	public void paint(Graphics g) {
		addMouseListener(this);
		
		Scanner s = new Scanner(System.in);
		int R, G, B;
		System.out.print("Input a R value: ");
		R = s.nextInt();
		System.out.print("Input a G value: ");
		G = s.nextInt();
		System.out.print("Input a B value: ");
		B = s.nextInt();
		Graphics2D g2 = (Graphics2D) g;
		g2.setColor(new Color(R, G, B));
		int x = 10;
		int y = 10;
		int w = 42;
		int h = 12;
		Rectangle r = new Rectangle(x, y, w, h);
		g2.fill(r);
	}

	@Override
	public void mouseClicked(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent arg0) {
		// TODO Auto-generated method stub
	}

	@Override
	public void mouseExited(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mousePressed(MouseEvent arg0) {
		// TODO Auto-generated method stub
		System.out.println("hi");
	}

	@Override
	public void mouseReleased(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}
}
