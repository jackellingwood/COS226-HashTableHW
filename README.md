Note:

I may not have included all the necessary info in each commit message, but all the info needed is present below and in my screenshots. All optimizations are in separate branches.

Optimization 1:

My first idea was to fix up the basic hash function I created by multiplying it by a prime, allowing the function to not be so skewed to the left by short titles. I also added a few more slots than the number of data points added which drastically reduced the time spent probing. This added 1000 wasted slots but improved times by multiple seconds.

Optimization 2:

Then I decided to try using LinkedNodes to handle collisions rather than linear probing. Surprisingly, this didn't affect the time taken too much, and still had wasted slots, and now extra memory lost from the LinkedLists.

Optimization 3:

I have used the djb2 hashing function in previous work and have found it to be very good, but I've never tested how much it avoids collision, so I tested it here in my linkedNode example. This improved title time and reduced collisions by a few thousand. It increased for the quote table likely because of a certain long entry...

Optimization 4:

I thought that some time may also be lost in traversing each linked list, so I gave the Node a .last property to track the last node with an empty .next, however, this did not improve either time by a significant margin. I think this may be because the hashing function is pretty good by this point. This optimization also increased memory overhead (each node now has to track a .last).

Optimization 5:

Since my quote times specifically were bad, I decided to add a special case for the bee movie script entry, as doing math operations for each char was taxing. I just use the length of the function to determine a key. This would also work to improve times for other data sets with very rare but very long outliers. This improved quote times by a factor of 5.

Optimization 5b: (Revision Optimization)

I wanted to try out linear probing to see if it performed well with the optimizations I had above, granted that I'd give it 1000 extra slots. This means that it would probably use less memory considering the overhead of linkedNodes and .last variables, while still making reasonably good time (only doubled) and only ~1000 more collisions. It performs slower than my original optimization, but has less collisions than it, likely due to my implementation of the djb2 hash function.

Conclusion:

I've probably added more memory overhead than is needed by using .last and LinkedNodes, so if I were to make a final version, I'd use linear probing with the rest of my optimizations. I'd give my table more slots than is needed and use a tried and true hash function like djb2, as well as handle absurdly long inputs.