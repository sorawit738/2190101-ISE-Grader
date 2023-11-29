users = dict()
users["Pop"] = {"minion", "spiderman"}
users["Tim"] = {"ju-on", "minion"}
users["Pun"] = {"minion"}
users["Puk"] = {"avenger", "batman", "spiderman"}
users["Tan"] = {"spiderman"}

def calculate_user_scores(query, users):
  user_scores = dict()
  for user, watched_movies in users.items():
    watched_movies_from_query = watched_movies & query
    total_movies = watched_movies | query
    # print(user, watched_movies_from_query, total_movies)
    if watched_movies.issubset(query) or watched_movies_from_query == set():
      user_scores[user] = 0
    else:
      score = round(len(watched_movies_from_query)/len(total_movies),2)
      user_scores[user] = score

  return user_scores

def recommend_movies(query, users, user_scores):
  recommend = set()
  max_score = max(user_scores.values())
  if max_score == 0:
    return 'No recommendation'

  for user, watched_movies in users.items():
    if user_scores[user] == max_score:
      recommend = recommend | watched_movies - query

  return sorted(list(recommend))


def main():
  n = int(input())
  query = set()
  for i in range(n):
    query.add(input().lower())
  user_scores = calculate_user_scores(query, users)
  print(sorted(user_scores.items()))
  recommend = recommend_movies(query, users, user_scores)
  print(recommend)

main()