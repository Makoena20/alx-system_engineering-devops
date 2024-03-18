#!/usr/bin/env ruby

# Regular expression to extract sender, receiver, and flags from the log
regex = /\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/

# Loop through each line of input
ARGF.each_line do |line|
  # Match the regular expression against the line
  match = line.match(regex)

  # If there's a match, extract sender, receiver, and flags
  if match
    sender = match[:sender].gsub(/^(\+)?/, '') # remove leading '+' if present
    receiver = match[:receiver].gsub(/^(\+)?/, '') # remove leading '+' if present
    flags = match[:flags]
    puts "#{sender},#{receiver},#{flags}"
  end
end

