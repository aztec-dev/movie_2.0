# Movies to Watch 2.0 by Azariah Pundari

A Python project with GUI and Console programs that (re)use classes to manage a list of *Movies to Watch*.

# Project Reflection

## 1. How long did the entire project take you?

### Estimate:

2 days

### Actual:

3 - 4 days

## 2. What are you most satisfied with?

I am most satisfied with getting to know how to use classes. I personally liked how it simplified the program and
breaking large chunks of the program into smaller parts. I realised that I had to keep appending in the first
assignment, however for this one, it was just one single line. I don't know about you but this does put a smile on my 
face.

It is also very satisfying when I finally get to figure out something that I've been working on for hours and seeing it
work as intended and it matches the sample output gives me so much ecstasy. Such bliss. 

## 3. What are you least satisfied with?

I am least satisfied with how long it takes me solve a specific problem. For example, for sort using attrgetter, it took
20 hours to get it to work (I may be exaggerating for added effect), thankfully I was able to use the video/practical 
references to get it to run.

## 4. What worked well in your development process?

What worked well was the a1_classes.py, I didn't spend a lot of time on it, it was fairly simple to run through the
initial program and updating everything to use the classes. I commented out a lof of the unused functions as they were
no longer required.

## 5. What about your process could be improved the next time you do a project like this?

I really need to improve upon thinking systematically. I usually skim read a lot and I do that with code too, I'd skip 
a huge chunk of code that I've written previously, and it leaves me confused at times as to what my code is doing. I've
found that going through my code systematically, it made me realised that some lines where just not required which leads
to not repeating myself and getting a better use of SRP.

## 6. Describe what learning resources you used and how you used them.

The learning resources I used were the videos that Lindsay has put up for our pleasure and kivy documents for best
practices with kivy. It was tempting to use stack overflow but Lindsay has stated that everything that is required for 
this assignment has been taught by him through the videos, so I stayed clear from stack overflow. The videos where used 
to get to understand the kivy demos better and specific functions like attregetter.

I also used the kivy demos and much of the program copying and pasting those demos and changing them to use my classes 
and other variables. I don't know if this is allowed but if they're provided for us to use then I might as well.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

The main challenges & obstacles for this assessment was the self.root.ids.id_name.text - this seriously confused me so
much throughout the entirety of this assessment that I had to go over what each component mean consistently. The 
positioning of the names, for example - does root comes before or after ids etc., was a problem, kivy doesn't have 
autocomplete, so I had to get used to it quickly.

Another challenge was how my program was using 'Button' instead of my method. It kept on saying 'Button' does not have
this or that. This was an easy fix but, it took a long time to fix - it was literally removing the variable and just 
calling movie.method_name.

One of the hardest challenges was getting my attrgetter to work. It wasn't working due to the key being a 'dict' due
to the file being a .json. This  took so long to figure out but thankfully Lindsay explains this using the guitar 
examples.

The last challenge was the error checking in kivy. This took a while as I've never done error checking using kivy 
before. Thankfully, was able to get it working after doing research if it was possible to return two components as I
realised I had to return a string and a True or False value if the try suite failed.

The usual input method was different as well so much so that it took a while for me to figure out how to do error 
checking in my main.py.

## 8. Briefly describe your experience using classes and if/how they improved your code.

In summary, my experience using classes was fulfilling, at first it started off hard and quite difficult to wrap my head 
around but having to go through my assignment 1 and updating it to use classes really helped alot, and I mean ALOT. It
has improved my code by making it clean and concise and with proper naming (I am unsure if my names are up to standards)
it tells you what the code is going to do. 

Classes have also improved my code by minimizing repetition. I am surprised at how much functions I had to comment 
out in my first assignment. Makes me realise that I have a lot to work on. Another improvement is how I can read through
my code and actually understand what it's doing. Usually reading through my code after a day or two I would get confused
but after this, I can say that I can grasp what it's trying to do.

I found myself getting mixed up as to what comes after the '.'. When using kivy, I found there to be no shortcuts, 
although this is due to kivy itself and not PyCharm. This results in me having to do double takes on what my class 
methods are and ensuring im using the correct class, thankfully PyCharm does give errors if the method isn't in the 
called class.
