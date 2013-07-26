package animation;
import java.applet.Applet;
import java.util.ArrayList;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;
public class DotApplet extends Applet
{
	ArrayList<Ellipse2D.Double> list = new ArrayList<Ellipse2D.Double>();
	public void init()
	{
		MouseListener ml = new MouseSensor();
		addMouseListener(ml);
	}
	public void paint(Graphics g)
	{
		setSize(800, 600);
		Graphics2D g2 = (Graphics2D) g;
		int index = 0;
		while(index < list.size())
		{
			Ellipse2D.Double e = list.get(index);
			g2.fill(e);
			index++;
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
			int x = e.getX();
			int y = e.getY();
			Ellipse2D.Double e2 = new Ellipse2D.Double(x - 3, y - 3, 6, 6);
			list.add(e2);
			repaint();
		}
	}
}
