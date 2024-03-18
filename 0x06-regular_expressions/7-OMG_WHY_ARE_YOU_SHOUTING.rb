#!/usr/bin/env ruby

# Extracts and concatenates capital letters from the input string
puts ARGV[0].scan(/[A-Z]/).join

