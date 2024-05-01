import sqlite3
import json
from models import Location
from models import Employee
from models import Animal

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike",
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive",
    }
]

def get_all_locations():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)
        locations = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    return locations
  
def get_single_location(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, (id,))
        location_data = db_cursor.fetchone()
        if location_data is None:
            return None  # Location with the given ID not found

        location = Location(location_data['id'], location_data['name'], location_data['address'])

        db_cursor.execute("""
        SELECT
            e.id employee_id,
            e.name employee_name,
            e.address employee_address
        FROM Employee e
        WHERE e.location_id = ?
        """, (id,))
        employees_data = db_cursor.fetchall()
        employees = [Employee(emp_data['employee_id'], emp_data['employee_name'], emp_data['employee_address']) for emp_data in employees_data]

        db_cursor.execute("""
        SELECT
            a.id animal_id,
            a.name animal_name,
            a.breed animal_breed,
            a.status animal_status
        FROM Animal a
        WHERE a.location_id = ?
        """, (id,))
        animals_data = db_cursor.fetchall()
        animals = [Animal(animal_data['animal_id'], animal_data['animal_name'], animal_data['animal_breed'], animal_data['animal_status']) for animal_data in animals_data]

        location_details = {
            'id': location.id,
            'name': location.name,
            'address': location.address,
            'employees': [emp.__dict__ for emp in employees],
            'animals': [animal.__dict__ for animal in animals]
        }

        return location_details

def create_location(location):
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))

        
def update_location(id, new_location):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Location
            SET
                name = ?,
                address = ?
        WHERE id = ?
        """, (new_location['name'], new_location['address'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
