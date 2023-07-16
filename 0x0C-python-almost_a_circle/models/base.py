#!/usr/bin/python3
"""This is the class Base"""


import json
import csv
from turtle import Turtle, Screen


class Base:
    """This is atrributes of class base
    Atrributes:
        __nb_objects: __nb_objects
        id: id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ the constructor of the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """this method returns JSON strings"""
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    """this method saves json string to file"""
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(json_string)

    """this method returns lists of dictionary"""
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    """this method creates any instance of class"""
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        elif cls.__name__ == "Square":
            dummy = cls(3)
        else:
            dumpy = cls()

        dummy.update(**dictionary)
        return dummy

    """this method loads json from file"""
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                instance = [cls.create(**d) for d in dict_list]

                return instance
        except FileNotFoundError:
            return []

    """this method writes to csv file"""
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)

            if list_objs is not None and len(list_objs) > 0:
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.width,
                                         obj.height, obj.x, obj.y])

                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    """This method loads from file"""
    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        objs = []

        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)

                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]),
                                       int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[2]),
                                       int(row[3]), int(row[0]))
                    objs.append(instance)
        except FileNotFoundError:
            return objs
        return objs

    """This method draw rectangle and square"""
    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = Screen()
        turtle = Turtle()
        turtle.speed(2)

        colors = ["red", "green", "blue", "orange",
                  "purple", "yellow", "black"]
        color_index = 0

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()

            turtle.fillcolor(colors[color_index % len(colors)])
            turtle.begin_fill()

            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.right(90)

            turtle.end_fill()
            color_index += 1

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()

            turtle.fillcolor(colors[color_index % len(colors)])
            turtle.begin_fill()

            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)

            turtle.end_fill()
            color_index += 1

        list_spirals = [
                {"length": 10, "angle": 90, "x": -100, "y": 0},
                {"length": 20, "angle": 65,  "x": -100, "y": 320},
                {"length": 80, "angle": 40,  "x": 0, "y": -300},
                {"length": 100, "angle": 70, "x": 10, "y": 300},
                ]

        for spiral in list_spirals:
            turtle.penup()
            turtle.goto(spiral["x"], spiral["y"])
            turtle.pendown()

            angle = spiral["angle"]
            length = spiral["length"]

            for _ in range(20):
                turtle.forward(length)
                turtle.right(angle)
                length += 5

        screen.exitonclick()
