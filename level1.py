import string

# discovering sectret message


del_from_cde = {
    ord('a') : None,
    ord('b') : None,
}

abc = string.ascii_lowercase

cde = abc.translate(del_from_cde)
cde += 'ab'

# print message

msg1 = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

msg2 = msg1.maketrans(abc, cde)

print("Message: \n" + msg1.translate(msg2), "\n\n")

url1 = "map"
url2 = url1.maketrans(abc, cde)

print("Change link to to: \n http://www.pythonchallenge.com/pc/def/" + url1.translate(url2) + ".html")