#!/usr/bin/env ruby

# Regular expression to match 'hbtn'
regex = /hbt{2,5}n/

# Accepting command line argument
puts ARGV[0].scan(regex).join

