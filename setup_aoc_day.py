#!/usr/bin/python3
import argparse
import os
import subprocess

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.

SESSION = ''

useragent = 'https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py by jonathanpaulson@gmail.com'

# Argument parser for specifying the year and day
parser = argparse.ArgumentParser(description='Download Advent of Code input and prepare challenge structure.')
parser.add_argument('--year', type=int, default=True, help='Year of the Advent of Code challenge')
parser.add_argument('--day', type=int, required=True, help='Day of the challenge (1-25)')
args = parser.parse_args()

# Format the year and day
year_str = str(args.year)
day_str = f"d{args.day:02d}"

# Create the directory structure including the year
base_dir = os.path.join(year_str, day_str, 'data')
os.makedirs(base_dir, exist_ok=True)

# Download the input file
cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A \'{useragent}\''
try:
    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    output = output.decode('utf-8')
except subprocess.CalledProcessError as e:
    print(f"Error fetching input: {e.output.decode('utf-8')}")
    exit(1)

# Save the input to the `input.txt` file
input_file_path = os.path.join(base_dir, 'input.txt')
with open(input_file_path, 'w') as f:
    f.write(output)

print(f"Input saved to {input_file_path}")

# Create empty Python files for the challenges
challenge_1_path = os.path.join(year_str, day_str, '01.py')
challenge_2_path = os.path.join(year_str, day_str, '02.py')

for file_path in [challenge_1_path, challenge_2_path]:
    if not os.path.exists(file_path):  # Avoid overwriting existing files
        with open(file_path, 'w') as f:
            pass
        print(f"Created file: {file_path}")

print(f"Structure for year {args.year}, day {args.day} created successfully.")
