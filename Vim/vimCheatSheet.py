# Based on https://www.youtube.com/watch?v=wlR5gYd6um0&feature=youtu.be
# Checkout https://www.youtube.com/channel/UCUR1pFG_3XoZn3JNKjulqZg for more vim tutorials

motions = u""" Basic Commands (Motions)  \n
go line up:				k  
go line down:				j  
go x line up:				{x}k
go x lines down:			{x}j  
forward one word:			w  
back by one word:			b
go to end of line:			$
find next char (forward/backward):	f/F  
search:					/{word}
"""

basicActiveCommands = """ Basic Commands (Active - Changes thae document) \n
repeat previous command:			.
delete char under cursor:			x
replace char under cursor:			r
delete char under cursor, go to insert mode:	s
delete a word/paragraph: 			daw/p  
change a word/paragraph: 			caw/p  
copy a word/paragraph:				yaw/p  
delete line:					dd  
change line:					cc  
copy line:					yy  
delete/change/copy x next lines:		d/c/y{x}j
paste:						p  
undo: 						u  
indent right/left:				>/<  	
indent x lines right/left:                      >/< {x}j
"""

textObjects = """ Further nouns - Text Objects \n
'inner word':		iw  
'inner tag':		it  
'inner quotes':		i"  
'inner paragraph':	ip  
'a sentence':		as  
Many commands in vim are of the form {verb}+{noun}. 
For example: delete a sentence: das.
"""

combinedCommands = """ Combination Commands \n
change everything until char X:		ct{X}
change everything until word X:		c/{X}
change inner word (repeatable):		ciw
insert letter {L} x times:		esc x i {L} esc esc
"""

complexCommands = """ ':' Commands \n
Find each occurrence of 'foo' (in all lines), and replace it with 'bar' (and ask for confirmation:
# :%s/foo/bar/gc \n
Format json file: # :%!python -m json.tool 
"""

otherCommands =  """ Other Commands:
open config file in terminal:		vim ~/.vimrc
"""

pluginInstructions = """ Plugin Commands:
checkout https://github.com/junegunn/vim-plug/blob/master/doc/plug.txt for installing plugins.
find more plugins on
https://github.com/kana/vim-textobj-user/wiki
----------------------------------------------------------------------------------------------------
COMMENTS Plugin:
Look here for possible problems: https://stackoverflow.com/questions/13469194/i-cant-work-with-nerdcommenter
Look here for documentation: https://github.com/scrooloose/nerdcommenter
"""

commandsList = ["motions", "basicActiveCommands", "textObjects", "combinedCommands", \
                 "complexCommands", "otherCommands", "pluginInstructions", "allCommands"]

allCommands = motions+basicActiveCommands+textObjects+combinedCommands+combinedCommands+\
                complexCommands+otherCommands+pluginInstructions

commandsDict = {"motions": motions,
                "basicActiveCommands": basicActiveCommands,
                "textObjects": textObjects,
                "combinedCommands": combinedCommands,
                "complexCommands": complexCommands,
                "otherCommands": otherCommands,
                "pluginInstructions": pluginInstructions,
                "allCommands": allCommands
        }

def displayCommands(commands):
    print(commandsDict[str(commands)])

def main():
    print("Please choose one the following options: \n")
    out = ""
    for i in range(len(commandsList)):
        out += commandsList[i]+", "
    selection = str(input(out[:-2]+": \n"))
    print("\n"+commandsDict[selection])

while True:
    main()


