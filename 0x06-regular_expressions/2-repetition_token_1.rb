#!/usr/bin/env ruby

# Regular expression to match cases with "hbtn", "htn", or "hbbbbtn"
regex = /hbt{0,1}n/

# Get the argument passed to the script
input = ARGV[0]

# Check if the input matches the regular expression
if input.match?(regex)
  puts input
end

