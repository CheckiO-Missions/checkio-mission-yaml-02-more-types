"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["""name: Alex
age: 12"""],
            "answer": { 
              "name": "Alex",
              "age": 12
            }
        },
        {
            "input": ["""name: Alex Fox
age: 12

class: 12b"""],
            "answer": {
                "name": "Alex Fox",
                "age": 12,
                "class": "12b"
            }
        },
        {
            "input": ["""name: "Alex Fox"
age: 12

class: 12b"""],
            "answer": {
                "name": "Alex Fox",
                "age": 12,
                "class": "12b"
            }
        },
        {
            "input": ["""name: "Alex \\"Fox\\""
age: 12

class: 12b"""],
            "answer": {
                "name": "Alex \"Fox\"",
                "age": 12,
                "class": "12b"
            }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
alive: false"""],
          "answer": {
              "name": "Bob Dylan",
              "children": 6, 
            "alive": False
          }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
coding:"""],
          "answer": {
              "name": "Bob Dylan", 
              "children": 6,
              "coding": None
          }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
coding: null"""],
          "answer": {
              "name": "Bob Dylan", 
              "children": 6,
              "coding": None,
          }
        },
        {
          "input": ["""name: "Bob Dylan"
children: 6
coding: "null" """],
          "answer": {
              "name": "Bob Dylan", 
              "children": 6,
              "coding": "null"
          }
        }
    ],
    "Extra": [
        {
            "input": ["""
name: Alex
age: 12"""],
            "answer": { 
              "name": "Alex",
              "age": 12
            },
            "explanation": "Extra space at the beginning"
        },
        {
            "input": ["""12: 12"""],
            "answer": {"12": 12},
            "explanation": 'Key can be int'
        },
        {
            "input": ["""name: Bob Dylan
born: 24 May 1941
resident: Malibu, California, U.S

children: 6"""],
            "answer": {
                "name": "Bob Dylan",
                "born": "24 May 1941", 
                "resident": "Malibu, California, U.S", 
                "children": 6
            }
        }
    ]
}
