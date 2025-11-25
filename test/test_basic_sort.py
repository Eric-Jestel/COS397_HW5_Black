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

import pytest
import numpy as np
import psutil

from basic_sort_COS397_Black_HW5.int_sort import bubble, quick, insertion


@pytest.fixture
def int_lists():
    """Generates deterministic lists to sort.

    Returns:
        list[list[int]]: A list of input lists for testing.
    """
    seed = np.random.default_rng(39725)
    return [
        [1, 2, 3],  # Positive control
        [3, 2, 1],  # Simple list
        [1, 1, 1],  # Duplicates
        seed.integers(low=-10, high=200, size=5).tolist(),  # Larger random list
        [],  # Empty set
        [5],  # Single item
        [3, 1, -4, 1, -5],  # Duplicates + negatives
    ]


def is_sorted(int_list):
    """Testing oracle."""
    return all(int_list[i] <= int_list[i + 1] for i in range(len(int_list) - 1))


def test_bubble(int_lists):
    for test_case in int_lists:
        assert is_sorted(bubble(test_case))


def test_bubble_cpu_usage(int_lists):
    """Bubble sort CPU usage test.

    Measures CPU time used by bubble sort on a test list.
    """
    process = psutil.Process()
    test_list = int_lists[3]

    cpu_before = process.cpu_times().user
    bubble(test_list)
    cpu_after = process.cpu_times().user

    cpu_used = cpu_after - cpu_before

    assert cpu_used >= 0


def test_quick(int_lists):
    for test_case in int_lists:
        assert is_sorted(quick(test_case))


def test_insertion(int_lists):
    for test_case in int_lists:
        assert is_sorted(insertion(test_case))
