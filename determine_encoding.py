
#   [file]:     determine_encoding.py
#   [desc]:     determine the encodings of a given file
#   [date]:     December 9 2022
#   [author]:   Donny-GUI
#   [notes]:    run function example() to see an example ran on this file

import os
from string import printable

ENCODINGS_NAMES = ['ascii', 'big5', 'big5hkscs', 'cp037', 'cp273', 'cp500', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp865', 'cp874', 'cp875', 'cp932', 'cp949', 'cp950', 'cp1006', 'ibm1026', 'cp1140', 'ibm1140', 'cp1250', 'windows-1250', 'cp1251', 'windows-1251', 'cp1252', 'windows-1252', 'cp1253', 'windows-1253', 'cp1254', 'windows-1254', 'cp1255', 'windows-1255', 'cp1256', 'windows-1256', 'cp1257', 'windows-1257', 'cp1258', 'windows-1258', 'euc_jp', 'eucjp, ujis, u-jis', 'euc_jis_2004', 'jisx0213, eucjis2004', 'euc_jisx0213', 'eucjisx0213', 'euc_kr', 'euckr, korean, ksc5601, ks_c-5601, ks_c-5601-1987, ksx1001, ks_x-1001', 'gb2312', 'chinese, csiso58gb231280, euc-cn, euccn, eucgb2312-cn, gb2312-1980, gb2312-80, iso-ir-58', 'gbk', 'gb18030', 'gb18030-2000', 'hz', 'hzgb, hz-gb, hz-gb-2312', 'iso2022_jp', 'csiso2022jp, iso2022jp, iso-2022-jp', 'iso2022_jp_1', 'iso2022jp-1, iso-2022-jp-1', 'iso2022_jp_2', 'iso2022jp-2, iso-2022-jp-2', 'iso2022_jp_2004', 'iso2022jp-2004, iso-2022-jp-2004', 'iso2022_jp_3', 'iso2022jp-3, iso-2022-jp-3', 'iso2022_jp_ext', 'iso2022jp-ext, iso-2022-jp-ext', 'iso2022_kr', 'csiso2022kr, iso2022kr, iso-2022-kr', 'latin_1', 'iso-8859-1, iso8859-1, 8859, cp819, latin, latin1, L1', 'iso8859_2', 'iso-8859-2, latin2, L2', 'iso8859_3', 'iso-8859-3, latin3, L3', 'iso8859_4', 'iso-8859-4, latin4, L4', 'iso8859_5', 'iso-8859-5, cyrillic', 'iso8859_6', 'iso-8859-6, arabic', 'iso8859_7', 'iso-8859-7, greek, greek8', 'iso8859_8', 'iso-8859-8, hebrew', 'iso8859_9', 'iso-8859-9, latin5, L5', 'iso8859_10', 'iso-8859-10, latin6, L6', 'iso8859_11', 'iso-8859-11, thai', 'iso8859_13', 'iso-8859-13, latin7, L7', 'iso8859_14', 'iso-8859-14, latin8, L8', 'iso8859_15', 'iso-8859-15, latin9, L9', 'iso8859_16', 'iso-8859-16, latin10, L10', 'johab', 'cp1361, ms1361', 'koi8_r', 'kz_1048, strk1048_2002, rk1048', 'maccyrillic', 'mac_greek', 'macgreek', 'mac_iceland', 'maciceland', 'maclatin2, maccentraleurope, mac_centeuro', 'mac_roman', 'macroman, macintosh', 'macturkish', 'csptcp154, pt154, cp154, cyrillic-asian', 'shift_jis', 'csshiftjis, shiftjis, sjis, s_jis', 'shift_jis_2004', 'shiftjis2004, sjis_2004, sjis2004', 'shift_jisx0213', 'shiftjisx0213, sjisx0213, s_jisx0213', 'utf_32']


##      determines which encodings will be 100% 'readable', as in "can be printed safely"

class Encoding:
    """ Determine the encoding of a file.
    :params:
        file: string,     file object for testing
    :returns:
        list of strings of encodings
     """

    def __init__(self, file:str) -> list[str]:

        if "/" not in file:
            self.path = f"{os.getcwd()}/{file}"
        else:
            self.path = file
        if os.path.exists(self.path):
            self.encodings = self.determine_use()
        print(self.encodings)

    def determine_use(self) -> list[str]:
        usable = []
        # go through all the encoding strings
        for encoding in ENCODINGS_NAMES:
            try:
                # open the file with encoding
                with open(self.path, encoding=encoding, mode='r') as rfile:
                    lines = [x for x in rfile.readlines()]
                words = [line.split(" ") for line in lines[0:]]
                # get the lines, words, chars, within the file. 
                # For the first ten lines, If the character is not in ascii printable, 
                # then it cant be printed and the encoding cant be used reasonably.
                # if the file fails to open, it isnt appended to 'usable'. if the first 10 lines of 
                # the file pass, then it is acceptable and the search continues
                for index, line in enumerate(words):
                    if index > 10:
                        usable.append(encoding)
                        break
                    for word in line:
                        for char in word:
                            if char not in printable:
                                break
                usable.append(encoding)
            except:
                continue 
        return usable


# Examples

def example():
    file = Encoding('determine_encoding.py')