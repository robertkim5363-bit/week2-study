"""
[Queue - Printer Waiting Line]

Problem Description:
- Use a Queue to process printer jobs in order.
- Utilize the FIFO (First In First Out) data structure.

Input:
- jobs: A list of print jobs (e.g., ["DocumentA", "DocumentB", "DocumentC"])

Output:
- The order in which the jobs are processed.

Example:
Input: ["DocumentA", "DocumentB", "DocumentC"]
Output:
Processing: DocumentA
Processing: DocumentB
Processing: DocumentC

Hint:
- In Python, a queue can be implemented using a list.
- append(): Add to the back (enqueue).
- pop(0): Remove from the front (dequeue).
"""

from collections import deque

def process_print_queue(jobs):
    """
    Process printer jobs in order.
    
    Args:
        jobs: List of jobs to print
    
    Returns:
        List of processed jobs
    """
    # 1. Create a queue using deque
    queue = deque(jobs)
    
    processed = []
    
    # 2. Repeat as long as the queue is not empty
    # In Python, 'while queue:' automatically stops when the queue is empty.
    while queue:
        
        # 3. Take out the job at the very front of the queue (Dequeue)
        current_job = queue.popleft()
        
        # 4. Process the job (Print to the screen)
        print(f"Processing: {current_job}")
        
        # 5. Add the finished job to the 'processed' list
        processed.append(current_job)
        
    return processed

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    jobs1 = ["DocumentA", "DocumentB", "DocumentC"]
    print("=== Processing Print Jobs ===")
    result1 = process_print_queue(jobs1)
    print(f"Finished processing: {result1}\n")
    
    # Test Case 2
    jobs2 = ["Email", "Report", "Photo", "Contract"]
    print("=== Processing Print Jobs ===")
    result2 = process_print_queue(jobs2)
    print(f"Finished processing: {result2}")
