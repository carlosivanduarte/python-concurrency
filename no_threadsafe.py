import concurrent.futures

counter = 0

def increment_counter(fake_value):
    global counter
    for _ in range(100):
        counter += 1


if __name__ == "__main__":
    fake_data = [x for x in range(5000)]
    counter = 0
