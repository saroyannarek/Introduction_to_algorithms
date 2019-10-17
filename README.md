# Introduction_to_algorithms

Analysis of insertion sort

The time taken by the INSERTION-SORT procedure depends on the input: sorting a
thousand numbers takes longer than sorting three numbers. Moreover, INSERTIONSORT
can take different amounts of time to sort two input sequences of the same
size depending on how nearly sorted they already are. In general, the time taken
by an algorithm grows with the size of the input, so it is traditional to describe the
running time of a program as a function of the size of its input. To do so, we need
to define the terms “running time” and “size of input” more carefully.
The best notion for input size depends on the problem being studied. For many
problems, such as sorting or computing discrete Fourier transforms, the most natural
measure is the number of items in the input—for example, the array size n
for sorting. For many other problems, such as multiplying two integers, the best
measure of input size is the total number of bits needed to represent the input in
ordinary binary notation. Sometimes, it is more appropriate to describe the size of
the input with two numbers rather than one. For instance, if the input to an algorithm
is a graph, the input size can be described by the numbers of vertices and
edges in the graph. We shall indicate which input size measure is being used with
each problem we study.
The running time of an algorithm on a particular input is the number of primitive
operations or “steps” executed. It is convenient to define the notion of step so
that it is as machine-independent as possible. For the moment, let us adopt the
following view. A constant amount of time is required to execute each line of our
pseudocode. One line may take a different amount of time than another line, but
we shall assume that each execution of the i th line takes time ci, where ci is a
constant. This viewpoint is in keeping with the RAM model, and it also reflects
how the pseudocode would be implemented on most actual computers.5
In the following discussion, our expression for the running time of INSERTIONSORT
will evolve from a messy formula that uses all the statement costs ci to a
much simpler notation that is more concise and more easily manipulated. This
simpler notation will also make it easy to determine whether one algorithm is more
efficient than another.
