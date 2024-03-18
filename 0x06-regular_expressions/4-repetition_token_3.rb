#!/usr/bin/env ruby

# Regular expression that matches h followed by any single character,
# and then t followed by 1 or more instances of 't'
regex = /h.t+t+/

# The argument passed to the script
arg = ARGV[0]

# Check if the argument matches the regular expression
if arg.match?(regex)
  puts arg
end

