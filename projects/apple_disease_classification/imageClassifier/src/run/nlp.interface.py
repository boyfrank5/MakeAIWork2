#!/usr/bin/env python
from sentence_transformers import SentenceTransformer, util

# Parameters: (nog te koppelen aan 'batch_classifier')
batchOneAql = 'class1'
batchOneNormal = 80
batchOneRot = 0
batchOneScab = 0
batchOneBlotch = 0

model = SentenceTransformer('all-MiniLM-L6-v2')

# De antwoorden te de chatbot returned:
sentences = [(f'The quality of the batch is: {batchOneAql}.'),
             (f'The amount of normal apples in batch one: {batchOneNormal}.'),
             (f'The amount of rotten apples in batch one: {batchOneRot}.'),
             (f'The amount of scab apples in batch one: {batchOneScab}.'),
             (f'The amount of blotch apples in batch one: {batchOneBlotch}.'),
             (f'Statistics of batch one:\n\tNormal apples: {batchOneNormal}.\n\tRotten apples: {batchOneRot}.\n\tScab apples: {batchOneScab}.\n\tBlotch apples: {batchOneBlotch}.'),

             (f'Hello, what would you like to know?'),
             (f'80 apples are inspected for the AQL test.'),
             (f'We use a batch size of eighty apples for the AQL process!'),
             (f'Here you will find a great apple pie recipe: www.omasappeltaart.nl.')
             ]

#Encode all sentences
embeddings = model.encode(sentences)

#Compute cosine similarity between all pairs
cos_sim = util.cos_sim(embeddings, embeddings)

#Add all pairs to a list with their cosine similarity score
all_sentence_combinations = []
for i in range(len(cos_sim)-1):
    for j in range(i+1, len(cos_sim)):
        all_sentence_combinations.append([cos_sim[i][j], i, j])

#Sort list by the highest cosine similarity score
all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[0], reverse=True)


#Start Chatbot
print('Hello, how can I help?')

i=0

while i < 5:
  questionChatbot = input()

  theQuestion = model.encode(questionChatbot, convert_to_tensor=True)
  print(f'\t{questionChatbot}') 
  answerArray = util.dot_score(theQuestion, embeddings)
  # print("Similarity:", util.dot_score(theQuestion, embeddings))
  answerlocation = (answerArray.argmax())
  print(sentences[answerlocation.item()])
  i += 1

print('\nHave a nice day!')
    