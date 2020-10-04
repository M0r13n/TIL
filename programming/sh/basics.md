# Basics about SH scripts and how to use them efficiently

**Table of Contents**

* [Basics](#basics)
  + [Variables](#variables)

## Basics

### Variables

* Basics:
    - Shell variables should be **UPPERCASE** by convention 
    - Definition: `variable_name=variable_value` -> `NAME="lmrichter"`
    - Access: The value of a variable is accessed by prefixing it with a **$**-sign: `echo $NAME`
    - Unset: `Unset NAME`
    - Variables can be marked readonly **AFTER** they were defined -> `NAME="lmrichter"; readonly NAME`
    - To use a variable in a continous string wrap it in curly braces -> `NAME="leon"; echo "$NAME_FILE"; echo "${NAME}_FILE"`

* Local Variables:
    - Prefix variable definition with *local* -> `local name="lmrichter"`
    - *Local* ensures that the variable has meaning only within that function block
    - **GOTCHA**: Before a function is called, **ALL** variables declared within the function are invisible outside the body of the function. But after it was called they still exist.

* Special Variables:
    - **$0**    : Filename of current script
    - **$n**    : Access the **n**-th argument that was passed
    - **$#**    : Number of supplied arguments
    - **$\***   : All arguments as a single string
    - **$@**    : All arguments as an array
    - **$?**    : Exit Status of last executed command
    - **$$**    : PID of current shell
    - **$!**    : PID of last background command

* Declare:
    - Normal assignment using declare is the same as not using it -> `foo="12"` == `declare foo="bar"`
    - Asign var by name -> `declare -n foo=bar` != `foo=bar`
    - Export -> `declare -x foo` == `export foo`
    - Integer: `declare -i`
    - Conversions: 
        - Convert to lowercase : `declare -l lowers="UPPER"`
        - Convert to uppercase : `declare -u upper="lower"`
    - Readonly:  -> `declare -r do_not_change_me="23123123"`

* Usage:
    - Get the value of a variable: `$VARIABLE_NAME`
    - Raise an error if a variable is not set `${VARIABLE_NAME?}`
    - Evaluate a expression `$(pwd)`
