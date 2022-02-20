import os
import re
from pprint import pprint
from bs4 import BeautifulSoup


def get_attributes(content):

    fatt = None

    # --- OBTAIN AL EXISTENT ATTRIBUTES --->
    if(content.find("< ") >= 0):
        content = content.replace("< ", "<")

    if(content.find(" >") >= 0):
        content = content.replace(" >", ">")

    soup = BeautifulSoup(content, 'html.parser')
    # [tag.attrs for tag in soup.findAll('a')]
    try:
        fatt = soup.find_all()[0].attrs
        if(len(fatt)==0):
            fatt = None

    except IndexError as e:
        fatt = None
    # <--- OBTAIN AL EXISTENT ATTRIBUTES ---

    return fatt



def get_clean_tag(line):

    isclean = False
    tag = None

    pattern = r'<(.*?)>'
    match = re.search(pattern, line)

    # See that there is a tag in the line
    if(match):
        # discard all spaces but the ones inside the tag
        tag = match.group()

        # See that is not a comment
        if((tag.find("<!--")==-1) and (tag.find("< !--")==-1)):
            isclean = True

    return isclean, tag



def num_attributes_line(line):

    maxlines = 0

    isclean, content = get_clean_tag(line)

    if(isclean):

        att = get_attributes(content)
        if(att is not None):
            maxlines = len(att)

    return maxlines



def max_bits_line(line):

    num_bits = 0
    num_att = num_attributes_line(line)

    # apply log base 2 to (line!)
    if(num_att > 1):
        num_bits = num_att-1

    return num_bits



def encode_line(line, bits):

    maxlines = 0
    enc = None

    isclean, content = get_clean_tag(line)

    if(isclean):

        att = get_attributes(content)
        print(att)

        # ORDER DICTIONARY TAKING INTO ACCOUNT THE PROPOSED ALGORITHM
        # crete dict with keys the position and for values the key of the attribute
        tosort = {}
        cont = 0
        for v in att.keys():
            tosort[cont] = v
            cont += 1

        print(tosort)

        # take transformation to attributes
        for k,v in tosort.items():
            # sorted value
            sv = []
            sv[:] = v # separate into list of characters
            sv.sort() # sort alphabetically
            sv.append(sv[0]) # put first char at the end
            del sv[0] # delete first char so second char is the first
            sv = ''.join(sv) # recreate string from the list
            tosort[k] = sv # change the value to the transformed value

        print(tosort)
        # sort alphabetically inverse the values
        att_sorted = {entry[0]:entry[1] for entry in sorted(tosort.items(), key = lambda x: x[1], reverse=True)}
        print(att_sorted)

        # apply algorithm to encode bits

        # now you have specific order in the attributes
        # take original attributes and get first and last word
        # search in the original string "line" and create new string
        # with new ordenated attributes

    return line

# sv = []
# sv[:] = "asljflajsf"
# sv.sort()
# print(sv)
# sv.append(sv[0])
# del sv[0]
# print(sv)
# sv = ''.join(sv)
# print(sv)

test = [
    "          <link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\">       ", # 2
    "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\" >    ",
    "     < link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\">",
    "           <link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\" >     ",
    "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\">",
    "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\">",
    "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" >",
    "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" >",
    "<link>",
    "< link>",
    "<link >",
    "< link >",
    "<!-- ======= Slider Section ======= -->",
    "<!-- ======= Slider Section ======= -- >",
    "< !-- ======= Slider Section ======= -->",
    "< !-- ======= Slider Section ======= -- >",
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d22864.11283411948!2d-73.96468908098944!3d40.630720240038435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sbg!4v1540447494452" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen>',
    '< iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d22864.11283411948!2d-73.96468908098944!3d40.630720240038435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sbg!4v1540447494452" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen>',
    '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d22864.11283411948!2d-73.96468908098944!3d40.630720240038435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sbg!4v1540447494452" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen >',
    '< iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d22864.11283411948!2d-73.96468908098944!3d40.630720240038435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sbg!4v1540447494452" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen >',
    '<!DOCTYPE html>',
    '< !DOCTYPE html>',
    '<!DOCTYPE html >',
    '< !DOCTYPE html >',
    '<meta content="width=device-width, initial-scale=1.0" name="viewport">',
    '< meta content="width=device-width, initial-scale=1.0" name="viewport">',
    '<meta content="width=device-width, initial-scale=1.0" name="viewport" >',
    '< meta content="width=device-width, initial-scale=1.0" name="viewport" >',
]

output = [
    2,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    6,
    6,
    6,
    6,
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    2,
]



def main():

    newhtml = []

    for t,o in zip(test, output):
        print(t)
        # see how many bits can you encode in the line
        num_bits = max_bits_line(t)
        # take first num_bits from the message
        bits = None # TEMP***
        # encode those x bits in the line
        newline = encode_line(t, bits)
        newhtml.append(newline)

        print()
        break; # TEMP***

    htmlString = "\n".join(newhtml)



# test to get all the possible bits to embed in a html file
def test_bits_total():

    print("Working directory:", os.getcwd())
    with open(os.getcwd()+"/stego/responseContent.html") as fd:
        content = fd.read()

    # content = '<input type="text" data-msg="Please enter at least 8 chars of subject" />' # 2

    hlines = content.splitlines()
    print("\n")
    print("Total HTML characters:\t", len(content))
    print("Total HTML lines:\t", len(hlines))

    bits = 0

    for line in hlines:
        bits += max_bits_line(line)

    print("Total Bits to embed:\t", bits, "\n")





# test if num_attributes_line works properly
def test_num_attributes_line():

        for t,o in zip(test, output):

            num_att = num_attributes_line(t)
            print(t, o, num_att)
            assert(o==num_att)



if __name__ == "__main__":
    # test_bits_total()
    # test_num_attributes_line()
    main()
