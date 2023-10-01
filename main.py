#cleaing Text steps
import string
from collections import Counter
text=open('Data/rise-of-e-health-and-its-impact-on-humans-by-the-year-2030-.txt',encoding='utf-8').read()
lower_case=text.lower()
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
tokenized_word=cleaned_text.split()
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_word=[]
final_count=0
for word in tokenized_word:
    if word not in stop_words:
        final_word.append(word)
        final_count=final_count+1
# "After removing the words"
# print(final_word)   
positive_score=[]
count=0
with open('NP/positive-words.txt','r') as file:
    for line in file:
        clear_line=line.replace('\n','')
        #for dictionary word,emotion=line.split(':')
        # print(clear_line)  
        if clear_line in final_word:
            positive_score.append(clear_line)
            count=count+1
print("final word count:",final_count)            
print("Positive word count:",Counter(positive_score))  
  
# print(positive_score)      
# print(tokenized_word)

# print(cleaned_text)
