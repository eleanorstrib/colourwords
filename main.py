
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
	'red': ['red', 'reddish', 'ruddy', 'cardinal', 'scarlet', 'vermilion', 'terracotta', 'crimson', 'claret', 'brick', 'burgundy', 'cerise', 'cherry', 'henna', 'maroon', 'oxblood', 'sanguine'],
	'orange': ['orange', 'jacinthe', 'saffron', 'ocher', 'ochre', 'tangerine'],
	'yellow': ['yellow', 'yellowish', 'citrine', 'goldenrod', 'gold', 'golden', 'apricot', 'blond', 'blonde', 'gamboge', 'lemon', 'maize', 'straw', 'wheat'],
	'green': ['green', 'greenish', 'celadon', 'chlorochrous', 'emerald', 'jade', 'cobalt', 'olive', 'sage', 'teal', 'verdigris', 'veridity'],
	'blue': ['blue', 'bluish', 'periwinkle', 'azure', 'slate', 'sapphire', 'aqua', 'aquamarine', 'cadmium', 'canary', 'cerulean', 'navy', 'turquoise'],
	'violet': ['violet', 'purple', 'indigo', 'ianthine', 'mauve', 'amethyst', 'eggplant', 'aubergine', 'lavender', 'lilac', 'puce', 'tyrian', 'orchil'],
	'pink': ['pink', 'pinkish', 'rose', 'blush', 'carnation', 'coral', 'fushia', 'salmon'],
	'black' : ['black', 'blackish', 'atrous', 'melanic', 'ebony', 'jet', 'sable', 'soot'],
	'brown': ['brown','brownish', 'tan', 'khaki', 'beige', 'bronze', 'bronzed', 'buff', 'umber', 'caramel', 'chestnut', 'chocolate', 'coffee', 'copper', 'fawn', 'hazel', 'mustard', 'mahogany', 'mocha', 'sepia', 'taupe', 'tawny', 'topaz'],
	'gray' : ['gray', 'grey', 'grayish', 'greyish', 'ash', 'ashen', 'charcoal', 'drab', 'heather', 'heathered', 'marble', 'silver', 'argent'],
	'white' : ['white', 'albicant', 'albugineous', 'ivory', 'ecru', 'alabaster', 'bone', 'chalk', 'frostiness', 'hoariness', 'zinc'],
}
# sources: http://phrontistery.info/colours.html, http://www.enchantedlearning.com/wordlist/colours.shtml
# https://www.vocabulary.com/lists/540059#view=notes

# these two dictionaries will hold our results
overall_colour_count = {} # values only
word_count = 0
colour_word_count = 0


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
		
		for key, value in colour_reference.iteritems():
			# check every word in the value list and see if it's the cleaned_word
			for option in value:
				if option == cleaned_word:
					colour_word_count += 1
					# the next few lines just tell the program to increment values in the dictionary, 
					#and add new sub dictionaries (aka 'nested dictionaries') where needed
					if key in overall_colour_count:
						if option in overall_colour_count[key]:
							overall_colour_count[key][option][0] += 1
							overall_colour_count[key][option][1] = (float(overall_colour_count[key][option][0])/float(word_count))*100
						else:
							overall_colour_count[key][option] = [1, float(1)/float(word_count)]
					else:
						overall_colour_count[key] = {}
						overall_colour_count[key][option] = [1, float(1)/float(word_count)]



############ printing commands ################
# this just makes the output look nice :)
# adjust the indent number if more whitespace is needed
pp = pprint.PrettyPrinter(indent=2)

print "***** Analysis for" , novel, "*****"
print "The word count is: ", word_count
print "The colour word count is", colour_word_count, "or", (float(colour_word_count)/float(word_count))*100, "percent of the word count"
print
print "Overall colour count is organized by top level colors and includes all values; for each color word the first value is the raw count, second value is the percentage of the total word count: "
pp.pprint(overall_colour_count)
print "************************************"




