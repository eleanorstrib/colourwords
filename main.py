# this is additional software that helos me get rid of the non-alphanumeric characters below
import re

# this creates a varible with the name of the file you want to analyze
# you can add more txt files in the same directory and put the filename here
novel = "monte_cristo.txt"

# this is a dictionary ({} brackets) with the broad color name as the key and a couple of 
# alternate color names as values in a list (with the [] brackets)
color_reference = {
	'red': ['cardinal'],
	'orange': ['jacinthe', 'saffron'],
	'yellow': ['citrine', 'goldenrod'],
	'green': ['celadon', 'chlorochrous'],
	'blue': ['periwinkle', 'azure'],
	'violet': ['violet', 'purple', 'indigo', 'ianthine'],
	'black' : ['black', 'atrous', 'melanic'],
	'white' : ['white', 'albicant', 'albugineous'],
}

# these two dictionaries will hold our results
meta_color_count = {} # keys
secondary_color_count = {} # values

# this creates an file called novel_text that we'll break down 
novel_text = open(novel)

for each_line in novel_text:
	# this removes trailing spaces
	stripped_line = each_line.rstrip()
	# this removes spaces between words and turns each line into a list that looks like this:
	# ['Walton!', '', 'Seek', 'happiness', 'in', 'tranquillity', 'and', 'avoid', 'ambition,', 'even', 'if', 'it']
	line_list = stripped_line.split(" ")
	
	for each_word in line_list: 
		# this takes each word and removes punctuation, any remaining space and makes it lowercase
		# e.g. "Walton!" becomes "walton"
		cleaned_word = re.sub('[^A-Za-z0-9]+', '', each_word).lower()
		# the if statement checks if the word matches any of the keys in our color_reference dictionary
		if cleaned_word in color_reference:
			# if it does, we increment the count for that word in our meta_color_count dictionary
			meta_color_count[cleaned_word] = meta_color_count.get(cleaned_word, 0) + 1
		# now we check for the more specialized words by checking the values in color_reference
		for key, value in color_reference.iteritems():
			for option in value:
				if option == cleaned_word:
					if key in secondary_color_count:
						if option in secondary_color_count[key]:
							secondary_color_count[key][option] += 1
						else:
							secondary_color_count[key][option] = 1
					else:
						secondary_color_count[key] = {}
						secondary_color_count[key][option] = 1


print "***** Analysis for" , novel, "*****"
print "meta color count of the high level groupings of color words (keys): ", meta_color_count
print "secondary color count including only non-top level words(values): " , secondary_color_count