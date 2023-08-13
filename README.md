
**_sTudoo is a webapp written in python which helps students to organize their class related projects, keep the overview and stay on track with deadlines._**

# Installation

To deploy the sTudoo application please make sure to follow the steps below.

## 1. Get a Server

To run sTudoo in production, a server is needed. So make sure that you have a functional server up and running. The provided command should work on the most linux based serveres. Please make sure that the package manager used in the following commands is **apt**. If the distribution you're using is using a different package manager (i.e. Fedora -> dnf) ensure that you adapt the commands for your case.

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

## 4. Installing Base Dependencies

To create a production-ready deployment make sure that the server and it's packages are up to date.

```
$ sudo apt-get -y update
```

Install **Python** and the python related packages.

```
$ sudo apt-get -y install python3 python3-venv python3-dev
```

In the follwing stepp we will install the MySQL server, supervisor (a tool that monitors Flask's server process), the Ngnix server (accepts requests and forwards them to the app) and Git to download the app from Github. During the MySQL installation a root password has to be set.

```
$ sudo apt-get -y install mysql-server supervisor ngnix git
```

## 5. Install the sTudoo app

Navigate into the home directory.

```
$ cd /home/
```

Download the app with git clone. 

```
$ git clone https://github.com/andrej-moor/studoo
```

Change into the the directory.

```
$ cd studoo
```

Create the virtual invironment.

```
$ python3 -m venv venv
```
Activate the virtual environment.

```
$ source venv/bin/activate
```
Install the package dependencies from `requirements.txt` via pip.

```
(venv) $ pip install -r requirements.txt
```

Install Gunicorn which is a production webserve for pyhton apps.

```
(venv) $ pip install gunicorn
```

Generate your own secret key string and copy it to the clipboard.

```
python -c "import uuid; print(uuid.uuid4().hex)"

12dfb585fb2a4b1da206f06cf09f0956
```

Create an `.env` file for environment viables. And open it with the texteditor nano.

```
(venv) $ touch .env
(venv) $ nano .env
```

First, enter the generated key string into the file. Afterwords enter the database url. Choose a password and enter it isnstead on `<db-password>`. Save the password, we will use it later in the MySQL settings.

```
SECRET_KEY=12dfb585fb2a4b1da206f06cf09f0956

DATABASE_URL=mysql+pymysql://studoo:<db-password>@localhost:3306/studoo
```
Save the file with `str+o` and close it with `str+q`.

Set the FLASK_APP environment variable to the entry point of the app, adding it to the `.profile` file of the user account. It will be set atomatically everytime one logs in.

```
$ echo "export FLASK_APP=studoo.py" >> ~/.profile
```

## 6. Set up MySQL

To manage multiple request at a time in production a MySQL databse will be implement.

Login in into MySQL as a root user.

```
$ sudo mysql -u root 
```

Create a database called `studoo` and a user with the same name with full acces. Enter your the password from the `.env` file you've chosen insteat of `<db-password>`.

```
mysql> create database studoo caracter set utf8 collate utf8_bin;
mysql> create user 'studoo'@'localhoast' identified by '<db-password>';
mysql> create database studoo caracter set utf8 collate utf8_bin;
mysql> flush privileges;
mysql> quit;
```

Run the database migrations that create all the tables.

```
(venv) $ flask db upgrade
```

## 7. Set up Gunicorn & Supervisor

Create a config file for the installed `Supervisor` package which will be reponsible for managing the `Unicorn` application webserver's processes.

```
$ touch /etc/supervisor/conf.d/studoo.conf
```

Add the following settings to it, by opening it with the nano editor.

```
$ nano /etc/supervisor/conf.d/studoo.conf

```
```
[program:studoo]
command=/home/studoo/studoo/venv/bin/gunicorn -b localhost:8000 -w 4 studoo:app
directoray=/home/studoo/studoo
user=studoo
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```

Reload the suvervisor service.

```
$ sudo supervisorctl reload
```
## Set Up Ngnix

To handle external web traffic let us set up the public facing Ngnix server.

First we will create a self-signed SSL certificate. After creating a directory in the root directory of the app.

Enter all the asked information, because they will be included in the SSL certificate.

```
$ mkdir certs
$ openssl req -new -newkey rsa:4096 -day 365 - nodes -x509 \
  - keyout certs/key.pem -out certs/cert.pem
```
**!! Make sure that you nee a "real" certificat by a trusted autority, otherwise users will receive warnings from the browser, that the certificate can't be trusted!! 

Include the appropriate files (key.pem & cert.pm) in the directories mentioned in the Ngnix config file when  have your dmain set up.


Next, delete the preinstalled test side created as a default by Ngnix

```
$ sudo rm /etc/ngnix/sites-enabled/default
```

Create a new config file,

```
$ touch /etc/ngnix/sites-enabled/studoo
```

and add the following content to it.

```
$ nano /etc/ngnix/sites-enabled/studoo
```

```
server {
  # listen on port 80 (http)
  listen 80;
  server_name_;
  location / {
    # redirect any rerequest to the same URL but on https
    return 301 https://$host$request_uri:
  }
}

server {
  # listen on port 443 (https)
  lsiten 433 ssl;
  server_name_;

  #location of the self-signed SSL certificate 
  ssl_certificate /home/studoo/studoo/certs/cert.pem;
  ssl_certificate_key /home/studoo/studoo/certs/key.pem;

  # write acces and error logs to /var/log
  acces_log /var/log/studoo_access.log;
  error_log /var/log/microblog:error.log;

  location / {
    #forward allplication request to the gunicorn server
    proxy_pass http://localhost:800;
    proxy:redirect off;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
  }

  location /static {
    # handle static files directly, without forwarding to the application
    alias /home/studoo/studoo/app/static;
    expired 30d;
  }
}
```

Now, we have to reload the config and activate it.

```
$ sudo service ngnix reload
```


