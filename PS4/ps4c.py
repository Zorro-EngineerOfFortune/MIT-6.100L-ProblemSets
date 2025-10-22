# Problem Set 4C
# Name:
# Collaborators:

import json
from ps4b import (
    Message,
    EncryptedMessage,
    PlaintextMessage,
)  # Importing your work from Part B


### HELPER CODE ###
def load_words(file_name):
    """
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    with open(file_name, "r") as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(" ")])
        return wordlist


def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    # Remove punctuation and convert to lowercase before checking against the word list
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()

    # Check for membership in the pre-loaded word list
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]  # Remove trailing newline/whitespace


def get_story_pads():
    with open("pads.txt") as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = "words.txt"
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    """
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    """
    # Initialize the word list once for efficiency
    worldlist_new = load_words("words.txt")

    # Wrap the ciphertext string into the EncryptedMessage object from ps4b
    cph_txt = EncryptedMessage(ciphertext)

    # These lists are used to collect potential plaintexts and their scores
    possib_text = []
    possib_text_final = []
    pads_scores = []

    # Loop 1: Decrypt and collect all potential plaintexts
    for n in pads:
        # Decrypt the message and get the resulting text string
        string_temp = (cph_txt.decrypt_message(n)).get_text()

        # Split the text into a list of words
        list_temp = string_temp.split()
        possib_text.append(list_temp)

    # Loop 2: Score each potential plaintext
    for text in possib_text:
        count = 0
        for word in text:
            # Check if word is valid (returns True/False, which is treated as 1/0 when added)
            c = True == is_word(worldlist_new, word)
            count += c
        # Append the total valid word count for this pad's decryption
        pads_scores.append(count)

    # Find the maximum score achieved across all pads
    max_val = max(pads_scores)

    # Loop 3: Identify the pad(s) that achieved the maximum score
    for i in range(len(pads_scores)):
        if pads_scores[i] == max_val:
            # Collect the word list for the successful decryption
            possib_text_final.append(possib_text[i])
            # Store the index of this successful pad (updates on ties)
            pad_num = i

    # Create the final PlaintextMessage object using the correct pad index
    answer = PlaintextMessage(possib_text_final[-1], pads[pad_num])
    return answer


def decode_story():
    """
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    """
    # 1. Get the encrypted story text and the list of pads
    story = decrypt_message_try_pads(get_story_string(), get_story_pads())

    # 2. Extract and return the final plaintext string
    return story.get_text()


if __name__ == "__main__":
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
    pass
