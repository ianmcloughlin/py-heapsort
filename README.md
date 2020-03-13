# Heap sort in Python
This is an implementation of heap sort in Python, used for teaching purposes.
It's crude and I haven't tested it.
If you find errors please email them to [ian.mcloughlin@gmit.ie](mailto:ian.mcloughlin@gmit.ie).
What I recommend you do with the code is:

1. Run the algorithm with some example lists and verify the results.
2. Add tests that run when the file is run as a script.
3. Adapt the `heapsort` and `heapify` functions to keep track of the number of comparisons made in sorting a given list.
4. Write a function that generates all permutations of a list.
5. Create a list with ten elements, generate all its permutations, and run heap sort of each permutation while keeping track of the number of comparisons made.
6. Consider whether your results confirm that heap sort in O(nlogn).

#### Hints

- To create a list with 10 elements you can use `list(range(10))`.
- To shuffle a list, you can use the `shuffle` function in the `random` module in the standard library. It shuffles in-place.
- To generate all permutations of a list you can use `permutations` in the `itertools` module. That's an interesting module - I'd recommend having a look.
- Don't be afraid to ask for advice, particularly on Stack Overflow.
