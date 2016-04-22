
############ STEP 1: import additional software ############ 
import re
import pprint


############ create some variables we'll use in the program ############ 
# this creates a varible with the name of the file you want to analyze
# you can add more txt files in the same directory and put the filename here
novel = "monte_cristo.txt"

# this is a dictionary ({} brackets) with the broad colour name as the key and a couple of 
# alternate colour names as values in a list (with the [] brackets)
colour_reference = {
	'red': ['red','cardinal', 'scarlet', 'vermilion', 'terracotta', 'crimson', 'claret', 'brick', 'burgundy', 'cerise', 'cherry', 'henna', 'maroon', 'oxblood', 'sanguine'],
	'orange': ['orange', 'jacinthe', 'saffron', 'ocher', 'ochre', 'tangerine'],
	'yellow': ['yellow','citrine', 'goldenrod', 'topaz', 'gold', 'golden', 'apricot', 'blond', 'blonde', 'gamboge', 'lemon', 'maize', 'straw', 'wheat'],
	'green': ['green', 'celadon', 'chlorochrous', 'emerald', 'jade', 'cobalt', 'olive', 'sage', 'teal', 'verdigris', 'veridity'],
	'blue': ['blue','periwinkle', 'azure', 'slate', 'sapphire', 'aqua', 'aquamarine', 'cadmium', 'canary', 'cerulean', 'navy', 'turquoise'],
	'violet': ['violet', 'purple', 'indigo', 'ianthine', 'mauve', 'amethyst', 'eggplant', 'aubergine', 'lavender', 'lilac', 'puce', 'tyrian', 'orchil'],
	'pink': ['pink', 'rose', 'blush', 'carnation', 'coral', 'fushia', 'salmon'],
	'black' : ['black', 'atrous', 'melanic', 'ebony', 'jet', 'sable', 'soot'],
	'brown': ['brown', 'tan', 'khaki', 'beige', 'bronze', 'bronzed', 'buff', 'umber', 'caramel', 'chestnut', 'chocolate', 'coffee', 'copper', 'fawn', 'hazel', 'mustard', 'mahogany', 'mocha', 'sepia', 'taupe', 'tawny', 'topaz'],
	'gray' : ['gray', 'grey', 'ash', 'ashen', 'charcoal', 'drab', 'heather', 'heathered', 'marble', 'silver', 'argent'],
	'white' : ['white', 'albicant', 'albugineous', 'ivory', 'ecru', 'alabaster', 'bone', 'chalk', 'frostiness', 'hoariness', 'zinc'],
}
# sources: http://phrontistery.info/colours.html, http://www.enchantedlearning.com/wordlist/colours.shtml
# https://www.vocabulary.com/lists/540059#view=notes

# these two dictionaries will hold our results
basic_colour_count = {} # keys only
all_colour_count = {} # values only
word_count = 0
pct_count = {}

############ STEP 2: open the txt files and break them into lists of words we can evaluate ############ 
# this creates an file called novel_text that we'll break down 
novel_text = open(novel)

for each_line in novel_text:
	# this removes trailing spaces
	stripped_line = each_line.rstrip()
	# this removes spaces between words and turns each line into a list that looks like this:
	# ['Walton!', '', 'Seek', 'happiness', 'in', 'tranquillity', 'and', 'avoid', 'ambition,', 'even', 'if', 'it']
	line_list = stripped_line.split(" ")
	
############ STEP 3: check each word against our color reference dictionary and count matches ############ 
	for each_word in line_list: 
		word_count += 1
		# this takes each word and removes punctuation, any remaining space and makes it lowercase
		# e.g. "Walton!" becomes "walton"
		cleaned_word = re.sub('[^A-Za-z0-9]+', '', each_word).lower()
		# the if statement checks if the word matches any of the keys in our colour_reference dictionary
		if cleaned_word in colour_reference:
			# if it does, we increment the count for that word in our basic_colour_count dictionary
			basic_colour_count[cleaned_word] = basic_colour_count.get(cleaned_word, 0) + 1
		# now we check for the more specialized words by checking the values in colour_reference
		for key, value in colour_reference.iteritems():
			# check every word in the value list and see if it's the cleaned_word
			for option in value:
				if option == cleaned_word:
					# the next few lines just tell the program to increment values in the dictionary, 
					#and add new sub dictionaries (aka 'nested dictionaries') where needed
					if key in all_colour_count:
						if option in all_colour_count[key]:
							all_colour_count[key][option] += 1
						else:
							all_colour_count[key][option] = 1
					else:
						all_colour_count[key] = {}
						all_colour_count[key][option] = 1


############ printing commands ################
# this just makes the output look nice :)
# adjust the indent number if more whitespace is needed
pp = pprint.PrettyPrinter(indent=2)

print "***** Analysis for" , novel, "*****"
print "The word count is: ", word_count
print "basic colour count for the most common colour words only (keys, eg 'blue', 'red', etc): "
pp.pprint(basic_colour_count)
print
print "secondary colour count organized by top level colors and includes all values: "
pp.pprint(all_colour_count)
print "************************************"




