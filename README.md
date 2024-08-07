AirBnB Clone Project

Welcome to the AirBnB clone project! This project is the first step towards building a full web application that mimics the functionalities of AirBnB. The primary goal of this step is to create a command interpreter to manage your AirBnB objects.

Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Testing](#testing)
- [Authors](#authors)

 Description

This project involves developing a command-line interface (CLI) to manage various AirBnB objects, such as users, places, and states. The command interpreter allows for creating, retrieving, updating, and deleting objects, as well as performing other operations on them.

 Features

- Create, read, update, and delete objects
- Command interpreter with interactive and non-interactive modes
- Serialization and deserialization of objects to/from JSON files
- Unit tests for all components

 Installation

Prerequisites

- Python 3.8.5
- Git

 Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/AirBnB_clone.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone
   ```
3. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install required packages (if any):
   ```bash
   pip install -r requirements.txt
   ```

Usage

Interactive Mode

To start the command interpreter in interactive mode, run:
```bash
./console.py
```

This will open a prompt `(hbnb)` where you can enter commands.

Example:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
```

Non-Interactive Mode

You can also use the command interpreter in non-interactive mode by piping commands:

```bash
echo "help" | ./console.py
```

Example:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

 Commands

The command interpreter supports the following commands:

- `create <class>`: Creates a new instance of the specified class
- `show <class> <id>`: Shows the details of an instance by class and ID
- `destroy <class> <id>`: Deletes an instance by class and ID
- `all [<class>]`: Shows all instances, or all instances of a specific class
- `update <class> <id> <attribute> <value>`: Updates an instance's attribute
- `quit`: Exits the command interpreter
- `EOF`: Exits the command interpreter

Testing

Unit tests are provided to ensure the correctness of the program. To run the tests, use:

```bash
python3 -m unittest discover tests
```

 Authors

-Chancy Tsonga 


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
