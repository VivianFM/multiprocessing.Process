from multiprocessing import Process
import time

def compute_task(name):
    print(f"{name}: Task started.")
    time.sleep(2)  # Simulates a CPU-bound workload
    print(f"{name}: Task completed.")

if __name__ == '__main__':
    # Initialize processes
    process_1 = Process(target=compute_task, args=("Process-1",))
    process_2 = Process(target=compute_task, args=("Process-2",))

    # Start processes
    process_1.start()
    process_2.start()

    # Wait for completion
    process_1.join()
    process_2.join()

    print("Main process: All subprocesses completed.")
