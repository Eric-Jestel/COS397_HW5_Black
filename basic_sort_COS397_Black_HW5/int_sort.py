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


def bubble(int_list): # Bubble sort added by Conall Gouveia
    """
    bubble docstring
    """
    new_list = int_list
    n = len(new_list)
    
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if new_list[j] > new_list[j+1]:
                a = new_list[j]
                b = new_list[j+1]
                new_list[j] = b
                new_list[j+1] = a
                swapped = True
        if not swapped:
            break
            
    print("bubble sort")
    return new_list # returning a sorted version of int_list, called new_list


def quick(int_list):
    """
    qsort docstring
    """
    print("quick sort")
    return sorted(int_list)


def insertion(int_list):
    """
    insertion docstring
    """
    print("insertion sort")
    return sorted(int_list)
