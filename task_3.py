"""
Micro library that allows users to work with notes about films
"""

import sys
import csv

class Micro_library:
    """
    Class for working with the library
    Needs for 1 input parameter: adress of the file with the library
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.films = []
        self.film_names = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.films.append(
                    {
                        "film_name": row["film_name"],
                        "note": row["note"],
                        "rating": float(row["rating"])
                    }
                )
                self.film_names.append(row["film_name"])
         

    def add_note(self, film_name: str, note: str, rating: float):
        """
        Method for adding note to the library
        """
        if film_name in self.film_names:
            sys.exit("Film is already in the library")
        elif not isinstance(rating, float):
             sys.exit("Not valid rating. It should be a number")
        elif rating < 1 or rating > 5:
            sys.exit("Not valid rating. It should be from 1 to 5")
        else:
            self.films.append(
                    {
                        "film_name": film_name,
                        "note": note,
                        "rating": rating
                    }
                )
            self.film_names.append(film_name)
            with open(self.filename, "a") as file:
                writer = csv.DictWriter(file, fieldnames = ("film_name", "note", "rating"))
                writer.writerow(self.films[-1])

    def remove_note(self, film_name: str):
        """
        Method for removing note from the library
        """
        try:
            index = self.film_names.index(film_name)
        except ValueError:
            sys.exit("There is no such film in the library")
        else:
            del self.film_names[index]
            del self.films[index]
            with open(self.filename, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames = ("film_name", "note", "rating"))
                writer.writeheader()
                writer.writerows(self.films)


    def print_notes(self):
        """
        Method for printing notes in console
        """
        for film in self.films:
            print("Film name: ", film["film_name"])
            print("Note: ", film["note"])
            print("Rating: ", film["rating"])
            print()

    def get_highest(self, n: int = 3):
        """
        Method for printing n of top films with the highest rating.
        Default number of films: 3
        """
        if not isinstance(n, int):
            sys.exit("Not valid number of films")
        else:
            r = sorted(self.films, key = lambda x: x["rating"], reverse = True)
            print(f"Top {n} films with the highest rating:")
            for i in range(n):
                print(i+1, r[i]["film_name"], r[i]["rating"], sep=" ")

    
    def get_lowest(self, n: int = 3):
        """
        Method for printing n of top films with the lowest rating.
        Default number of films: 3
        """
        if not isinstance(n, int):
            sys.exit("Not valid number of films")
        else:
            r = sorted(self.films, key = lambda x: x["rating"])
            print(f"Top {n} films with the lowest rating:")
            for i in range(n):
                print(i+1, r[i]["film_name"], r[i]["rating"], sep=" ")

    
    def get_average_rating(self):
        """
        Method for getting average rating of all films
        """
        rate_mean = sum([film["rating"] for film in self.films]) / len(self.films)
        print(f"Average rating is {rate_mean:.2f}")
