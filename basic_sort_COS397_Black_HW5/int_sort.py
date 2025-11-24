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


def bubble(int_list):
    """
    This is a bbble sort algorithm

    Bubble sort:
        Parameter: int_list
    
    Returns:
        The function returns a new list called new_list, which is an ordered form of int_list.
    
    Raises:
        None.
        
    """
    new_list = list(int_list)
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
    qsort docstring
    """
    if len(int_list) <= 1:
        return int_list

    pivot = int_list[len(int_list) // 2]

    left = [x for x in int_list if x < pivot]
    middle = [x for x in int_list if x == pivot]
    right = [x for x in int_list if x > pivot]

    return quick(left) + middle + quick(right)


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
