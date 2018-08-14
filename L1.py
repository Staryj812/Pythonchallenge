# http://www.pythonchallenge.com/pc/def/map.html



coded_str = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""
coded_url = "http://www.pythonchallenge.com/pc/def/map.html"
additional_symbols = " ,./:"
alphabet = "abcdefghijklmnopqrstuvwxyz" + additional_symbols
coded_alphabet = "cdefghijklmnopqrstuvwxyzab" + additional_symbols
key = str.maketrans(alphabet, coded_alphabet)

decoded_str = coded_str.translate(key)
decoded_url = coded_url.translate(key)
print(decoded_str)
print(decoded_url)

# ocr