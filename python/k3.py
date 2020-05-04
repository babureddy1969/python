words = []
with open("british-english.txt") as fh:
    for line in fh:
        word = line.strip()
        words.append(word)
for word in ["holpful", "kundnoss", "holpposs", "blagrufoo", "liberdi"]:
    neighbors = get_neighbors(words, 
                              words, 
                              word, 
                              3,
                              distance=levenshtein)
    print("vote_distance_weights: ", vote_distance_weights(neighbors, 
                                                           all_results=False))
    print("vote_prob: ", vote_prob(neighbors))

	