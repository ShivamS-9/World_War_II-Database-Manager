import pymysql
import os

def clear_screen():
    os.system('clear')

def connect_to_database():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Sea_Hawk@5478",
        database="dna_project"
    )
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    # if query.lower().startswith('select'):
    results = cursor.fetchall()
    for row in results:
        print(row)


def insertion(t_choice):
    if t_choice==1:
        name = input("Enter country name: ")
        alliance = input("Enter alliance: ")
        political_leader = input("Enter political leader: ")
        population = input("Enter population at start of war: ")
        invading_country = input("Enter invading country: ")

        query = f"INSERT INTO Countries VALUES ('{name}', '{alliance}', '{political_leader}', {population}, '{invading_country}');"

    if t_choice==3:
        # For inserting into Weapons table
        weapon_name = input("Enter weapon name: ")
        weapon_type = input("Enter weapon type: ")
        place_of_origin = input("Enter place of origin: ")
        mass = input("Enter mass: ")
        dimension_id = input("Enter dimension ID: ")

        query = f"INSERT INTO Weapons VALUES ('{weapon_name}', '{weapon_type}', '{place_of_origin}', {mass}, {dimension_id});"

    if t_choice==2:

        soldier_name = input("Enter soldier's name: ")
        
        rank = input("Enter soldier's rank: ")
        place_of_death = input("Enter place of death: ")
        national_id = input("Enter national ID: ")
        query = f"INSERT INTO Casualties (Name, Rank_position, PlaceofDeath, NationalId) VALUES ('{soldier_name}', '{rank}', '{place_of_death}', {national_id});"
    return query

def modification(t_choice):
    if t_choice == 1:
        country_name = input("Enter country name: ")
        leader_name = input("Enter new political leader's name: ")

        query = f"UPDATE Countries SET PoliticalLeader = '{leader_name}' WHERE Name = '{country_name}';"

    if t_choice == 2:
        soldier_name = input("Enter soldier's name: ")
        death_date = input("Enter the date of death: ")

        query = f"UPDATE Casualties SET Diedon = '{death_date}' WHERE Name = '{soldier_name}';"

    return query

def projection(query_choice):
    if query_choice == 1:
        return """SELECT Soldiers.ServiceNumber AS SoldierID, Soldiers.Name AS Name, Countries.Name
                FROM Soldiers
                JOIN Countries ON Soldiers.CountryName = Countries.Name;"""

    elif query_choice == 2:
        return """SELECT Casualties.Name, Casualties.Rank_position, Countries.Name, Casualties.DiedOn,BombingCampaigns.CountryBombed 
                FROM (Casualties JOIN BombingCampaigns ON Casualties.DateID = BombingCampaigns.DateID) 
                JOIN Countries ON Casualties.Nationality = Countries.Name;"""

    elif query_choice == 3:
        country_name = input("Enter country name: ")
        return f"SELECT CountryName AS Country, No_ofRefugees, MilitaryDeaths FROM Aftermath WHERE CountryName = '{country_name}';"

    elif query_choice == 4:
        return """SELECT Name, Nationality, Occupation
                FROM InfluentialPersonalities;"""

    elif query_choice == 5:
        return """SELECT BattlesFought.NameOfBattle, Soldiers.FightingFor AS Country, COUNT(DISTINCT Soldiers.Name) AS SoldiersCount, COUNT(DISTINCT Casualties.Name) AS CasualtiesCount FROM BattlesFought(LEFT JOIN Soldiers ON BattlesFought.ServiceID = Soldiers.ServiceNumber LEFT JOIN Casualties ON BattlesFought.NationalID = Casualties.NationalID) GROUP BY BattlesFought.NameOfBattle, Soldiers.FightingFor;"""

    elif query_choice == 6:
        return """SELECT Count(*) AS NumberOfPrisoners, CapturedByCountry AS Country_Name
                FROM PrisonersOfWar Group by CapturedByCountry
                ORDER BY NumberOfPrisoners DESC;"""
    elif query_choice == 7:
        country_name = input("Enter Table name: ")
        return f"SELECT * FROM {country_name};"
    elif query_choice == 8:
        return """SELECT AVG(Mass) AS AverageMass
                    FROM Weapons
                    GROUP BY Type
                    ORDER BY AverageMass Desc;"""
    elif query_choice == 9:
        return """Select Max( No_ofRefugees) AS Max_Refugees From Aftermath;"""        
    elif query_choice == 10:
        return """Select  No_ofRefugees AS Max_Refugee_Number, CountryName AS Country From Aftermath Order By No_ofRefugees Limit 2;"""    
    elif query_choice==11:
        return """Select SUM(Aftermath.No_ofRefugees) AS Refugee_Num, SUM(Aftermath.Expenditure) AS Expenditure, SUM(Aftermath.MilitaryDeaths) AS Military_Deaths, SUM(Aftermath.CivilianDeaths) AS Civilian_Deaths, Countries.Allegiance AS Allegiance, Sum(Countries.TotalpopulationatStartofWar) AS TotalpopulationatStartofWar
From (Aftermath Join Countries On Aftermath.CountryRelation = Countries.Name)
Group By Allegiance;"""
def deletion(tchoice):
    if t_choice == 1:
        country_name = input("Enter country name: ")
        
        # Constructing the DELETE command for InfluentialPersonalities table
        query = f"DELETE FROM InfluentialPersonalities WHERE countryname = '{country_name}';"

    if t_choice == 2:
        soldier_rank = input("Enter soldier's rank: ")
        
        # Constructing the DELETE command for Casualties table
        query = f"DELETE FROM Casualties WHERE Rank_position = '{soldier_rank}';"

    return query





# main
connection = connect_to_database()

while True:
    clear_screen()
    print("+---------------------------+")
    print("Menu - Actions")
    print("+---------------------------+")
    print("1. Insertion")
    print("2. Modification")
    print("3. Projection")
    print("4. Deletion")
    print("5. Exit")
    print("+---------------------------+")
    choice = eval(input("Enter your choice: "))
    clear_screen()

    if choice == 1:
        print("+---------------------------+")
        print("Menu - Tables for Insertion")
        print("+---------------------------+")
        print("1. Countries")
        print("2. Casualities")
        print("3. Weapons")
        print("+---------------------------+")
        t_choice = eval(input("Enter your choice: "))

        query = insertion(t_choice)
        try:
            execute_query(connection, query)
            print("Query executed successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == 2:
        print("+---------------------------+")
        print("Menu - Tables for Modification")
        print("+---------------------------+")
        print("1. Countries")
        print("2. Casualities")
        print("+---------------------------+")
        t_choice = eval(input("Enter your choice: "))

        query = modification(t_choice)
        try:
            execute_query(connection, query)
            print("Query executed successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == 3:
        print("+-----------------------------------------+")
        print("Menu - Tables for Projection")
        print("+-----------------------------------------+")
        print("1. List all Soldiers and their respective Countries.")
        print("2. Details of Casualities in Bombing.")
        print("3. Display number of Refugees and Military Deaths for a specific Country.")
        print("4. List Name, Nationality, Occupation of Influential Personalities.")
        print("5. Display Details of Battles.")
        print("6. Display the Number of Prisoners Captured by each Country.")
        print("7. Display a Table.")
        print("8. Display Average Mass of all Weapon types.")
        print("9. Display Max Number of Refugees.")
        print("10. Display 2 Countries with Lowest Number of Refugees.")
        print("11. Display AfterMath Comparison between Allied and Axis Powers.")
        print("+-----------------------------------------+")
        t_choice = eval(input("Enter your choice: "))

        query = projection(t_choice)
        try:
            # print(query)
            execute_query(connection, query)
            print("Query executed successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == 4:
        print("+---------------------------+")
        print("Menu - Tables for Deletion")
        print("+---------------------------+")
        print("1. Influential Personalities")
        print("2. Casualities")
        print("+---------------------------+")
        t_choice = eval(input("Enter your choice: "))

        query = deletion(t_choice)
        try:
            print(query)
            execute_query(connection, query)
            print("Query executed successfully")
        except Exception as e:
            print(f"An error occurred: {e}")


    elif choice == 5:
        break
    else:
        print("Invalid choice. Please enter a Valid Choice")
    dchoice = input("Please Press Enter to Continue !! ")
    

connection.close()

