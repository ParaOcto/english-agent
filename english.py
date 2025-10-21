#!/usr/bin/env python3
"""
English Vocabulary Generator
A script for generating vocabularies every day at 8:00 a.m
"""

import random
from datetime import datetime


# Vocabulary database with words, definitions, and example sentences
VOCABULARY = [
    {
        "word": "ephemeral",
        "definition": "lasting for a very short time",
        "example": "The beauty of cherry blossoms is ephemeral, lasting only a few days.",
        "part_of_speech": "adjective"
    },
    {
        "word": "ubiquitous",
        "definition": "present, appearing, or found everywhere",
        "example": "Smartphones have become ubiquitous in modern society.",
        "part_of_speech": "adjective"
    },
    {
        "word": "serendipity",
        "definition": "the occurrence of events by chance in a happy or beneficial way",
        "example": "Finding that book was pure serendipity; it was exactly what I needed.",
        "part_of_speech": "noun"
    },
    {
        "word": "ameliorate",
        "definition": "make something bad or unsatisfactory better",
        "example": "The new policy helped ameliorate the working conditions.",
        "part_of_speech": "verb"
    },
    {
        "word": "perspicacious",
        "definition": "having a ready insight into and understanding of things",
        "example": "Her perspicacious observations helped solve the problem quickly.",
        "part_of_speech": "adjective"
    },
    {
        "word": "eloquent",
        "definition": "fluent or persuasive in speaking or writing",
        "example": "The speaker delivered an eloquent speech that moved the audience.",
        "part_of_speech": "adjective"
    },
    {
        "word": "pragmatic",
        "definition": "dealing with things sensibly and realistically",
        "example": "We need a pragmatic approach to solving this issue.",
        "part_of_speech": "adjective"
    },
    {
        "word": "meticulous",
        "definition": "showing great attention to detail; very careful and precise",
        "example": "The architect was meticulous in every aspect of the design.",
        "part_of_speech": "adjective"
    },
    {
        "word": "verbose",
        "definition": "using or expressed in more words than are needed",
        "example": "His verbose explanation could have been much more concise.",
        "part_of_speech": "adjective"
    },
    {
        "word": "resilient",
        "definition": "able to withstand or recover quickly from difficult conditions",
        "example": "Despite the setbacks, the team remained resilient and determined.",
        "part_of_speech": "adjective"
    }
]


def generate_vocabulary():
    """Generate a random vocabulary word for today."""
    # Select a random word from the vocabulary list
    vocab = random.choice(VOCABULARY)
    
    # Get current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    # Display the vocabulary
    print("=" * 60)
    print(f"📚 Daily Vocabulary - {date_str} at {time_str}")
    print("=" * 60)
    print()
    print(f"Word: {vocab['word'].upper()}")
    print(f"Part of Speech: {vocab['part_of_speech']}")
    print()
    print(f"Definition:")
    print(f"  {vocab['definition']}")
    print()
    print(f"Example:")
    print(f"  {vocab['example']}")
    print()
    print("=" * 60)


def main():
    """Main entry point of the script."""
    generate_vocabulary()


if __name__ == "__main__":
    main()
