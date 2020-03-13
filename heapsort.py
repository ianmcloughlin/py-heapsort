def heapify(A, i, s=0):
  """Treats the array A[:-s] as a binary tree and pushes A[i] down through the
  levels until the branch starting at A[i] becomes a max heap.
  It is assumed that the branches starting at A[2*i+1:s] and A[2*i+2] are
  already max heaps.
  Changes the array A in place, so there is no return value.
  """
  # Index of last child.
  ilastchild = len(A) - s - 1
  # Index of last parent.
  ilastparent = (ilastchild - 1) // 2
  global count
  # Keep looping until the break.
  while True:
    # Assume A[i] is bigger than the children at first.
    ilargest = i
    
    # Index of left child.
    ileft = 2*i + 1
    # Check left child exists.
    if ileft <= ilastchild:
      # Check whether left child is bigger than A[ilargest].
      if A[ileft] > A[ilargest]:
        # If it is, change ilargest.
        ilargest = ileft
    
    # Index of right child.
    iright = 2*i + 2
    # Check right child exists.
    if iright <= ilastchild:
      # Check whether right child is bigger than A[ilargest].
      if A[iright] > A[ilargest]:
        # If it is, change ilargest.
        ilargest = iright
    
    # Find the largest of A[i], A[lchild] and A[rchild], maknig sure the
    # children exist first.

    # Check if we made a swap.
    if ilargest == i:
      # If we didn't, we're done.
      break
    else:
      # Otherwise swap A[i] for A[ilargest] and then set i to ilargest.
      A[i], A[ilargest] = A[ilargest], A[i]
      i = ilargest
  
def heapsort(A):
  """Sort the array A in-place using heap sort.
  """
  
  # First, create a max heap.
  
  # Index of last child.
  ilastchild = len(A) - 1
  # Index of last parent.
  ilastparent = (ilastchild - 1) // 2
  
  # Loop backwards through all parents, converting them into max heaps.
  for i in range(ilastparent, -1, -1):
    # This assumes A[2*i+1] and A[2*i+2] are already max heaps, and then
    # transforms A[i] into a max heap.
    heapify(A, i)
  
  # We loop for each element of the list, swapping the root at A[0] for the
  # element at A[-(s+1)] and then heapify-ing the tree A[:-s].
  for s in range(len(A)):
    # Move root to correct position.
    A[0], A[-(s+1)] = A[-(s+1)], A[0]
    # Heapify the tree.
    heapify(A, 0, s+1)
