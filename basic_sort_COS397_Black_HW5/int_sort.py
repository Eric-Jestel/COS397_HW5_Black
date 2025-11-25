# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================


"""
This module sorts lists of integers...
"""
int_list = [4, 5, 6, 7, 8, 10, 25, 3, 16, 200, 153]
testlist = [5, 6, "apple", 5]


def bubble(int_list):
    """
    bubble docstring
    """
    new_list = int_list
    n = len(new_list)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if new_list[j] > new_list[j + 1]:
                a = new_list[j]
                b = new_list[j + 1]
                new_list[j] = b
                new_list[j + 1] = a
                swapped = True
        if not swapped:
            break

    print("bubble sort")
    return new_list  # returning a sorted version of int_list, called new_list


def quick(int_list):
    """
    Args:
        param1: A list of any size containing integers

    Returns:
        Returns a sorted list of integers in ascending order

    KeyError: 
        Raises an exception TypeError if any fields in list are not type int
    """
    try:
        # For loop that checks the type of entire list
        for i in range(len(int_list)): 
            if not isinstance(int_list[i], int):
                # Raise TypeError exception if any fields ar not type int 
                raise TypeError
        
        # Checks if the list is of length <= 1
        if len(int_list) <= 1:
            # Return list if true (No sort needed)
            return int_list
        
        # Choose a pivot in the middle of the list 
        pivot = int_list[len(int_list) // 2]

        # List that contains numbers left(less than) of the pivot
        left = [x for x in int_list if x < pivot]
        #List that contains numbers equal to pivot
        middle = [x for x in int_list if x == pivot]
        #List that contains numbers right(greater than) of the pivot
        right = [x for x in int_list if x > pivot]

        # Recursively call quick for the left and right lists
        # Join left + middle + right and return sorted list
        return quick(left) + middle + quick(right)
    except TypeError:
        # Print error message if TypeError is caught
        print("All fields in list must be type int")


def insertion(int_list):
    """
    insertion docstring
    """
    # making a shallow copy of the list to simplify
    return_List = int_list
    # iterates through each element in the list with i starting at 1
    for i in range(1, len(return_List)):
        # allows us to look 1 behind [i]
        j = i - 1
        # saves the number of return_List[i]
        compare = return_List[i]
        # makes sure j is at least 0 and compare < return_List[j]
        while j >= 0 and compare < return_List[j]:
            # bumps [j] forward 1
            return_List[j + 1] = return_List[j]
            # increments [j]
            j -= 1
        # puts the saved number in the last moved spot
        return_List[j + 1] = compare

    print("insertion sort")
    return return_List