import sqlite3
import questionary

    # Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('people.db')
c = conn.cursor()

    # Create table
c.execute('''CREATE TABLE IF NOT EXISTS persons
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
conn.commit()

def add_person():
        # This is the "form" - uses arrow keys, validation, etc.
        name = questionary.text("What is the person's name?").ask()
        email = questionary.text("What is the person's email?").ask()
        
        # Insert a row of data
        c.execute("INSERT INTO persons (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"✅ {name} added successfully!")

def main_menu():
        while True:
            # Main menu for the app
            choice = questionary.select(
                "What do you want to do?",
                choices=[
                    "Add a person",
                    "View all people",
                    "Exit"
                ]).ask()
            
            if choice == "Add a person":
                add_person()
            elif choice == "View all people":
                # Fetch and display data
                c.execute("SELECT * FROM persons")
                for row in c.fetchall():
                    print(row)
            elif choice == "Exit":
                conn.close()
                break

if __name__ == "__main__":
        main_menu()