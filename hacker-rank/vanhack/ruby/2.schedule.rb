def findSchedules(workHours, dayHours, pattern)
  schedule = pattern.split('')
  known = schedule.reject { |s| s == '?' }
  unknown = schedule - known
  pendingHours = workHours.to_i - known.map(&:to_i).sum
  permutations = (0..dayHours.to_i).to_a.repeated_permutation(unknown.size)
  puts 'permutations 1 done'
  results = []
  permutations.each do |p|
    # select { |p| p.sum == pendingHours }
    puts "Li" if p.sum == pendingHours
    results << schedule.join('').gsub('?') { p.shift } if p.sum == pendingHours
  end
  puts 'permutations 2 done'
  # li = li.map { |p| schedule.join('').gsub('?') { p.shift } }
  results
end

result = findSchedules(*ARGV)
puts result

