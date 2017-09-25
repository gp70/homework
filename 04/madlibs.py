import random as r

initstory = """
There once a(n) NOUN who lived in a NOUN . NAME lived by it , and one day , NAME
PASTTENSEVERB , which made it feel ADJECTIVE . NAME lived ADVERB ever after .
"""

finstory=""
name=""
nounlist=["couch", "dog", "foot", "aardvark", "candy", "pirate", "eagle", "table", "chair", "house", "world eater"]
verblist=["jump","eat","attacc","protecc","ride","smash","meme","slay"]
ptverblist=['jumped','ate','killed','attacced','proteccted','rode','smashed','memed','slayed','roared']
adverblist=['amazingly', 'astoundingly','astonishingly','distractingly','cutely']
adjlist=['glorious','bounteous','big','furious','intelligent']
namelist=['Christopher Walken','Rick Astley','Donald Duck','Pikachu']
pronounlist=['They','He','She']

story = initstory.split()

for i in story:
    if "PRONOUN" in i:
        i = pronounlist[r.randrange(len(pronounlist))]
        finstory += " "+ i
    elif "PASTTENSEVERB" in i:
        i= ptverblist[r.randrange(len(ptverblist))]
        finstory += " "+i
    elif "ADVERB" in i:
        i = adverblist[r.randrange(len(adverblist))]
        finstory += " "+i
    elif "ADJECTIVE" in i:
        i = adjlist[r.randrange(len(adjlist))]
        finstory += " "+i
    elif "VERB" in i:
        i = verblist[r.randrange(len(verblist))]
        finstory += " "+i
    elif "NOUN" in i:
        i = nounlist[r.randrange(len(nounlist))]
        finstory += " "+i
    elif "NAME" in i:
        if name != "":
            i = name
            finstory += " "+i
        else:
            i = namelist[r.randrange(len(namelist))]
            name=i
            finstory += " "+i
    elif "," in i:
        finstory += ","
    elif "." in i:
        finstory += "."
    else:
        finstory += " "+i
            

print(finstory)
