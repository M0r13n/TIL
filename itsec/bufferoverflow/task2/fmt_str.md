# Der Format String Angriff macht sich keinen Speicherüberlauf im klassischen Sinne zu Nutze. Wie funktioniert ein derartiger Angriff grundsätzlich?

Um den Angriff zu verstehen, gilt es die Funktion printf und co und die String Formatierung in C zu verstehen.  
Ein **Format String** definiert die Art und Weise, wie ein gegebener Input konvertiert wird.  
In der Regel soll die geschehen, damit Variablen in menschen-lesbare Werte übersetzt werden können.
Probleme entstehen wie fehlender oder mangelnder Inputvalidation.  

In C gibt eine eine Reihe von String Formatting Functions. Namentlich:
	- fprint
	- printf
	- sprintf
	- usw.

Allen Funktionen gemein ist, ihre generelle Funktion. Sie erwarten einen Formatierung String und *n* Variablen, die es zu konvertieren gilt. 
Beispiel : `printf(fmt, args(...))`.

Es gibt folgende Fmt's:
- %% : % character (literal) -> by reference
- %p : External representation of a pointer to void -> by reference
- %d : Decimal -> by value
- %c : Character -> by value
- %u : Unsigned decimal -> by value
- %x : Hexadecimal -> by value
- %s : String -> by reference
- %n : Writes the number of characters into a pointer -> by reference

# Solution
- %x %x %x %x %x %n
