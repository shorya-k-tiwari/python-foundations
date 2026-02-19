"""
Contact Book CLI
Simple command-line contact manager using functions and dictionary storage
"""

contacts = {}


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()