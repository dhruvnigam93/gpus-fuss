import numpy as np
import time


def benchmark_numpy():
    """Benchmark NumPy matrix multiplication"""
    size = 5000
    print(f"Testing with matrices of size {size} x {size}")

    # Create random matrices
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    # Warm-up
    _ = A @ B

    # Time the operation
    start = time.time()
    C = A @ B
    end = time.time()

    numpy_time = end - start
    print(f"NumPy (CPU) time: {numpy_time:.3f} seconds")

    return numpy_time


def benchmark_cupy():
    """Benchmark CuPy matrix multiplication"""
    try:
        import cupy as cp

        size = 5000

        # Create random matrices on GPU
        A = cp.random.rand(size, size)
        B = cp.random.rand(size, size)

        # Warm-up
        _ = A @ B
        cp.cuda.Stream.null.synchronize()

        # Time the operation
        start = time.time()
        C = A @ B
        cp.cuda.Stream.null.synchronize()
        end = time.time()

        cupy_time = end - start
        print(f"CuPy (GPU) time: {cupy_time:.3f} seconds")

        return cupy_time
    except ImportError:
        print("CuPy not installed - skipping GPU benchmark")
        return None
    except Exception as e:
        print(f"GPU not available: {e}")
        return None


if __name__ == "__main__":
    print("Starting benchmarks...\n")

    numpy_time = benchmark_numpy()
    print()

    cupy_time = benchmark_cupy()
    print()

    if cupy_time:
        speedup = numpy_time / cupy_time
        print(f"Speedup: {speedup:.1f}x")
        print(f"\nResults:")
        print(f"NumPy: {numpy_time:.3f}s")
        print(f"CuPy: {cupy_time:.3f}s")
        print(f"Speedup: {speedup:.1f}x")
    else:
        print(f"Results:")
        print(f"NumPy: {numpy_time:.3f}s")
        print(f"CuPy: Not available (no GPU detected)")
