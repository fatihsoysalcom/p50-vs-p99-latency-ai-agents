import random
import time
import statistics

def simulate_agent_response(is_outlier=False):
    """Simulates an AI agent's response time.

    Args:
        is_outlier (bool): If True, simulates a very slow response.

    Returns:
        float: The simulated response time in seconds.
    """
    if is_outlier:
        # Simulate a rare, very slow response (e.g., complex query, network issue)
        return random.uniform(5, 15)
    else:
        # Simulate typical, fast responses
        return random.uniform(0.05, 0.5)

def calculate_percentiles(latencies):
    """Calculates P50 (median) and P99 latencies.

    Args:
        latencies (list): A list of response times.

    Returns:
        tuple: A tuple containing P50 and P99 latencies.
    """
    if not latencies:
        return None, None

    latencies.sort()
    n = len(latencies)

    # Calculate P50 (Median)
    p50_index = (n - 1) // 2
    p50 = latencies[p50_index] if n % 2 != 0 else (latencies[p50_index] + latencies[p50_index + 1]) / 2

    # Calculate P99
    p99_index = int(0.99 * n)
    # Ensure index is within bounds, especially for small lists
    p99_index = min(p99_index, n - 1)
    p99 = latencies[p99_index]

    return p50, p99

# --- Simulation Scenarios ---

# Scenario 1: Mostly fast responses, no outliers
print("--- Scenario 1: No Outliers ---")
latencies_no_outliers = [simulate_agent_response() for _ in range(100)]
p50_no, p99_no = calculate_percentiles(latencies_no_outliers)
print(f"P50 (Median): {p50:.3f}s")
print(f"P99: {p99_no:.3f}s")
print("\n")

# Scenario 2: Mostly fast responses, with a few outliers
print("--- Scenario 2: With Outliers ---")
latencies_with_outliers = [simulate_agent_response() for _ in range(95)] + [simulate_agent_response(is_outlier=True) for _ in range(5)]
random.shuffle(latencies_with_outliers) # Mix them up

p50_with, p99_with = calculate_percentiles(latencies_with_outliers)
print(f"P50 (Median): {p50_with:.3f}s")
print(f"P99: {p99_with:.3f}s")
print("\n")

# Scenario 3: A single, extreme outlier
print("--- Scenario 3: Single Extreme Outlier ---")
latencies_extreme_outlier = [simulate_agent_response() for _ in range(99)] + [simulate_agent_response(is_outlier=True) for _ in range(1)]
random.shuffle(latencies_extreme_outlier)

p50_extreme, p99_extreme = calculate_percentiles(latencies_extreme_outlier)
print(f"P50 (Median): {p50_extreme:.3f}s")
print(f"P99: {p99_extreme:.3f}s")
print("\n")

print("Notice how P50 (median) remains relatively stable, while P99 is heavily influenced by outliers.")
print("For AI agent workloads, P99 is often a more critical metric for user experience.")
