import os
import re

with open(os.getcwd()+"\\responseContent.html") as fd:
    content = fd.read()

hlines = content.splitlines()
msg = []

#If len > 0, the HTML line given contains this kind of brackets < >
def tag_lines (input):
    re_list = ['<', '>']
    matches = []

    for r in re_list:
        matches += re.findall(r, input)

    return len(matches)

#Takes the HTML lines with HTML tags and returns the codification
#depending on if it has a space between the brackets or not.
def retrieve_msg_spaces (input):
    match1 = re.search('<\s', input)
    match2 = re.search('\s>', input)

    if(tag_lines(input) > 0):
        if (match1):
            msg.append(1)
        else:
            msg.append(0)


        if (match2):
            msg.append(1)
        else:
            msg.append(0)