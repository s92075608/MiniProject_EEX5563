# test.py
import unittest
from allocation import best_fit

class TestBestFitMemoryAllocation(unittest.TestCase):
    def test_best_fit(self):
        block_sizes = [200, 300, 400, 100, 150]
        process_sizes = [120, 250, 50]
        
        expected_allocation = [0, 1, 4]
        allocation = best_fit(block_sizes, process_sizes)
        
        self.assertEqual(allocation, expected_allocation)

    def test_no_allocation(self):
        block_sizes = [100, 150, 200]
        process_sizes = [250, 300, 350]
        
        expected_allocation = [-1, -1, -1]  # No process can be allocated
        allocation = best_fit(block_sizes, process_sizes)
        
        self.assertEqual(allocation, expected_allocation)

    def test_partial_allocation(self):
        block_sizes = [200, 300, 400, 100, 150]
        process_sizes = [120, 250, 50, 300, 150]
        
        expected_allocation = [0, 1, 4, 3, 2]
        allocation = best_fit(block_sizes, process_sizes)
        
        self.assertEqual(allocation, expected_allocation)

if __name__ == "__main__":
    unittest.main()
