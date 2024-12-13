# allocation.py

def best_fit(block_sizes, process_sizes):
    """
    Allocates memory to processes using the Best Fit algorithm.

    Parameters:
        block_sizes (list): List of available memory block sizes.
        process_sizes (list): List of sizes of processes to be allocated.

    Returns:
        allocation (list): List of block indices allocated to each process.
    """
    # Number of blocks and processes
    num_blocks = len(block_sizes)
    num_processes = len(process_sizes)

    # Stores block index allocated to each process (-1 indicates not allocated)
    allocation = [-1] * num_processes

    # Iterate over each process to allocate memory
    for i in range(num_processes):
        best_idx = -1  # Variable to store the index of the best-fitting block

        for j in range(num_blocks):
            # Check if the block can accommodate the process
            if block_sizes[j] >= process_sizes[i]:
                # Update best_idx if the current block is a better fit
                if best_idx == -1 or block_sizes[j] < block_sizes[best_idx]:
                    best_idx = j

        # If a suitable block is found, allocate it
        if best_idx != -1:
            allocation[i] = best_idx
            # Reduce the size of the allocated block
            block_sizes[best_idx] -= process_sizes[i]

    return allocation
