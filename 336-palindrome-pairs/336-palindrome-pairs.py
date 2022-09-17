class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        # dictionary by comprehension
        # key   : word
        # value : index of word
        word_index_dict = { word:index for index, word in enumerate(words) }
        
        # use set's property to avoid repeated pairs
        index_of_palindrome_pair = set()
        
        # check each word and its possible palindrome combination
        for index, word in enumerate(words):
            
            for i in range(0,len(word)+1, +1):
                
                # Make a bipartite partition with index i
                # word = left + right
                left    = word[:i]
                right   = word[i:]
                
                
                # If left is palindrome, and reverse of right exists,
                # then right[::-1] + left + right = right[::-1] + word is also a palindrome
				
                if left == left[::-1] and word_index_dict.get( right[::-1], -1) not in (index, -1):
                    index_of_palindrome_pair.add( (word_index_dict[ right[::-1] ], index ) )
                    
                    
					
                # If right is palindrome, and reverse of left exists,
                # then left + right + left[::-1] = word + left[::-1] is also a palindrome.
				
                if right == right[::-1] and word_index_dict.get( left[::-1], -1) not in (index, -1):
                    index_of_palindrome_pair.add( (index, word_index_dict[ left[::-1] ] ) )
        
        
        # convert set of tuple to list of list as final result
        result = list( map (list, index_of_palindrome_pair) )
        
        return result