package animation;
import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;
public class CircleAnimation extends Applet
{
	Thread t;
	int x = 100;
	boolean isMoving = false;
	public void init()
	{
		Runnable r = new Runner();
		t = new Thread(r);
		t.start();
		MouseListener m = new MouseSensor();
		addMouseListener(m);
	}
	public void paint(Graphics g)
	{
		setSize(800, 600);
		Graphics2D g2 = (Graphics2D) g;
		Rectangle2D box = new Rectangle2D.Double(x, 100, 100, 100);
		g2.draw(box);
	}
	class Runner implements Runnable
	{
		public void run()
		{
			while(true)
			{
				if(isMoving)
					x += 2;
				try
				{
					Thread.sleep(25);
				}
				catch (InterruptedException e)
				{
					System.err.println("There was an error.");
				}
				repaint();
			}
		}
	}
	class MouseSensor implements MouseListener
	{

		@Override
		public void mouseClicked(MouseEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseEntered(MouseEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseExited(MouseEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mousePressed(MouseEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseReleased(MouseEvent e)
		{
			int xC = e.getX();
			int yC = e.getY();
			if(xC >= x && xC <= x + 100 && yC >= 100 && yC <= 200)
			{
				isMoving = !isMoving;
			}
		}
		
	}
}
