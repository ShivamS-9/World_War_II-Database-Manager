# World War II Database Management System Project

## Overview  
This project is a comprehensive Database Management System (DBMS) for analyzing and managing data related to **World War II**. It includes functionalities such as insertion, modification, projection, and deletion of data stored in a relational database. The database contains normalized tables in **1NF**, **2NF**, and **3NF**, ensuring data integrity and efficient query processing.
---

## Features  
The system provides the following operations:

### 1. **Insertion**
- **Countries Table**: Add details like name, alliance, political leader, population, and invading country.
- **Weapons Table**: Insert weapon details, including type, place of origin, mass, and dimensions.
- **Soldiers Table**: Add soldier details, including name, rank, place of death, and national ID.

### 2. **Update**
- Update the political leader of any country.
- Update the date of death for a soldier.

### 3. **Projection**
Retrieve data using queries like:
- List all soldiers and their respective countries.
- Get details of casualties during bombing campaigns.
- Display the number of refugees and military deaths for a specific country.
- List influential personalities with their name, nationality, and occupation.
- Display battle details, including participating soldiers and casualties.
- Show countries captured by each input country.
- Display the average mass of all weapon types.
- Find the country with the maximum number of refugees.
- Compare the aftermath of Allied and Axis Powers post-war.

### 4. **Deletion**
- Remove records from the **Influential Personalities** table.
- Delete entries from the **Casualties** table.

---

## Technical Details  

### ER Model
The ER Model is included in the ER_Model.pdf file. The database design follows strict normalization rules as follows:  
- **1NF**: Each table contains atomic values with a unique identifier.  
- **2NF**: Ensures all non-key attributes are fully functionally dependent on the primary key.  
- **3NF**: Removes transitive dependencies for better data integrity.

### Tech Stack  
- **Database**: MySQL  
- **Backend**: Python (`pymysql` for database connectivity)  
- **Libraries**: `os`, `pymysql`

