def get_similar_docs(query, k, score= False):
  if score:
    similar_docs= index.similarity_search_with_score(query=query, k=k)
  else:
    similar_docs= index.similarity_search(query=query, k=k)

  return similar_docs