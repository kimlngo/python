import time

def benchmark_execution(fn_in_scope):

    def wrap_fn():
        start = time.time()
        fn_in_scope()
        end = time.time()

        print(f"Execution takes: {end - start}")
    
    return wrap_fn

