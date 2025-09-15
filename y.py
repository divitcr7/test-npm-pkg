def random_word_generator(length: int = 8) -> str:
    """Generate a random word of specified length."""
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    word = ''
    
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)
    
    return word.capitalize()