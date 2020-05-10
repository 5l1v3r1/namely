#!/usr/bin/python3

from string import Template
import itertools
import re
import argparse
import pathlib
import sys


banner = '''
 __  _  __  __ __ ___ _ __   __
|  \| |/  \|  V  | __| |\ `v' /
| | ' | /\ | \_/ | _|| |_`. .' 
|_|\__|_||_|_| |_|___|___|!_!  

by Oriel & Tyler Kranig

github.com/OrielOrielOriel
github.com/tylerkranig

'''
#  Defines path as the parent directory of the script + the character '/'
PATH = str(pathlib.Path(__file__).parent.absolute()) + '/'


def createSubstitutionDictionary(template, first, last, domain):
	"""
	Creates a dictionary to be passed to safe_substitute()
	Dictionary outlines the relationship between template
	variables and the values they are being substituted with.

	Requires a template formatted string, first name, last name,
	and domain name. 

	The initial dictionary works for all templates not requiring
	a string indice operation to be performed on a name. 

	The regex finds strings matching ${firstX} or ${lastX} where
	X is an integer. It uses X as the end value for a string index
	of the corresponding first/last name. 
	"""

	search = re.findall('\${(first|last)(\d+)}', template)

	substitution_dictionary = {
			'first': first,
			'last': last,
			'domain': domain
	}
	
	for pattern in search:
		key = ''.join(pattern)
		length = int(pattern[1])
		name = first if pattern[0] == 'first' else last

		substitution_dictionary[key] = name[:length]

	return substitution_dictionary

"""
Constructs the CLI argument parser. 

The default path for the *file arguments is equal to 
a certain filename concatenated to the parent directory
of the script file as defined by pathlib and instantiated
at the start of the script.  

"""

def parseArguments():
	parser = argparse.ArgumentParser(description=banner, formatter_class=argparse.RawTextHelpFormatter)

	parser.add_argument('-n', '--name',
		metavar='name',
		nargs=2,
		type=str, 
		help='A single name'
	)
	parser.add_argument('-nf', '--namefile',
		metavar='namefile',
		type=str,
		help='A list of names'
	)

	parser.add_argument('-d', '--domain',
		metavar='domain',
		type=str,
		help='A single domain'
	)
	parser.add_argument('-df', '--domainfile',
		metavar='domainfile',
		type=str,
		help='A list of domains'
	)

	parser.add_argument('-t', '--template',
		metavar='template',
		type=str,
		help='A single template'
	)
	parser.add_argument('-tf', '--templatefile',
		metavar='templatefile',
		type=str,
		default=PATH+'templatelist.txt',
		help='A list of templates'
	)	

	parser.add_argument('-o', '--outfile',
		metavar='outfile',
		type=str,
		help='The file to output to'
	)

	return parser

"""
The following load* functions accept a filename, open 
that filename, and return a list consisting of each line, 
stripped of '\n' characters. 

The loadNames function also splits each line at the first
whitespace, expecting each line to be in the format:

		first last 

The loadFile function returns a file opened in write mode
where the file's name is the inputted filename. 

"""

def loadNames(parserArgument):
	with open(parserArgument, "r") as all_names:
		return [name.strip('\n').split() for name in all_names.readlines()]

def loadDomains(parseArgument):
	with open(parseArgument, "r") as all_domains:
		return [domain.strip('\n') for domain in all_domains.readlines()]

def loadTemplates(parseArgument):
	with open(parseArgument, "r") as all_templates:
		return [template.strip('\n') for template in all_templates.readlines()]

def loadFile(parseArgument):
	return open(parseArgument, "w")

"""
The following write* functions are responsible for 
outputting the correctly formatted emails to stdout
or to a specified file.

The writeToFile function is hard coded to write to 
the outfile variable, which is globally instantiated in 
main(). Newline characters '\n' are concatenated to each
email. 

"""


def writeToTerminal(email):
	print(email)

def writeToFile(email):
	outfile.write(email + '\n')



def main():
	global outfile  #  Instantiates outfile as a global variable for use by writeToFile().
	parser = parseArguments()  #  Launches the parser.


	#  If no CLI arguments are provided, print the argparse help screen. 
	if len(sys.argv)==1:
	    parser.print_help(sys.stderr)
	    sys.exit(1)

	parser = parser.parse_args()  #  Parses the provided CLI arguments.


	#  Raises an exception if either names or domains are missing from the CLI arguments.
	if not (parser.name or parser.namefile):
		raise Exception('No names provided. Use either -n or -nf')

	if not (parser.domain or parser.domainfile):
		raise Exception('No domains provided. Use either -d or -df')


	#  Chooses between a single paramter provided in the CLI or a specified file containing multiple lines of parameters. 
	names = [parser.name] if parser.name else loadNames(parser.namefile)
	domains = [parser.domain] if parser.domain else loadDomains(parser.domainfile)
	templates = [parser.template] if parser.template else loadTemplates(parser.templatefile)


	#  Opens the filename provided by the CLI, or sets itself to None.
	outfile = loadFile(parser.outfile) if parser.outfile else None  


	#  Chooses which write* function to use based on if an outfile argument was provided. 
	write_function = writeToFile if parser.outfile else writeToTerminal


	#  Iterates over each combination of domain, name, and template and passes the output to the chosen write* function.
	for domain, name, template in itertools.product(domains, names, templates):
		template = Template(template)  #  Creates a Template() object based on the template.
		first, last = name  #  Assigns first, last to name[0] and name[1] respectively. 

		substitution_dictionary = createSubstitutionDictionary(template.template, first, last, domain)  #  Defines the substitution dictionary.


		#  Substitutes the keys in template with the associated pairs as defined in substitution_dictionary.
		#  The function safe_substitutes() leaves a key alone if does not find an associated value.
		email = template.safe_substitute(substitution_dictionary)  


		#  The variable 'write_function' is equivalent to one of the write* functions as instantiated before the for loop.
		write_function(email)  


	#  Closes the specified outfile if it exists.
	if outfile:
		outfile.close()


if __name__ == '__main__':
	main()

