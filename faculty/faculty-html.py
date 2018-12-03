import re
import sys
import fileinput
# from argparse import *

# def main(args):
def main():
	outputfile = open("gen-faculty-directory.html", "w").close(); # Clear File
	outputfile = open("gen-faculty-directory.html", "a");

	outputfile.write("<div>\n")

	with open("input.txt", "r") as inputs:
		for i, inputline in enumerate(inputs):
			if i >= 1:
				template = open("faculty-template.html", "r");
				print("line", i, ": ", inputline)
				person = inputline.split(" | ")
				person[2] = repr(person[2]).replace("\\n", "").replace("\'", "")
				print(person[2])

				for templateline in template:
					new_line = templateline.replace("@!professor", person[0]).replace("@!phone", person[1]).replace("@!email", person[2])
					# print(new_line)
					outputfile.write(new_line)
				outputfile.write("\n")
				template.close();

	outputfile.write("\n</div>")

	print("\nCreated gen-faculty-directory.html")

# Process Command Line Arguments
def entrypoint():
	main()

# Runs Entrypoint to do Argument Parsing
if __name__ == "__main__":
    entrypoint()