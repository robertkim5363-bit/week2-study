"""
[Priority Queue - Emergency Room Patient Management]

Problem Description:
- Process patients according to their priority using a Priority Queue.
- The smaller the number, the higher the priority (1 > 2 > 3).

Input:
- patients: List of tuples (name, priority)

Output:
- The order in which patients are processed.
"""

import heapq

def process_emergency_room(patients):
    """
    Process patients based on their priority.
    
    Args:
        patients: List of (name, priority)
    
    Returns:
        Processed patient order
    """
    # 1. Create an empty heap (which is just a normal list in Python)
    heap = []
    
    # 2. Add all patients to the heap
    for name, priority in patients:
        # TRICKY PART: Python heaps sort by the FIRST item in a tuple.
        # We must push (priority, name) instead of (name, priority)!
        heapq.heappush(heap, (priority, name))
        
    processed = []
    
    # 3. Repeat as long as the heap is not empty
    while heap:
        # Take out the patient with the highest priority (the smallest number)
        current_priority, current_name = heapq.heappop(heap)
        
        # Print the processing message
        print(f"처리: {current_name} (우선순위: {current_priority})")
        
        # Add the patient's name to the processed list
        processed.append(current_name)
        
    return processed

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    patients1 = [
        ("김철수", 3),
        ("이영희", 1),
        ("박민수", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result1 = process_emergency_room(patients1)
    print(f"처리 순서: {result1}")
    print()
    
    # Test Case 2
    patients2 = [
        ("환자A", 5),
        ("환자B", 1),
        ("환자C", 3),
        ("환자D", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result2 = process_emergency_room(patients2)
    print(f"처리 순서: {result2}")
