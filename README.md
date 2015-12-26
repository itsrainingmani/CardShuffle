# CardShuffle

While my friend was shuffling a deck of cards, he wondered what would happen if the shuffle was perfect, ie, if the deck of 2n cards was split evenly into 2 piles of n cards and these cards were merged evenly back into a single deck. 

After performing this shuffle on decks of size 4 and 6, we wondered how many steps would it take for a deck of 52 cards to become perfectly shuffled. I wrote a program that performs this operation in python and we discovered that the exact number of steps to perfectly shuffle 52 cards was 12. 

Out of curiosity we ran the program on decks of sizes ranging from 2 to 52 where n is even and input this sequence into the OEIS (Online Encyclopedia of Integer Sequences) database and we discovered that the sequence gives the number of Mongean shuffles needed to perfectly shuffle a deck of 2n cards.
