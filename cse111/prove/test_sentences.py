from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import random
import pytest

def test_get_determiner():
    single_determiners = ["a", "one", "the"]
    for _ in range(20):
        word = get_determiner(1)
        assert word in single_determiners

    plural_determiners = ["some", "many", "the"]
    for _ in range(20):
        word = get_determiner(0)
        assert word in plural_determiners

def test_get_adjective():
    adjectives = ["charming", "cruel", "fantastic", "gentle", "huge", "perfect", "rough", "sharp", "tasty", "zealous"]
    for _ in range(20):
        word = get_adjective()
        assert word in adjectives

def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(20):
        word = get_noun(1)
        assert word in single_nouns
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(20):
        word = get_noun(0)
        assert word in plural_nouns

def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(20):
        word = get_verb(0, "past")
        assert word in past_verbs
    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(20):
        word = get_verb(1, "present")
        assert word in present_single_verbs
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(20):
        word = get_verb(0, "present")
        assert word in present_plural_verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(20):
        word = get_verb(0, "future")
        assert word in future_verbs

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(20):
        word = get_preposition()
        assert word in prepositions

def test_get_prepositional_phrase():
    # test preposition
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # test noun
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    # test determiner
    single_determiners = ["a", "one", "the"]

    plural_determiners = ["some", "many", "the"]
    
    # test prepositional phrase
    for _ in range(20):
        single_prep = get_prepositional_phrase(1)
        single_prep = single_prep.split()
        assert single_prep[0] in prepositions
        assert single_prep[1] in single_determiners
        assert single_prep[2] in single_nouns
        
        plural_prep = get_prepositional_phrase(0)
        plural_prep = plural_prep.split()
        assert plural_prep[0] in prepositions
        assert plural_prep[1] in plural_determiners
        assert plural_prep[2] in plural_nouns       

pytest.main(["-v", "--tb=line", "-rN", __file__])