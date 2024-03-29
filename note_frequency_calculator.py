import re

def filter(string, substr):
    return [str for str in string 
    if re.match(r'[^\d]+|^', str).group(0) in substr]

#this is a hack
octave = [
    'C','C#','D','D#','E','F','F#','G','G#','A','A#','B'
]

#this is probably very bad
def note(n_given):

    #rest
    if filter('z', n_given):
        return 0.1 #0 breaks it
    
    octave_up = 1
    n_processed = n_given
    if n_given.islower():
        octave_up += 1
        n_processed = n_given.upper()
        
    for char in n_given:
        if char == ',':
            octave_up = octave_up / 2
        if char == '\'':
            octave_up = octave_up * 2    
            
    n = octave.index((filter(octave, n_processed))[-1])
    return 2**(n / 12) * 261.63 * octave_up
    
    