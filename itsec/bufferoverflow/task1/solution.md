# Task 1
- see assm.md for assembler output and comments
- see my_interpretation for pseudo c code 


# Formulieren Sie eine Vermutung, wie das Programm funktioniert und was man tun müsste, um den getätigten Angriff unmöglich zu machen.
Vorgehen:  
-  Dissembling mit GDB  
- Für den Assembler code siehe assm.md  
- Wir sehen, die folgenden Funktionen: häufig printf, strlen, strcmp und strcpy  
- Da viel printf, gucken wir ob wir Strings hardgecoded finden. Tuen wir auch und zwar:  
	- password   
	- Your password is not valid.  
	- Hello %s. Your password is correct.  
	- Usage: %s <password> <name>  
- schauen wir uns den assembler code genauer an und nehmen ggf. Ghidra zur Hilfe, können wir ungefähr den code wie in my_interpretation.c zu sehen rekonstruieren  
- die Variablen wurden von mir benannt, damit der Flow leichter nachzuverfolgen ist  

Funktion des Programms:  
Zu Beginn wird ein Buffer mit 20 Bytes erzeugt.  
Das Programm verlangt nach genau zwei Kommandlineargumenten und verweigert bei einer Abweichung davon den Dienst und gibt den Statuscode 1 zurück.  
Danach vergleicht es die Länge des Nutzerinput mit 8. Ist der Input von der Länge 8 (call of strlen), vergleicht es den Text mit dem Text password (strcmp). Die Schwachstelle ist ` strcpy(buffer,(char *)argv[2]);`. Strcpy kopiert ohne Längencheck und hier kann ein Bufferoverflow entstehen.  

# Welche einfachen Maßnahmen können C-Programmierende ergreifen, um solche Attacken unmöglich zu machen oder zumindest erheblich zu erschweren? Nennen Sie mindestens zwei.
- Input validation
- die sichere variante von strcpy
- aslr

# Wie kann man Programme auf derartige Sicherheitslücken testen? Gibt es automatisierte Verfahren, die die Existenz einer solchen Sicherheitslücke mit hoher Wahrscheinlickeit aufzeigen?

- gibts bestimmt, keine lust zu suchen gerade

# Wie wird in Linux Sorge dafür getragen, dass beispielsweise ein erfolgreicher Angriff, der sich einen Buffer Overflow zu Nutze macht, nicht auf den gesamten Arbeitsspeicher zugreifen kann?

Virtual address space

