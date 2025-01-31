/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        // Dummy node to simplify result list creation
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0;

        // Iterate through both lists until both are fully processed
        while (l1 != null || l2 != null || carry != 0) {
            int sum = carry; // Initialize sum with carry from previous iteration

            if (l1 != null) {
                sum += l1.val; // Add value from first list
                l1 = l1.next; // Move to next node
            }

            if (l2 != null) {
                sum += l2.val; // Add value from second list
                l2 = l2.next; // Move to next node
            }

            carry = sum / 10; // Calculate carry for next addition
            current.next = new ListNode(sum % 10); // Store last digit of sum in new node
            current = current.next; // Move to newly created node
        }

        return dummyHead.next; // Return head of the resulting sum list
    }
}

