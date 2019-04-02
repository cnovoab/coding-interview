SUFFIX = %w(st nd rd th)

MONTHS = {
  'Jan' => '01',
  'Feb' => '02',
  'Mar' => '03',
  'Apr' => '04',
  'May' => '05',
  'Jun' => '06',
  'Jul' => '07',
  'Aug' => '08',
  'Sep' => '09',
  'Oct' => '10',
  'Nov' => '11',
  'Dec' => '12'
}

def reformat_date(dates)
  dates.map do |date|
    date = date.split(' ')
    y, m, d = date[2], MONTHS[date[1]], date[0].to_i.to_s.rjust(2,'0')
    "#{y}-#{m}-#{d}"
  end
end
