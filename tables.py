progressions = [
    ["I", "IV", "vi", "V"],
    ["I", "V"],
    ["I", "V", "IV"]
]

romReference = {
    "i": 0,
    "I": 0,
    "ii": 2,
    "II": 2,
    "iii": 4,
    "III": 4,
    "iv": 5,
    "IV": 5,
    "v": 7,
    "V": 7,
    "vi": 9,
    "VI": 9,
    "vii": 11,
    "VII": 11,

}

intervals = {
    "3": {
        "min": (3, 4),
        "maj": (4, 3),
        "dim": (3, 3),
        "aug": (4, 4)
    },
    "7": {
        "min": (3, 4, 3),
        "maj": (4, 3, 4),
        "dom": (4, 3, 3),
        "dim": (3, 3, 3),
        "aug": (4, 4, 4)
    },
    "shorthand": {
        "maj": ("1", "3", "5"),
        "min": ("1", "b3", "5"),
        "dim": ("1", "b3", "b5"),
        "aug": ("1", "3", "#5"),
        "maj7": ("1", "3", "5", "7"),
        "min7": ("1", "b3", "5", "b7"),
        "7": ("1", "3", "5", "b7"),
        "dim7": ("1", "b3", "b5", "bb7"),
        "hdim7": ("1", "b3", "b5", "b7"),
        "minmaj7": ("1", "b3", "5", "7"),

        "maj6": ("1", "3", "5", "6"),
        "min6": ("1", "b3", "5", "6"),

        "9": ("1", "3", "5", "b7", "9"),
        "maj9": ("1", "3", "5", "7", "9"),
        "min9": ("1", "b3", "5", "b7", "9"),

        "sus2": ("1", "2", "5"),
        "sus4": ("1", "4", "5")
    },
    "intervalToStep": {
        "1": 0,
        "2": 2,
        "b3": 3,
        "3": 4,
        "4": 5,
        "b5": 6,
        "5": 7,
        "#5": 8,
        "6": 9,
        "bb7": 9,
        "b7": 10,
        "7": 11,
        "8": 12,
        "9": 14,

    }

}

notes = {
    "noteToStep": {
        "C": 0,
        "Db": 1,
        "D": 2,
        "Eb": 3,
        "E": 4,
        "F": 5,
        "Gb": 6,
        "G": 7,
        "Ab": 8,
        "A": 9,
        "Bb": 10,
        "B": 11,
        "C#": 1,
        "D#": 3,
        "F#": 6,
        "G#": 8,
        "A#": 10
    },
    "flat": [
        "C",
        "Db",
        "D",
        "Eb",
        "E",
        "F",
        "Gb",
        "G",
        "Ab",
        "A",
        "Bb",
        "B"
    ],
    "sharp": [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B"
    ]
}

regexes = {
    "root": "((IV|V?I{0,3})|(iv|v?i{0,3}))",
    "quality": "(majmin|maj|min|dom|dim|aug)",
    "size": "",
    "whole": "[VvIi]{1,3}([a-z]{3}|.{0})\d{0,2}"
}