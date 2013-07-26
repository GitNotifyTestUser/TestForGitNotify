package mouse;
import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Color;
import java.awt.geom.Rectangle2D;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
public class MouseTest extends Applet
{
	Color rectColor;
	public void init()
	{
		MouseSensor ms = new MouseSensor();
		addMouseListener(ms);
		rectColor = Color.BLACK;
	}
	public void paint(Graphics g)
	{
		Graphics2D g2 = (Graphics2D) g;
		setSize(800, 600);
		g2.setColor(rectColor);
		g2.fill(new Rectangle2D.Double(100, 100, 100, 100));
	}
	class MouseSensor implements MouseListener
	{
		public void mouseClicked(MouseEvent e)
		{
		}
		public void mouseEntered(MouseEvent e)
		{
			rectColor = Color.BLACK;
			repaint();
		}
		public void mouseExited(MouseEvent e)
		{
			rectColor = Color.WHITE;
			repaint();
		}
		public void mousePressed(MouseEvent e)
		{
			int mouseX = e.getX();
			int mouseY = e.getY();
			if(100 < mouseX && 200 > mouseX && 100 < mouseY && 200 > mouseY)
				rectColor = Color.RED;
			repaint();
		}
		public void mouseReleased(MouseEvent e)
		{
			int mouseX = e.getX();
			int mouseY = e.getY();
			if(100 < mouseX && 200 > mouseX && 100 < mouseY && 200 > mouseY)
				rectColor = Color.BLUE;
			repaint();
		}
	}
}
