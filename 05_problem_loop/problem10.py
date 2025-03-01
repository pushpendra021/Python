import time

max_retries = 5
wait_time = 1  # Start with 1 second

for attempt in range(1, max_retries + 1):
    print(f"Attempt {attempt}: Waiting for {wait_time} seconds...")
    time.sleep(wait_time)  # Simulate waiting
    wait_time *= 2  # Double the wait time
