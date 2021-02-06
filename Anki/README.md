Contains Anki addons and tricks.

# fontRandomizer.html

This script randomizes the style of your Anki cards.

Your should learn vocabulary without relying on the association with the font/size/style of the character,
because your brain will then connect two unrelated concept to each other. You should rather learn the 'essence' of
the character. My proposal to enforce learning the essence of characters is by changing the style of character
every time you see it. Another bonus is that every charater is something 'new', increasing the surprise effect and thus making it more fun to study.
In this way you learn like a good Machine Learning algorithm that has a diverse dataset and is optimized to generalize, not overfit. 

How to use:

1) Open Anki on the Desktop version
2) click on **Browse**
3) Choose a Deck on the left. Below the right column where the cards are listed is located a button called **Cards...**. click on that.
4) Replace the **Front Template** with the content of fontRandomizer.html.
   Note, in fontRandomizer.html you might need to replace {{Front}} by the label of the front field. Most of the time it's just called "Front".
   If it's not go back and look up the name of the Front field, it is found below the **Cards...** button. If for instance the Front is labeled 
   "Hanzi", then you to replace {{Front}} by {{Hanzi}}.
   
   The template is then applied to all cards with the same card type, so you don't need to do this for every single card! Note however, that this also affects cards in          other decks with the same card type. If you don't want that, then you should create a new card type specifically for that deck you want to randomize.

That's it!
If you want to change the list of possible fonts, then just look up the array *fontList* in the fontRandomizer.html and add/remove fonts. You can look up possible fonts on the internet by googling "list of html css fonts" or something like that.
If you don't want to randomize size, font-weight, or color, then just comment out Lines 34, 35 and 36 by adding "//" in front of each of these lines.

This script will not modify your card information in the database. Therefore, in order to remove the fontRandomizer just remove the code in **Front Template**.
