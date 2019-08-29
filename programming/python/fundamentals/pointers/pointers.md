# Pointers

- Each object consists of at least three things:
	1. **Reference Count** 
	2. **Type** 
	3. **Value**

- `id(x)` returns the memory address of an object
- all primitive data types are immutable
- Python does not really use variables instead it uses names

## Recall: Variables in C

```C
// allocate 4 bytes for an integer
// assign the number 3 to that memory location
// let x point to that location 
int x = 3;

// memory location stays the same, BUT the value changes -> x is mutable
x = 4;
```

- in C the variable **owns it's memory location**

## Object Creation in Python

- `x = 5`
- create a PyObject
- set type of that obj to int
- set the value to 5
- create a **name** called x and let x **point** to the newly created PyObject
- increase the reference count (number of how many names **point** to that object)
- NOTE: **PyObject** is C struct and therefore not accessible in Python

## Difference C and Python
- in both languages the variable x **points** to something
- in C the x owns it's memory space and directly points to the memory location
- in Python x points to a **PyObject** which in turn owns that space
- So the PyObject behaves somewhat like a middleman
- `x=5` in Python can therefore rather be seen as **binding x to a reference** than as a **assignment**

## Interning
- for performance reasons Python interns a small set of objects, like numbers from -5 to 256 or strings once I use them
