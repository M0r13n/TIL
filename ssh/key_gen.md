# Quick way to setup SSH via keyfile

On the remote host:

```sh
ssh-keygen -t rsa -b 2048
```

The key location is `/root/.ssh/id_rsa`.

Public key can be found in `/root/.ssh/id_rsa.pub`.
Private key can be found in `/root/.ssh/id_rsa`.

**NOTE**: Permission of private key should be `0600`.

On local host:

```sh
ssh-copy-id USER@HOST-IP
```

**Note**: You might need to execute : `install openssh-clients`.


## Restrict password-based login:
Edit sshd_config file:
```
sudo nano /etc/ssh/sshd_config
```

and add `PermitRootLogin without-password`.

Finally execute: `service sshd reload`.