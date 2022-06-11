import random
from datetime import datetime


def max_heapify(arr, n, i):                             # parameters to take in an array representation of a heap, an array size, and an index to recurse on
    largest = i                                         # set the index of the "largest" node to the index passed into the array
    l = 2 * i + 1                                       # find the index of the left child of node at index i
    r = 2 * i + 2                                       # find the index of the right child of node at index i

    if l < n and arr[largest] < arr[l]:
        largest = l                                     # if the current "largest" node is smaller than the left child, set
                                                        # the index of the "largest" node to the left child
    if r < n and arr[largest] < arr[r]:
        largest = r                                     # if the current "largest" node is smaller than the right child, set
                                                        # the index of the "largest" node to the rightf child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]     # if the index of the "largest" node isn't equal to the index passed to the array, swap the
                                                        # value at index i with the value at index "largest"
        max_heapify(arr, n, largest)                    # recursive call


def build_max_heap(arr):  				# Building the heap from an input array
    size = len(arr)  					# setting the size of the heap
    for i in range(size // 2, -1, -1):  # iterating through parent elements in the heap in a bottom up fashion
        max_heapify(arr, size, i)  		# ensuring that the children are less than or equal to the parent


def heapsort(arr):
    size = len(arr) 
    build_max_heap(arr)  # create max heap; MAX value at index 0 

    for i in range(size - 1, 0, -1): #size - 1 down to 1
        arr[i], arr[0] = arr[0], arr[i]  #swap arr[i] with top node
        max_heapify(arr, i, 0)  # max heapify 


def insert(arr, elem):  # parameters include array (must meet heap property) and input value
    arr.append(elem)  # append input value to array end
    inputPos = len(arr) - 1  # start position of input value
    while arr[inputPos] > arr[(inputPos-1) // 2] and inputPos != 0:  # check if input's value is greater than parent's
        arr[inputPos], arr[(inputPos-1) // 2] = arr[(inputPos-1) // 2], arr[inputPos]  # swap input and parent's values
        inputPos = (inputPos-1) // 2  # redefine position of input value as the original position of its parent


def extract_max(arr):
    arr[0], arr[-1] = arr[-1], arr[0]  	# swap largest node with last
    largest = arr.pop()  				# remove the largest that was put in the last
    max_heapify(arr, len(arr), 0)  		# run heapify to rebuild heap
    return largest						# return the largest value

def test_build_functions(test_len):
	A=[0]*test_len
	a=0
	b=0
	repeat=20
	for j in range(repeat):
		for i in range(test_len):
			A[i]=random.choice(range(test_len))
		start_time = datetime.now()
		#max_heapify(A,test_len,0)
		#heapsort(A)
		build_max_heap(A)
		final_time = datetime.now()
		a+=(final_time-start_time).total_seconds()*1000000
		b+=test_simple_functions(A,test_len)
	a=str(a/repeat)
	while len(a) < 10:
		a += '0'
	return (a + "\t\t" + str(b/20))
	
def test_simple_functions(A,test_len):
	insert_test = test_len/2
	start_time = datetime.now()
	a=extract_max(A)
	#insert(A,insert_test)
	final_time = datetime.now()
	A.append(0)
	return (final_time-start_time).total_seconds()*1000000

if __name__ == '__main__':
	print("Length\t\tTime of build(μs)\tTime of simple(μs)")
	curr_time = datetime.now()
	a=1000
	print(str(a) + "\t\t" + test_build_functions(a))
	a=10000
	print(str(a) + "\t\t" + test_build_functions(a))
	a=100000
	print(str(a) + "\t\t" + test_build_functions(a))
	a=500000
	print(str(a) + "\t\t" + test_build_functions(a))
	a=1000000
	print(str(a) + "\t\t" + test_build_functions(a))
	
	'''A = [1,2,3,4,5,6,7,8,9,10]

	print(A)
	build_max_heap(A)
	print("Build Max Heap Output: " + str(A) + "\n")
	
	insert(A, 11)
	print("Insert Output: " + str(A) + '\n')
	
	extract_max(A)
	print("Extract Max Output: " + str(A) + '\n')'''
	