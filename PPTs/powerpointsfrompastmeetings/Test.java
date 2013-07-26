package animation;
import java.applet.Applet;
import java.awt.Graphics;
public class Test extends Applet
{
	Thread t;
	int x;
	public void init()
	{
		Runnable r = new Runner();
		t = new Thread(r);
		t.start();
	}
	public void paint(Graphics g)
	{
		setSize(800, 600);
		g.drawRect(x, 100, 50, 50);
	}
	class Runner implements Runnable
	{
		public void run()
		{
			while(true)
			{
				if(x < 750)
					x += 4;
				else
					break;
				try
				{
					Thread.sleep(50);
				}
				catch(InterruptedException ie)
				{
					System.err.println("There was an error.");
					System.exit(1);
				}
			}
		}
	}
}
