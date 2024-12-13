# main.py
from allocation import best_fit

def main():
    """
    Demonstrates the Best Fit algorithm with an example.
    """
    # Initial memory block sizes (in KB)
    block_sizes = [200, 300, 400, 100, 150]
    # Sizes of processes to be allocated (in KB)
    process_sizes = [120, 250, 50]

    # Display initial state of memory blocks
    print("Initial Memory Blocks (in KB):")
    for i, size in enumerate(block_sizes):
        print(f"Block {i + 1}: {size} KB")
    print()

    # Perform memory allocation
    allocation = best_fit(block_sizes, process_sizes)

    # Display results
    print("Process No.  Process Size  Block No.")
    for i, process_size in enumerate(process_sizes):
        if allocation[i] != -1:
            print(f"    {i + 1}           {process_size}         {allocation[i] + 1}")
        else:
            print(f"    {i + 1}           {process_size}         Not Allocated")

    # Display final state of memory blocks
    print("\nFinal Memory Blocks (in KB):")
    for i, size in enumerate(block_sizes):
        print(f"Block {i + 1}: {size} KB")

# Execute the main function
if __name__ == "__main__":
    main()
