A History Of Software
=====================

(editor overview)
Turing to software - Bomba, Min ACE, first stored program computer - changing your own programming.  
Changing your own programming is the definting point of software - the hardware became capable of making a turing complete machine. 
1950 paper - can machines think
Manchester Baby. Pivot of world to USA. Von Neumman

52-54 road to fortran, plus turing death.
UK self inflicted wound of last two years of turings life and migration of computing to USA.
'debug this silent monster'. The 1-1 line conversion vs conceptual ladder of fortran

60s Unix, Thomson, breaking grip of large corporations

70s lisp grows up, AI winter, functional 

80s as rise of open source and 90s rise of PC, and internet, 'a PC on every dsktop' to iPhone a supercomputer in every pocket.
80s also OO computing as response to AI winter - again important sell to corporate world (see agile)

Next step is agents working on our behalf - needing improved security, meaning of privacy and abiity to view review it ourselves and self programming - open and programmable.  And to move beyond the individual to programming the group, the company, the society.

Intro
-----

I believe that software is best seen as a new form of literacy, and so it has two competing aims - to be able to run as billions of binary instructions on a CPU, and also to be comprehesible to human minds.  I am incapable of performing billions of binary calculations per second, but on a daily basis my collegues and I share software that we can read, imagine running and are able to reason about the outcomes of the software and the bugs we have inevitably added and diverted us from the true purpose of coffee drinking.  

So Software has two compilers to target - (trained) human minds, and the hardware inside every Motherboard.  The English you are reading has only one compiler to target my brain and your brain - the (trained) human mind.  Yes I am deliberatly linking between the use of human written languages and software code.  I bang on about this a lot.

How we got there is the story of geniuses and mortals, war, organisational guerillas, and a faith that openness and transparency will triumph.

Notes:
Manchester University Transistor Computer, is generally regarded as the first transistor-based stored-program computer having become operational in November 1953
so was the transistor computer, following the arc laid out by turing


Manchester Baby
- stored program
- the software was division
so ran repeatedly 
- software could be anything (well just calculations but you know)
store was wiliams tube - https://en.m.wikipedia.org/wiki/Williams_tube
Basically a cyhorde ray tune that charged on the stored dots faded over time - thus they were read back and faded over time. 
at this point any instructions coukd be kept in its 32x32 bits if memory, but the underlying hardware needed to supply abilities - addition and negation (the earliest CPU) just allowed for addition and subtraction.  Division was thus just 

frankly these things were just fast calculators. indeed thats all CPUs today are.

MUTC was first transistor conouter so we can see how we got to the starting gate by 1948 - stored programs, transistors, NNaND logic.

So a quick trio theough the manchester baby and transistor via turing.




Alan Turing and the road to Software 
------------------------------------

Alan Mathison Turing was 27 years old when he walked through the gates of Bletchly Park, the UK Governments Code and Cipher School (GCCS), just a day after the UK declared war on Germany. 

There is a lovely scene in the 2014 biopic of Turing's life `The Imitation Game` where Benedict Cumberbatch as Turing is having an interview with Charles Dance as 'The Establishment Figure', deciding if Turing should be allowed to work at Bletchly.  Charles Dance's character is pompous and throughout the film provides most of the 'oppostion' to Turing.  Of course we need exposition to explain Turings already astounding genius and where the UK is in the war, but we set up a dynamic here that probably oversells the 'lone genius struggling against a world that does not understand him'.

While I love any film I can persuade my kids to watch that teaches even a passing resemblance to history ("look its him from Avengers"), when he walked into Bletchly Park, Turing had already been working with the UK government and Polish Intelligence in their attempts to break Nazi Ciphers for over a year.

Yes there were difficulties getting sufficient resources to build the bombe, that cracking the Enigma code was always a struggle, but a struggle not against pompous Admirals, but against mathematics itself. Fmously, a letter to Churchill solved most of the resource problems ("give them whatever they need" was the reply), but the enemy remained building a machine to take on nature.  

The Bombe and Colosusss, both used to break German ciphers, were *electro-mechanical*.  That is they lierally moved wires withing themselves (the famous round dials) hunting for one combination of wires that did *not* carry current.  It was much like brute forcing).

(appenix A goes into great detail on how Enigma was broken, and Appenxidx B into the design of ACE, the first stored program coputers.)

This is a side note on the value of organisations that throw off enough money to afford R&D. States and others. We now are a century from the initial R&D of nuclear energy, quantum mechaics, computing and the ROI on those investments are off the scale.  It might be worth diving inot Home Chain Radar, Proximity fuses and so on.

(worth dicussing the home chain radar, bletchly as examples of what UK was supremely good at - organisation on massive Stae scale. Something the spark travelled to USA with).


What was Turing's two big ideas.  The first is that software can *think* - that is learn and adapt its own programming so that it can change.  The Bombe was a calculating machine, but it only did one thing.  The instructions that made the were built in and could not be changed except y outside humad

During the war and afterwarda at Machester, he worked on designing a 'stored program machine" - that 
Turig forsaw software as solution to thinking

I am still sticking with my "software as a form of literacy" concept.  But just as literacy was not possible without some form of mark-making technology (from clay and stick, to ink and pulp) literacy itself "transcends" the technology, but cannot exist without it - a virtual and real life split perhaps.


Different technologies drive different computing capabiities, which drives the software literacy tropes / genres we use to represent the new capabilities.

Yes we could all write assembler or even binary, and you know, people did. But we could all count by marking one line after another till we reached our age, but instead symbols encapsulate greater and greter higher level interpretations.

A story.
Databases waited for the technology to move from tapes to random access disks. Then we could get random access to any chunk of data enabling a new way of laying out data physically allowing for new ways to query and then SQL 
 

I think this is analsous to science fiction writing.
Shakespeare used fairies because aliens were not a well understood concept to his audience.  And rembmer tha software is both expressing ententions to a computer / compiler, it is also (equally? More so?) expressing intentions to the human reader (who needs to agree or understand and partner with the work)

(Brng in the history of the moon story - first science fictin story
https://en.m.wikipedia.org/wiki/Lucian
Lucian of Samosata 
A True History
https://en.m.wikipedia.org/wiki/A_True_Story
)

Biblio:

https://github.com/DJHoffmann/Enigma/blob/master/Enigma.py

We lave Alan with his Apple. (stephen Fry comment)
He foresaw a self modifying machine - and built one. The spark had fled to the USA (politics, Von Braun, organisation, british decline).  But software is a language that had to speak to the computer on how to modify itself but also be understood by the humans.  And at this level of sophistication, humans were mostly understanding at single 1:1 mapping of instructions.  It is as if we counted by making one line on a clay tablet for each addition, instead of using 5 or 7 as symbols.  The next step is to design a language that is short, concise, compact for humans, but *expands* into machin language.



John Backus and the road to Fortran
-------
- Organisation and subversion 
- The development of in redibly sophisiticated weaponry (radar, cavity magnetron, nuclear fission, jet turbines, proximity fuse (Tizzard mission)

all needed computing power to go firther model more


The next step is general computing. Maths is fine and fundamental, but how do we expand outside of maths, how do we share the time on the commputer, how do we build a level of software abstraction that looks after the resources, does the administration of the computer hardware, but does so using the computer, and does so in a way that does not interfere with new growth new needs.  How to we have an operatiing system.  These are no longer single purpose machines but are expected to do many dofferent functions (databases, UI inouts, reporting, a counting) - each different program wants access to the same resources and coukd also go wring and take out everyone else - (malicious was rare!) - how do we adminster all that?  not manually  

UNIX 
----
Editor for mortals
Baked into and starting to eat the world - see rows of accountants and replacing them - films stills of tony hancock and then maggie smith film

Unix leads to common operating system 

How do we unleash the millions of people who want to build for themselves. How do we find the best wayt to build software together.

Linux and the socialism of software 
----------------------
Open, sophisticated but rough, best sevelopemnt practises 

Open in social orgbaisation - the issues of toxic relationships and better solutions

Co-ordination, decision making, large scale software and large scale capitalism.  The challenge of the organisation.  Linux was incredible. Is it the right approach? Failed GUI choices. 

Microsoft, WYSIWIG and dead ends
------------------------
Its not software - low code and no code. Cutting out marvel comic panels and rearrnaging them. It works to an extent and great practitioners can oroduce something *fast*. But it is more like a DJ remixing. There is nothing wrong per se, there is a need for a busines to just get onwoth it.  But from the stand point of a fully literate society, remixing Panels from Marvel comics is missong the point (and dont get me started on the legal issues of trying to add in panels from DC comics!)


Apple, Curated computing, distributed computing

unsolved questions

Any new frontiers in computing or software? ChatGPT just copies.
