# Environment Variables
Each process has its **own, separate** set of env vars and inherits a **duplicate** of the environment of it's **parent process** (unless explicit changes are made). Those changes need to be done **between** running `fork` and `exec`. In Unix shells, variables assigned **without** the export keyword are **not** true environment variables, as they are **not recognized by the kernel**. Those are displayed by the `set` command, but not by the `printenv`.

## Some commands
- **view env**: `printenv` or `env`
- **change vars** : `env VAR="BLA_BLI_BLUB"` or `export VAR="..."` or `setenv VAR value`
- export : variables are inherited by commands
- env or direct assignment: variables will **NOT** be inherited