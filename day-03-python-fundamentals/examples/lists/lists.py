'''# Challenge 1: Student Score Manager

scores = [85, 92, 78, 90, 88]

print("First score:", scores[0])
print("Last score:", scores[-1])
print("Number of scores:", len(scores))

scores.append(95)

lowest_score = min(scores)
scores.remove(lowest_score)

average_score = sum(scores) / len(scores)

high_scores = [score for score in scores if score > 85]

print("Average score:", average_score)
print("Scores above 85:", high_scores)


# Challenge 2: Temperature Data Cleaning

temperatures = [23, 25, None, 27, "30", 22, None, 28]

clean_temperatures = [
    int(temp) for temp in temperatures 
    if temp is not None
]

total = 0

for temp in clean_temperatures:
    total += temp

average_temp = total / len(clean_temperatures)

high_temp = [
    temp for temp in clean_temperatures 
    if temp > 25
]

print("Clean temperatures:", clean_temperatures)
print("Average temperature:", average_temp)
print("Temperatures above 25:", high_temp) '''
movies = [
    "Inception",
    "Interstellar",
    "Avatar",
    "Titanic",
    "Matrix",
    "Gladiator"
]

# First 3 movies
print(movies[:3])

# Last 2 movies
print(movies[-2:])

# Reverse list
print(movies[::-1])

# Every second movie
print(movies[::2])


