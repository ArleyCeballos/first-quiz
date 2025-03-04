import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """
SELECT animals.name, animals.species, animals.age
FROM animals
LEFT JOIN people_animals ON animals.animal_id = people_animals.pet_id
WHERE people_animals.owner_id IS NULL;
"""


# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """
SELECT COUNT(*) AS pet_count
FROM animals
JOIN people_animals ON animals.animal_id = people_animals.pet_id
JOIN people ON people_animals.owner_id = people.person_id
WHERE animals.age > people.age;
"""


# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """
SELECT p.name AS person_name, a.name AS pet_name, a.species
FROM people AS p
JOIN people_animals AS pa ON p.person_id = pa.owner_id
JOIN animals AS a ON pa.pet_id = a.animal_id
WHERE p.name = 'bessie' AND a.animal_id NOT IN (
    SELECT pet_id
    FROM people_animals
    GROUP BY pet_id
    HAVING COUNT(owner_id) > 1
);
"""
