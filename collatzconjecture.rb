#!/usr/bin/ruby

while 1 == 1 do
	p = 0
	puts "Enter your starting number: "
	n = gets.chomp.to_i
		while n > 1 do
			if n % 2 == 0
				n = n / 2
				p = p + 1
				puts "#" + p.to_s + ": " + n.to_s 
			else
				n = 3 * n + 1
				p = p + 1
				puts "#" + p.to_s + ": " + n.to_s 
			end
		end
end