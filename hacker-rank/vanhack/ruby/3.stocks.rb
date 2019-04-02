#!/bin/ruby

require 'net/http'
require 'json'
require 'date'

def openAndClosePrices(firstDate, lastDate, weekDay)
  # validate input
  firstDate = Date.parse(firstDate)
  lastDate = Date.parse(lastDate)
  fail 'Invalid date range, lastDate must be greater than or equal than firstDate' if firstDate > lastDate

  # make requests per month-year
  uri = URI('https://jsonmock.hackerrank.com/api/stocks/search')
  months = (firstDate..lastDate).map {|x| x.strftime("%B-%Y")}.uniq
  months.each do |month|
    page = 1
    # loop through results pages
    loop do
      uri.query = URI.encode_www_form(page: page, date: month)
      res = Net::HTTP.get_response(uri)
      body = JSON.parse(res.body)

      body['data'].each do |data|
        date = Date.parse(data['date'])
        next if date.strftime('%A').downcase != weekDay.downcase || firstDate > date || lastDate < date
        # puts "Date: #{data['date']} - Open: #{data['open']} - Close: #{data['close']} - Day: #{day_name}"
        puts "#{data['date']} #{data['open']} #{data['close']}"
      end

      page += 1
      break if (page > body.fetch('total_pages', 1))
    end
  end
end

openAndClosePrices(*ARGV)
