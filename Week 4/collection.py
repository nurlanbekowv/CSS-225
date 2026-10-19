# Samat
# 10/18/2026
# Stores authors and the year they died, then prints each one like:
# Charles Dickens died in 1870.

authors = {
    "Charles Dickens": 1870,
    "William Thackeray": 1863,
    "Anthony Trollope": 1882,
    "Gerard Manley Hopkins": 1889
}

for author, year in authors.items():
    print(author + " died in " + str(year) + ".")
