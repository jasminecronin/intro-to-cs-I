"""Assignment 5: Semantic Similarity
This program builds a large list of semantic descriptors for every unique
word in one or more large pieces of text (such as novels), which are used to
determine one word's semantic similarity to another. A test is then
administered to evaluate the program's accuracy at choosing the correct
synonym when given a different word.

Author: Jasmine Roebuck, Dec. 8, 2017"""


import time


def main():
    """Calls to build the semantic descriptors dictionary, then runs the
    synonyms test. Results are printed to the console."""
        
    testfile = 'test.txt' # The text file with the synonyms test
    texts = ['Proust.txt', 'Tolstoy.txt'] # The novels to process
    
    start_time = time.clock()
    descriptors = build_semantic_descriptors_from_files(texts)
    end_time = time.clock()
        
    score = run_similarity_test(testfile, descriptors, cosine_similarity)
    run_time = float("{0:.2f}".format(end_time-start_time)) # Format time
    print('Accuracy: {0}%   Run Time: {1} sec.'.format(score, run_time))


def norm(vec):
    """Given a sparse vector vec, returns its length as a float value."""
    
    sum_of_squares = 0.0  # Float for large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return sum_of_squares ** 0.5


def cosine_similarity(vec1, vec2):
    """Given two sparse vectors vec1 and vec2 (stored as dictionaries),
    returns the cosine similarity between them."""
    
    dot_product = 0.0 # Float for large numbers
    for k in vec1:
        if k in vec2: # Only consider positive entries
            dot_product += vec1[k] * vec2[k]
    sim = dot_product / (norm(vec1) * norm(vec2)) # Cosine similarity
    return sim


def build_semantic_descriptors(sentences):
    """Given a 2D list of strings sentences, returns a dictionary dict that
    contains all words in sentences as keys. Each key points to another 
    dictionary representing the semantic descriptor vector for that word."""
    
    dict = {}
    # Build a single count of words for each sentence
    for sentence in sentences: 
        subdict = {}
        for word in sentence:
            if word in subdict:
                subdict[word] += 1 # Increment if the word appeared before
            else:
                subdict[word] = 1 # Else create new entry
        # Make copies and insert subdict into dict
        for k in subdict: 
            w = subdict.copy()
            w.pop(k) # Exclude each word from it's own dictionary
            if k in dict: # Word already has a vector
                for j in w:
                    if j in dict[k]:
                        dict[k][j] += w[j] # Add counts
                    else:
                        dict[k][j] = w[j] # Create entry
            else: # Add new word to the dictionary
                dict[k] = w       
    return dict
                    

def build_semantic_descriptors_from_files(filenames):
    """Given a list of strings representing names of large text files, 
    returns a dictionary of the semantic descriptor vectors for all the words
    in the files. Multiple files are treated as a single piece of text.""" 
    
    sentences = []
    for filename in filenames:
        file = open(filename, 'r', encoding='utf-8')
        text = file.read().lower() # Change capital letters
        file.close()             
        # Builds the 2D list of words for each text file
        sentences.extend(build_sentence_list(text))  
 
    dict = build_semantic_descriptors(sentences)
    return dict
    
    
def build_sentence_list(text):
    """Given a string text representing a large piece of text, returns a 2D
    list where the outer list represents sentences and the inner lists are
    individual words. Strips all punctuation and whitespace.""" 
    
    sentences = []
    punctuation = ',---:;\'"“”()'
    finished = False
    while not finished: # Find the next sentence
        stops = [text.find('.'), text.find('!'), text.find('?')]
        while min(stops) == -1 : # Necessary when close to end of text
            stops.remove(-1)   # and we stop finding end punctuation
            if stops == []: # No more end punctuation in the text
                finished = True
                break
        if finished: # Stop processing,
            break     # discard anything after the last '.', '!', or '?'
        next_stop = min(stops) # Location of next '.', '!', or '?'
        sentence = text[:next_stop] # Slice off the sentence
        text = text[next_stop + 1:] # Set aside the remainder
        lst = sentence.split() # Create the list of words
        i = 0 # Replacement iteration variable, since..
        while i != len(lst): # length of the list will change here
            lst[i] = lst[i].strip(punctuation) # Remove outer punctuation
            if lst[i].find('-') != -1: # Remove dashes inside words
                lst = lst[:i] + lst[i].split('-') + lst[i + 1:]
            i += 1
        while '' in lst: # Removes empty leftovers
            lst.remove('') 
        sentences.append(lst) # Add processed sentence to larger list
    return sentences
            

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):  
    """Given a string word, a list of strings choices, and a dictionary
    semantic_descriptors, returns the element from choices which has the
    largest semantic similarity to word using the data from the dictionary
    and the similarity function similarity_fn. Prints an error message if one
    of the test words does not have a descriptor in the dictionary."""
    
    try: # If test word is not in text files, results in KeyError
        v1 = semantic_descriptors[word] # Grab the vector for the word
        similarities = []
        for choice in choices:
            v2 = semantic_descriptors[choice] # Grab the vector for choice
            sim = similarity_fn(v1, v2) # Calculate similarities
            similarities.append(sim)
        max = similarities[0]
        for num in similarities:
            if num > max:
                max = num
        best_choice = similarities.index(max)
        return choices[best_choice]
    except:
        print('KeyError: Tested word was not found in the text.')
        return 'N/A'


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    """Given a string filename referring to a test text file, returns the
    percentage of questions on which most_similar_word guesses the answer
    correctly using the data in semantic_descriptors and the similarity
    function similarity_fn."""
    
    file = open(filename, 'r')
    score = 0
    total = 0
    for line in file.readlines():
        test = line.split()
        word = test[0] # The given word in the test question
        actual = test[1] # The actual synonym
        choices = test[2:] # The answer choices
        answer = most_similar_word(word, choices, semantic_descriptors, 
                                    similarity_fn)
        if answer == actual: # Returned correct answer
            score += 1
        total += 1
    file.close()
    result = (score / total) * 100 # Calculate percentage score
    result = float("{0:.1f}".format(result)) # Format the score
    return result


main()
