# Author: <Perris Navarro> <perrisn@uoregon.edu>

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
Version 0.2 has been updated for PS4.'''

__version__ = "0.2"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNAbases = set('ATGCNatcgn')
RNAbases = set('AUGCNaucgn')

def convert_phred(letter: str) -> int:
    """Converts a single character into a phred score""" 
    return ord(letter)-33

def validate_base_seq(seq,RNAflag=False):
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    return set(seq)<=(RNAbases if RNAflag else DNAbases)

def validate_base_seq():
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    pass

def gc_content():
   def gc_content(DNA):
    '''Will calculate the total DNA content and then calculate the GC content, and returns as a decimal'''
    DNA=DNA.upper() #Make sure sequence is all uppercase
    content_GC=DNA.count ("G") + DNA.count ("C") #Count number of Cs and Gs
    return (content_GC/len(DNA)) 
    

def oneline_fasta():
    '''Making a change for github assignment again.'''
    '''Making a change for github assignment.'''
    '''Adding another change.'''
    pass

def qual_score(phred_score: str) -> float:
    """Takes a string of phred_score as a parameter and calculates the average quality score of the whole phred string"""
    total:int=0
    for letter in (phred_score):
        total+=convert_phred(letter)
    
    return total/len(phred_score)

if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")

    assert qual_score("EEE") == 36
    assert qual_score("#I") == 21
    assert qual_score("EJ") == 38.5
    assert qual_score(phred_score) == 37.62105263157895, "wrong average phred score"
    print("Your convert_phred function is working! Nice job")

    assert validate_DNA_seq(DNA), "String contains invalid characters - are you sure you used DNA sequence?"