#!/bin/bash
set -x
echo "Processing initial tests"
python /sre/cli.py --input_filename /sre/images_to_compare.csv --output_filename /sre/results.csv
echo "Checking test results"
# The files cannot be compared in their entirety because they contain the time
# it took to process each file, this time will vary.
# In the next diff, we will use only the first 4 columns for comparison:
# - The row number
# - The filename1
# - The filename2
# - The mean squared error
diff <(cut -d, -f1-4 /sre/expected_results.csv) <(cut -d, -f1-4 /sre/results.csv)
# If the files are different, diff will set exit code to 1, this will allow
# to fail this script and fail the docker build
exit $?
