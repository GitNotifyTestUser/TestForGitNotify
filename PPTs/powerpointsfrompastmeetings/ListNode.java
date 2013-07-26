package linkedlist;

public class ListNode
{
	public ListNode(Object startValue)
	{
		value = startValue;
	}
	public void setValue(Object newValue)
	{
		value = newValue;
	}
	public void setNext(ListNode newNext)
	{
		next = newNext;
	}
	public Object getValue()
	{
		return value;
	}
	public ListNode getNext()
	{
		return next;
	}
	public String toString()
	{
		if(next == null)
			return value.toString();
		return value.toString() + " " + next.toString();
	}
	private Object value;
	private ListNode next;
}
