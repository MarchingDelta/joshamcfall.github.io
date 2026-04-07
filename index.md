## **Introduction**
Hi! My name is Joshua McFall and I have been in the SNHU computer science for 3 years. This github page is to showcase my final project for CS-499 to graduate with a Bachelor's Degree.

# **Enhancement One: Software Design and Engineering**

The artifact for the software engineering and design category I chose was my project from IT 145 that I completed in November 2023. It is a database application (that ironically utilizes no database) that stores animals that have been rescued. The goal of this class was to make a program that lets the rescuers easily find/edit information about the rescued animals without having to use physical records. I selected this item because it is a good chance to renovate the structure of the project since I made this program at a time where I did not have any understanding of software development cycle nor design, so a lot of it is either lumped into 1 file or has some aspects of spaghetti code. 

[Enhancement 1](https://github.com/MarchingDelta/cs499-capstone/tree/MarchingDelta-enhancement-1)


# **Enhancement Two: Algorithms and Data Structures**

Thinking of Data Structures and Algorithms, this is where some optimizations for a program would take place by changing how some logic works so that it has the same output, but utilizing more optimized algorithms. Usually, this would mean to work on any weak links of the program; in this case being accessing the animals SQL database. SQL select queries are already fairly quick, ranging from O(1) if using a primary key for lookups and O(n) for full table scans with no indexes. Now, putting a primary key on the search id for all animals would achieve this goal quite easily, I wanted to use a more local solution. With that, I implemented a cache into the program. This cache is made of a hashed key-value pair dictionary that stores the search ID of any animal that has been queried recently along with the amount of times they have been queried. This adds some customization to the cache as it not only makes queries on popular animals quicker it also keeps count of how many times they have been searched. That data in itself can be used to show popularity for the listed animals, which can reveal some patterns as to why those animals are popular when analyzing traits. 

[Enhancement 2](https://github.com/MarchingDelta/cs499-capstone/tree/MarchingDelta-enhancement-2)

# **Enhancement Three: Databases**

I plan on implementing an SQL database to the program. I picked SQL over MongoDB due to the former having a fixed schema. This keeps everything consistent as all animals need to have the same type of information; name, date of rescue, type of animal, etc. Although MongoDB has strong horizontal scaling due to its ability to shard across servers, it also brings the risk of having malformed entries due to no schema, so some animals may be entered without having critical information. I used the same artifact as the previous 2 enhancements, since this project did not have a database system at all when it was first developed. And it was better to start off with a clean slate since the possibilities of future features are more open due to no restrictions. After doing this enhancement, I have met the goal and implemented an SQL database system into this program. 

[Enhancement 3](https://github.com/MarchingDelta/cs499-capstone/tree/MarchingDelta-enhancement-3)
