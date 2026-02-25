import time
import sys
import os

# Ensure backend is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.llm_service import analyze_content

def benchmark():
    content_type = "text"
    content = "This is a test content that should be cached for performance improvements."

    print(f"Benchmarking analyze_content with content length: {len(content)}")

    try:
        # First call (should be slow without cache)
        start_time = time.time()
        result1 = analyze_content(content_type, content)
        end_time = time.time()
        duration1 = end_time - start_time
        print(f"First call took: {duration1:.6f} seconds")

        # Second call with same arguments (should be fast with cache)
        start_time = time.time()
        result2 = analyze_content(content_type, content)
        end_time = time.time()
        duration2 = end_time - start_time
        print(f"Second call took: {duration2:.6f} seconds")

        if duration1 > 0:
            improvement = (duration1 - duration2) / duration1 * 100
            print(f"Improvement: {improvement:.2f}%")

    except Exception as e:
        print(f"Benchmark failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    benchmark()
