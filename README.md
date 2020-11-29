|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | 
|  H  |  A  |  S  |  H  |  -  |  F  |  U  |  N  |  C  |  T  |  I  |  O  |  N  |  S  | 

## About

Hash Functions is an application developed for an assignment of a Discrete Mathematics class. It  implements the basic functioning of a hash function.

## Technologies

* Python

## Requirements

To run and edit the project, be sure to have installed in your computer the following softwares:

- [Python](https://www.python.org/downloads/)
- A code editor

After that, you'll need to clone this repo:

```
git clone https://github.com/LBeghini/Hash-Functions.git
```

## Setup

Inside the project directory, [create a virtual environment](https://docs.python.org/3/library/venv.html) (venv)

At the ```cmd```, type:

```
python -m venv ./venv
```

After that you should see a venv directory.

To run commands using venv, go to ```Scripts``` directory inside ```venv```:
```
project
│   main.py
│   ...
└─── venv
     └─── Scripts
         │   activate
```
To use the virtual environment, run:

```
activate
```
Then, using the virtual environment, install the project requirements:

```
pip install -r requirements.txt
```

That will prevent you to install the libs in the local computer, and it will be available only on the project scope.

## Editing

Whenever you install a new library, you need to update the ```requirements.txt``` file.

At the ```cmd```, run:
```
pip freeze > requirements.txt
```
## Running

### venv:
To see the project running, inside the virtual environment at ```cmd```, run:
```
python main.py
```
### Release:
This project provides a [release](https://github.com/LBeghini/Hash-Functions/releases) where you cand download the ```dist.rar```, that includes a file ```main.exe```.

## Usage

When the program starts, you need to set the size of the hash table, that is an integer greather than 2.

After that, the program will show you the layout of the hash table, and the commands that you'll need to use the program:
```
COMMANDS:
-i, --insert                      insert a key
-d, --delete                      delete a key
-s, --search                      search a key and returns it's index
-h, --hash                        returns the hash rule
exit                              exit the program
```

## Example

Creating a table with 12 positions:
```
Table size: 12

╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╤══════╤══════╕
│ 0   │ 1   │ 2   │ 3   │ 4   │ 5   │ 6   │ 7   │ 8   │ 9   │ 10   │ 11   │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪══════╪══════╡
│     │     │     │     │     │     │     │     │     │     │      │      │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╧══════╧══════╛
```
Inserting a key 12 into the table:
```
OPERATION: -i 12
╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╤══════╤══════╕
│ 0   │ 1   │ 2   │ 3   │ 4   │ 5   │ 6   │ 7   │ 8   │ 9   │ 10   │ 11   │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╪══════╪══════╡
│ 12  │     │     │     │     │     │     │     │     │     │      │      │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╧══════╧══════╛
```
## More
For further information visit the [Wiki](https://github.com/LBeghini/Hash-Functions/wiki).
