# Fallout Pseudo Hack
# Copyright (C) 2019 Ashley Roberge

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import random
import base64
import time

def main():

        specials="\\`~!@#$%^&*()_+-=[]{}|;:\'<,>./?\""
        garbage=0
        wordPos=0

        f = open('falloutdictlist.txt', 'r')
        with open('falloutdictlist.txt') as f:
                read_data = f.read()
        
        words = read_data.splitlines()
        randWord = ""
                
        while True:
         
                randHex = "0x" + format(random.randint(61440, 65535), 'X')
                print( randHex, end=" ", flush=False )

                for i in range(12):
                        if (wordPos > len(randWord) - 1):
                                wordPos = 0
                                randWord = words[random.randint(0, len(words) - 1)]
                                garbage=random.randint(4,54)
                        if (garbage > 0):
                                print(specials[random.randint(0, len(specials) - 1)], end="", flush= False)
                                garbage = garbage - 1
                        elif (wordPos <= len(randWord)):
                                print(randWord[wordPos], end="", flush=False)
                                wordPos = wordPos + 1
                print("")
                time.sleep(0.2)

if __name__=='__main__':
        main()
