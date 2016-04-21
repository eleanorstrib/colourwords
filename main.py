import re

novel = "monte_cristo.txt"

color_reference = {
	'red': ['red', 'cardinal'],
	'orange': ['orange', 'jacinthe', 'saffron'],
	'yellow': ['yellow', 'citrine', 'goldenrod'],
	'green': ['green', 'celadon', 'chlorochrous'],
	'blue': ['blue', 'periwinkle', 'azure'],
	'violet': ['violet', 'purple', 'indigo', 'ianthine'],
	'black' : ['black', 'atrous', 'melanic'],
	'white' : ['white', 'albicant', 'albugineous'],
}

meta_color_count = {}
secondary_color_count = {}

novel_text = open(novel)

for each_line in novel_text:
	stripped_line = each_line.rstrip()
	line_list = stripped_line.split(" ")
	# ['Walton!', '', 'Seek', 'happiness', 'in', 'tranquillity', 'and', 'avoid', 'ambition,', 'even', 'if', 'it']

	for each_word in line_list: 
		cleaned_word = re.sub('[^A-Za-z0-9]+', '', each_word).lower()
		if cleaned_word in color_reference:
			meta_color_count[cleaned_word] = meta_color_count.get(cleaned_word, 0) + 1
		for key, value in color_reference.iteritems():
			for option in value:
				if option == cleaned_word:
					secondary_color_count[option] = secondary_color_count.get(option, 0) + 1


print meta_color_count
print secondary_color_count