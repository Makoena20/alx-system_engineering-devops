#!/usr/bin/env ruby

log_line = ARGV[0]

regex = /(?:\[from:([\w\+\d]+)\])?\s?(?:\[to:([\w\+\d]+)\])?\s?\[flags:([\d:-]+)\]/

matches = log_line.match(regex)

sender = matches[1] || ''
receiver = matches[2] || ''
flags = matches[3] || ''

puts "#{sender},#{receiver},#{flags}"

