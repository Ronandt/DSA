def selection_sort(arr):
    for x in range(len(arr) -1):
        min_index = x
        for y in range(1 + x, len(arr)):
            if(arr[y] < arr[min_index]):
                min_index = y 
        arr[x], arr[min_index] = arr[min_index], arr[x]
    return arr
    '''[2,1,3]'''
        
print(selection_sort([2,1,3,4,65,3]))



def insertion_sort(arr):
    for x in range(1, len(arr)):
        current_indx_to_swap = x
        for y in range(x-1, -1, -1):
            if(arr[y] > arr[current_indx_to_swap]):
                arr[y], arr[current_indx_to_swap] = arr[current_indx_to_swap], arr[y]
                current_indx_to_swap-=1   
            else:
                break
            

        
        
    return arr
        
print(insertion_sort([1,3,2]))
    


def merge_sort(arr):
    #base case
    if(len(arr) == 1):
        return arr
    pivot = len(arr)//2
    first_half = merge_sort(arr[:pivot])
    second_half = merge_sort(arr[pivot:])
    return sort_merge_sort(first_half, second_half)

def sort_merge_sort(arr1,arr2):
    merged_list = []
    while len(arr1) != 0 and len(arr2) !=0:
        if(arr1[0] < arr2[0]):
            merged_list.append(arr1.pop(0))
        else:
            merged_list.append(arr2.pop(0))
    if(len(arr1) > 0):
        merged_list.extend(arr1)
    if(len(arr2) > 0):
        merged_list.extend(arr2)
    return merged_list
print(merge_sort([4,2,5,1,3]))


def pythonic_quick_sort(arr):
    #assume pivot is center
    if(len(arr) <=1):
        return arr
    pivot = len(arr)//2
    first_half = [x for x in arr if arr[pivot] > x]
    second_half = [x for x in arr if arr[pivot] < x]
    return pythonic_quick_sort(first_half) + [arr[pivot]] + pythonic_quick_sort(second_half)

print(pythonic_quick_sort([2,4,1]))


def actual_quick_sort(arr, pivot, start, end):
    if(start >= end):
        return 
    quick_sort_pivot_sorter(arr,pivot, start,end)

    right = actual_quick_sort(arr, pivot, pivot + 1 ,end) #high end
    left = actual_quick_sort(arr, pivot-1, 0, pivot-1 ) #low end 
    

def quick_sort_pivot_sorter(arr, pivot, start, end ):
    pivot_position = start-1
    for x in range(start, end):
        if(arr[x] <= pivot):
            pivot_position +=1
            arr[pivot_position], arr[x] = arr[x], arr[pivot_position]
    arr[pivot_position + 1], arr[end] = arr[end], arr[pivot_position + 1]
arr = [3,4,1,5,0]
print(actual_quick_sort( arr = arr, pivot = len(arr)-1, start = 0, end = len(arr)-1))
print(arr)
                  


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.head = None
    def append(self,value):
        if(self.head == None):
            self.head = Node(value)
        else: #if head exists
            previous_node = self.head
            self.head = Node(value)
            self.head.next = previous_node
    def remove(self):
        return_node = self.head
        self.head = self.head.next
        return return_node
    def search(self,value):
        current_pointer = self.head
        while current_pointer != None:
            if(current_pointer == value):
                return True
            current_pointer = self.head.next
        return False
    def peak(self):
        return self.head
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        added_node = Node(value)
        if(self.head == None):
            self.head = added_node
        prev_tail = self.tail
        self.tail = added_node
        prev_tail.next = added_node
    def remove(self):
        if(self.head.next == None):
            self.tail = None
            return None
        first_node = self.head.next
        self.head = first_node
        return "removed"
    
def BinarySearch(arr, value_to_be_found):
    low_pointer = 0
    high_pointer = len(arr) -1

    while low_pointer <= high_pointer:
        target =  (high_pointer+low_pointer)//2
        if(value_to_be_found > arr[target]):
            low_pointer = target + 1
        elif(value_to_be_found < arr[target]):
            high_pointer = target -1
        elif(arr[target]==value_to_be_found):
            return True
    return False


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data: Any) -> None:
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.insert_node(self.root, data)

    def insert_node(self, node: TreeNode | None, data: Any) -> None:
        if data < node.data:
            if not node.left:
                node.left = TreeNode(data)
            else:
                self.insert_node(node.left, data)
        else:
            if not node.right:
                node.right = TreeNode(data)
            else:
                self.insert_node(node.right, data)



        


    

        

