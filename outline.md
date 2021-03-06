* Title
* What is concurrency
* What is parallelism
* Concurrency vs. parallelism
  * "Multitasking" is two or more processes running concurrently
* Why do we need to think about concurrency
  * Required for efficient computation
  * Difficult for humans to reason about (we experience the world linearly and
    are pretty bad at parallelism, so reasoning about concurrency is unnatural)
* Hardware not included
  * Transputer
  * I'd love to see a talk on it! (Especially cores, cache lines, and memory
    busses.)
* Not distributed systems
  * Think Go, not Plan9; Node.js, not MongoDB
* Everything was invented in the 60s and 70s
* Threads vs. "Async" was addressed in 79
* Threads notably absent from the history
  * Source of all evil/parallelism
  * What are threads?
    * <worst-diagram-ever.jpg>
* To answer that we must understand 3 concepts
* 1/3 Primitives vs. Patterns vs. Models
* Primitive Evolution
  * Example:
```
 mutex + condition_variable = monitor
    ^             ^              ^
    |             |              |
primitive     primitive    new primitive!
|                     |
+----------+----------+
           |
        pattern
```
* 1/3 continued...
  * Threading is a primitive, not a model
  * Modern examples:
    * Akka's Actor model is exposed via primitives in Erlang, Julia follows suit
    * Go exposes CSP as primitives
    * Dart and Rust expose task isolation and message passing primitives (Actorish)
* 2/3 Concurrency & Scheduling
  * Traditional/OS threads are preemptive; green threads are userland, but not
    always cooperative
  * Modern examples:
    * Rust has configurable scheduling with a M:N library
    * Python and Ruby both support preemption but have cooperative libraries
    * Javascript and Dart only support cooperative scheduling
* 3/3 Methods of Interaction
  * Threads share memory; this is the source of their controversy/complexity
  * Erlang provided low-level primitives for high-level models in the 80s.
    Other languages took nearly 25 years to catch up.
  * Modern examples:
    * Uninteresting: Java, C#, C/C++, Python, Ruby, Go all support preemption and shared memory
    * Javascript shares memory but doesn't have preemption
    * Rust promises safe sharing by tracking ownership
    * Dart doesn't allow shared memory, only message passing
    * Julia has highlevel primitives for messaging passing and copying instead
      of sharing
* Now
  * New languages like Go, Rust, Julia, and Dart all including lots of
    concurrency features.
  * C# has added concurrency features to an already mature language
* Next
  * Generators as coroutines - Python has been trying it for over 10 years with
    near-0 adoption. Node.js appears headed down the same road.
  * STM (Haskell/GHC & Clojure have it, many other languages have experimental
    or library support)
  * Scheduler hinting syscalls in Linux
  * More M:N threading (Go's goroutines, Rust's tasks, Dart's isolates, Haskell/GHC again)
    * Those who can't M:N, N:1 (stackless Python, PyPy, Ruby Fibers, Node.js
      Fibers, Dart tasks)
  * **More models being implemented as primitives** -- You can't stop evolution!
