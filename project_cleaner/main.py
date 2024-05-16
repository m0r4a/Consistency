import os
import re
import random


class Project:
    def __init__(self, name, description, difficulty, status):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.status = status


def main():
    projects = open_readme()

    # Creating a dictionary to store the projects
    projects_dict = {}

    # Processing each project in the README file
    for project_info in projects:
        project = parse_project(project_info)
        if project:
            projects_dict[project.name] = project

    # Showing the mini menu
    while True:
        print("--------- Menu ---------")
        print("1. Show all projects")
        print("2. Show a random project")
        print("Any other key to exit")

        choice = input("Choose an option:")

        if choice == "1":
            clear_terminal()
            show_all_projects(projects_dict)
        elif choice == "2":
            clear_terminal()
            show_random_project(projects_dict)
            break
        else:
            print("¡See ya!")
            break


def show_all_projects(projects_dict):
    clear_terminal()
    print("---------- Projects ----------")
    for index, project_name in enumerate(projects_dict.keys(), 1):
        print(f"{index}. {project_name}")

    project_index = input(
        "Enter the number of the project you want to see more information about:")

    if project_index.isdigit():
        project_index = int(project_index)
        project_names = list(projects_dict.keys())
        if 1 <= project_index <= len(project_names):
            project_name = project_names[project_index - 1]
            project = projects_dict[project_name]
            clear_terminal()
            print_project_info(project)
            exit(0)
    else:
        print("Invalid input. Please enter a number.")
        exit(1)


def show_random_project(projects_dict):
    clear_terminal()
    random_project = random.choice(list(projects_dict.values()))
    print("---------- Random Project ----------:")
    print_project_info(random_project)


def print_project_info(project):
    print("Name:", project.name)
    print("Description:", project.description)
    print("Difficulty:", project.difficulty)
    print("Status:", project.status)


def parse_project(project_info):
    # Cleaning the project info
    pattern = r"\|\s*\[(.*?)\]\((.*?)\)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|"
    match = re.match(pattern, project_info)

    if match:
        name = match.group(1)
        description = match.group(3)
        difficulty = match.group(4)
        status = match.group(5)

        # Creating a project object
        return Project(name, description, difficulty, status)
    else:
        return None


def open_readme():
    with open('../README.md', 'r') as file:
        return file.readlines()


def clear_terminal():
    # Cleaning the terminal
    if os.name == 'posix':  # Linux & macOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')


main()
