#!/usr/bin/env ruby

# Regular expression to match a 10-digit phone number
regex = /^[0-9]{10}$/

# Get the input argument
phone_number = ARGV[0]

# Check if the input matches the regular expression
if phone_number.match?(regex)
  puts phone_number
end

