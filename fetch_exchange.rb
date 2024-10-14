# frozen_string_literal: true

require 'uri'
require 'net/http'
require 'json'

def fetch_exchange_rate(base, symbol)
  url = URI('https://data.fixer.io/api/latest')
  params = {
    access_key: '',
    base: base,
    symbols: symbol
  }
  url.query = URI.encode_www_form(params)
  response = Net::HTTP.get_response(url)

  raise "HTTP request failed: #{response.code}" unless response.is_a?(Net::HTTPSuccess)

  parsed_json = JSON.parse(response.body)

  raise "API request failed: #{parsed_json['error']['info']}" unless parsed_json['success']

  puts parsed_json['rates'][symbol]
rescue JSON::ParserError => e
  puts "Failed to parse JSON: #{e.message}"
end

fetch_exchange_rate('USD', 'ZAR')
