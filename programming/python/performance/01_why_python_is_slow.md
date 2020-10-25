# Why python is slow(ish)

Python has several drawbacks that make it perform much slower than other languages like C. These will be listed in a sec.

Python trades native (raw) performance for speed of development and ease of use. Because it abstracts away nearly every aspect of the underlying hardware, it is easy to use as a developer and therefore provides fast development speeds. This come with a cost: Performance. But through good programming practice, good algorithms and the use of fitting modules (*numpy*, etc) Python can combine both: **performance** and **speed of development**.

## Reasons that make Python slow

* **GIL**: Python is locked to run run one execution at a time - even on multi-threaded platforms
* **Vectorization**: Python does not support vectorization and therefore cant use the full potential of CPU's and **GPUs**
* **Garbage Collection**: Memory is fragmented and not layed out optimally. This hurts especially the L1/L2 cache.
* **No Compiler**: Because Python is interpreted, it cant rely on all those fancy optimizations that a compiler does for you.
* **Dynamic typing**: Makes it nearly impossible to optimize algorithms and memory.
