


def twoSumNaive(num_arr, pair_sum):
    # search first element in the array
    for i in range(len(num_arr) - 1):
        # search other element in the array
        for j in range(i + 1, len(num_arr)):
            # if these two elemets sum to pair_sum, print the pair
            if num_arr[i] + num_arr[j] == pair_sum:
                print("Pair with sum", pair_sum, "is: (", num_arr[i], ",", num_arr[j], ")")


# Driver Code
num_arr = [3, 5, 2, -4, 8, 11]
pair_sum = 7

# Function call inside print
twoSumNaive(num_arr, pair_sum)
# Time Complexity: O(n^2) since we are traversing through a nested loop


# a hashtable has O(1) lookup time which would be more optimal solution

def twoSumHashing(num_arr, pair_sum):
    # create an empty hashtable
    hashTable = {}

    # for each element in the array
    for i in range(len(num_arr)):
        # calculate the complement by subtracting the current list elemnt from the given number
        complement = pair_sum - num_arr[i]
        # Look up the complement in the hashtable if it exists
        if complement in hashTable:
            # if it exists, a pair that sums up the given number has been found
            print("Pair with sum", pair_sum, "is: (", num_arr[i], ",", complement, ")")
        # insert the current element of the array in to the hashtable
        hashTable[num_arr[i]] = num_arr[i]


# Driver Code
num_arr = [4, 5, 1, 8]
pair_sum = 9

# Calling function
twoSumHashing(num_arr, pair_sum)


# Time Complexithy: O(n)
    # As the whole array is needed to be traversed only once.

    # Space: O(n)
        # As a hash map has been used to store array elemetns