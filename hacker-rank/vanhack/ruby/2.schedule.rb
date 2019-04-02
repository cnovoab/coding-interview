# Sample input
WORK_HOURS = 56
DAY_HOURS = 8
SCHEDULE = '???8???'

def findSchedules(workHours, dayHours, pattern)
  schedule = pattern.split('')
  known = schedule.reject { |s| s == '?' }.map(&:to_i)
  unknown = schedule - known
  pendingHours = workHours - known.sum
  possibleSchedules = []
  (0..dayHours).to_a.repeated_permutation(unknown.size) do |p|
    possibleSchedules << p if p.sum == pendingHours
  end
end
