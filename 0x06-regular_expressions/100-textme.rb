#!/usr/bin/env ruby

# Regex pattern for extracting sender, receiver, and flags
pattern = /\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/

# Read each line from stdin
ARGF.each_line do |line|
  # Match the pattern against the line
  match = line.match(pattern)
  if match
    sender = match[:sender]
    receiver = match[:receiver]
    flags = match[:flags]
    puts "#{sender},#{receiver},#{flags}"
  end
end

