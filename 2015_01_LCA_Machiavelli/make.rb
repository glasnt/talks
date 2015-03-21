#!/usr/bin/ruby

if ARGV.length < 2

	puts "#{$0} \"Title of Slide\" number_of_slides"
	exit
end

title = ARGV[0]
slideno = ARGV[1].to_i
list = "list.txt"
slidefolder = "slides"

file = title.tr(" ","")

title_slide = <<EOF
<section class="title">
<h1>#{title}</h1>
</section>
EOF
	


x = "#{slidefolder}/#{file}0.html"
File.open(x, "w") { |f| f.write(title_slide)}
File.open(list, "a") {|f| f.puts x }

content = <<EOF
<section>
<h1>#{title}</h1>
<p>
<ul><li>Things</li></ul>
</p>
</section>
EOF

(1..slideno).each do |n|
	x = "#{slidefolder}/#{file}#{n}.html"

	File.open(x, "w") { |f| f.write(content)}
	File.open(list, "a") {|f| f.puts x }
end
