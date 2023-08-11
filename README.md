
**_sTudoo is a webapp written in python which helps students to organize their class related projects, keep the overview and stay on track with deadlines._**

# Installation

To deploy the sTudoo application please make sure to follow the steps below.

## 1. Get a Server

To run sTudoo in production, a server is needed. So make sure that you have a functional server up and running.

Possible solutions for installing a server are provided by [Linode]
(https://www.linode.com/), [Digital Ocean](https://www.digitalocean.com/) or [Amazon Lightsail](https://aws.amazon.com/lightsail/).

Please follow the Documentation of the provider to install the virtual server and make sure you have the **IP** and the **root password** of your server.

## 2. SSH into the server

Open your terminal of choice and ssh into the server.

```
$ ssh root@<ip-of-your-server>
```

Type in your password after the prompt.

## 3. Create an account for deployment work

Create a new user.

```
$ adduser --gecos "" your_user_name
```

Give the user sudo permissions.

```
$ usermod -aG sudo your_user_name
```

Login as the user you've created

```
$ su your_user_name
```

### 3.1. Creating a public key

To log in without typing a password we will use a **public key authentication**. To do so, we will use a second terminal on your own machine. Leave the first (server) terminal session open though.

`ls` into the ~/.shh directory.

```
$ ls ~/.ssh

id_rsa id_rsa.pub
```

If `id_rsa` & `id_rsa.pub` are listed like above, you already have a key.

If the directory itself or the files are missing run the following command to create a SSH keypair.

```
$ ssh-keygen
```

Accept the following prompts by pressing `enter`. After the command has run the mentioned files should have been created. The `id_rsa.pub` files is the **public key** (which is provided to third parties to get identified). The `id_rsa` is the **private key** and shouldn't be shared with anyone.

### 3.2. Configuring the public key as an authorized host

In the next step we're going to configuire the public key as an authorized host in the server.

Print the public key on your machines terminal (not the server).

```
$ cat ~/.ssh/id_rsa.pub

ssh-rsa Alaksjdkfjjoi2..............3870asjd20ß23r8zz8ß1´="=
```
The output of the command should be a long cryptic string of characters as shown under the command above.

Copy the string to your clipboard, switch to the terminal of ther remote server and import the key with the following command.

```
$ echo <copy-your-key-here> >> ~/.ssh/authorized_keys

$ chmod 600 ~/.ssh/authorized_keys
```
The passwordless loging should now be working every time your log in with ssh.

## 4. Insalling Base Dependencies




