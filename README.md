# Multiprocessing with `multiprocessing.Process`

The `multiprocessing` module in Python offers a high-level interface for creating and managing separate processes through a process-based parallelism API similar to the `threading` module. 

The `Process` class allows for creating and managing separate memory spaces that run concurrently, enabling true **parallelism** in Python programs. Each `Process` instance runs in its **own Python interpreter and memory space**, providing **better performance** for computationally intensive operations than threads, which share the same memory space and are constrained by the GIL.

It's particularly important in CPU-bound tasks where the Global Interpreter Lock (GIL)[^1] becomes a limiting factor. 

> [^1]: The Global Interpreter Lock (GIL) is a mutex (mutual exclusion lock) used in CPython, the reference implementation of Python. Its purpose is to ensure that only one thread executes Python bytecode at a time, even on multi-core systems.

## Key Advantages

- Enables true parallelism by leveraging multiple CPU cores.
- Avoids GIL restrictions inherent in Python threads.
- Provides process isolation, which can improve robustness in certain applications.
- Flexible process lifecycle management (start, join, terminate).

## When to Use

Use `multiprocessing.Process` when:

- Overcoming limitations of the Global Interpreter Lock (GIL), which restricts true parallelism in multi-threaded code.
- Achieving process-level isolation for improved security, fault tolerance, or modularity.
- Scaling execution across multiple CPU cores to meet performance requirements.
- Leveraging multiple processes without necessarily requiring significant memory upgrades, depending on the memory footprint of each task.

> For I/O-bound tasks (e.g., reading from disk, accessing a database, or making network requests), alternatives like `threading` or `asyncio` may provide better performance and lower overhead.

## Practical example

See [`example_multiprocessing.Process.py`](./example_multiprocessing.Process.py) for a complete example.

### `Process` Parameters

In the code snippet `Process(target=function_name, args=(arg1, arg2, ...))`, the `Process` class from the `multiprocessing` module is used to **create** a new process to run the specified function in parallel. Let’s break it down:

1. **`target=function_name`**  
   This is the function that the new process will execute. The `target` argument specifies the function to be called in the new process.

2. **`args=(...)`**  
   This tuple contains the arguments that will be passed to the target function when the process is started.

   The `args` tuple is used to provide the required input values for the target function when the process begins execution.

### `Process` Methods
#### `.start()`

- **Purpose**: It **initiates the process**, causing the `target` function (e.g., `function_name`) to begin executing in a new process.
- **How it works**: When `.start()` is called, a new process is created, and the function specified in `target` starts running in that process. This operation is asynchronous, meaning the main program continues executing without waiting for the new process to complete.
> **Note:** Calling `.start()` **is required** to actually launch the process! If you create a Process object and never call `.start()`, the process is never executed—it's just an object sitting in memory.

#### `.join()` 

- **Purpose**: It causes the **main program to wait** for the process to finish before continuing. It ensures that the program doesn't exit until all processes have completed their work.
- **How it works**: When `.join()` is called, the main program pauses at that point and waits for the associated process to finish. Once the process terminates, the program resumes execution.
> **Note:** `.join()` is **not mandatory**, but it's crucial if you need to ensure the child processes finish before the main process proceeds (e.g., when collecting results, cleaning up resources, or timing execution).

## Summary
The `.start()` method launches a subprocess while the main process continues executing; only when `.join()` is reached does the main process pause to wait for each subprocess to finish — note that subprocesses (e.g., `process_1.start()`; `process_2.start()`) run independently and do not wait for each other, only the main process is blocked by `.join()`.
