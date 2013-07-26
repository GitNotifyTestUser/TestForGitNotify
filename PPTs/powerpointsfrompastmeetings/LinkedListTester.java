package linkedlist;

public class LinkedListTester
{
	public static void main(String[] args)
	{
		ListNode first = new ListNode("Seven");
		first.setNext(new ListNode("Minute"));
		first.getNext().setNext(new ListNode("Warning"));
		/*ListNode current = first;
		while(current != null)
		{
			System.out.println(current.getValue());
			current = current.getNext();
		}*/
		System.out.println(first);
	}
}
