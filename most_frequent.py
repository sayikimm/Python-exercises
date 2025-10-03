def find_most_frequent_item(inventory_list):
    frequency_map = {}

    # 2. Iterate and Count
    for item in inventory_list:
        # Check if the item is already a key, and update or insert
        if item in frequency_map:
            frequency_map[item] += 1
        else:
            frequency_map[item] = 1

    # 3. Find the Maximum
    if not frequency_map:
        return None  # Handle empty list case

    max_item = None
    max_count = 0

    for item, count in frequency_map.items():
        if count > max_count:
            max_count = count
            max_item = item

    # 4. Return
    return max_item


# --- Test Cases ---
print(
    f"Test 1: {find_most_frequent_item(['laptop', 'mouse', 'laptop', 'keyboard', 'laptop', 'monitor'])}"
)
print(f"Test 2: {find_most_frequent_item(['A', 'B', 'A', 'C', 'B'])}")
print(f"Test 3: {find_most_frequent_item(['pen', 'pencil', 'ruler'])}")
