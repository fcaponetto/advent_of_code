def convert(initial_value, conversion_map):
    for dest_start, source_start, length in conversion_map:
        if source_start <= initial_value < source_start + length:
            # Calculate the corresponding destination value
            dest_value = dest_start + (initial_value - source_start)
            return dest_value
    # If no specific conversion is found, return the initial value
    return initial_value

def apply_conversion_maps(initial_values, conversion_maps):
    result = []
    for initial_value in initial_values:
        for conversion_map in conversion_maps:
            initial_value = convert(initial_value, conversion_map)
        result.append(initial_value)
    return result

seeds = [79, 14, 55, 13]

# Define conversion maps in the order specified
conversion_maps = [
    [(50, 98, 2), (52, 50, 48)],  # seed-to-soil map
    [(0, 15, 37), (37, 52, 2), (39, 0, 15)],  # soil-to-fertilizer map
    [(49, 53, 8), (0, 11, 42), (42, 0, 7), (57, 7, 4)],  # fertilizer-to-water map
    [(88, 18, 7), (18, 25, 70)],  # water-to-light map
    [(45, 77, 23), (81, 45, 19), (68, 64, 13)],  # light-to-temperature map
    [(0, 69, 1), (1, 0, 69)],  # temperature-to-humidity map
    [(60, 56, 37), (56, 93, 4)]  # humidity-to-location map
]

# Apply conversion maps to seeds
result = apply_conversion_maps(seeds, conversion_maps)

# Display the result
for seed, soil in zip(seeds, result):
    print(f"Seed number {seed} corresponds to location number {soil}.")
