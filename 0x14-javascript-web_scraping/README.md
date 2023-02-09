# 0x14. JavaScript - Web scraping

## Resources

**Read or watch**:

- [Working with JSON data](https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A "Working with JSON data")
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA "The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco")
- [request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ "request module")
- [Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g "Modern JS")

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard](https://intranet.alxswe.com/rltoken/W9rASrTqkF-xXjcwomrMLw "Rules of Standard") + [semicolons on top](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg "semicolons on top"). Also as reference: [AirBnB style](https://intranet.alxswe.com/rltoken/NZR55f9vk1dZXj5q7UI5mQ "AirBnB style")
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

## More Info

### Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs 
```

### Install semi-standard

[Documentation](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg "Documentation")

```
$ sudo npm install semistandard --global 
```

### Install `request` module and use it

[Documentation](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ "Documentation")

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules 
```

# TASKS answers :
0. We use the fs module to read the contents of a file.
The file path is passed as a command line argument and resolved using the path module.
The file is read using the fs.readFile method, with utf-8 encoding specified.
If there is an error reading the file, the error object is printed to the console using console.error.
The file contents are printed to the console using console.log if no error occurs.

1. The script takes two command line arguments, the first is the file path, and the second is the string to write. 
The __fs.appendFile__ method is used to write the string to the file.
can use also __fs.writeFile__
The third argument is the encoding, which is set to 'utf-8'.
The fourth argument is a callback function that is called after the __write__ operation is complete.
If there was an error during the write, it is passed to the callback function and printed to the console.

2. The request module  is used to send HTTP requests to a server and retrieve the response data.
A __GET request__ is a method used to retrieve information from a server without modifying any data on the server.
The __request.get function__ is used to send a GET request to the URL passed as the first argument.
If the request is successful, the status code of the response is logged to the console.
If there is an error, the error object is logged to the console.
URL USED : https://alx-intranet.hbtn.io/status && https://alx-intranet.hbtn.io/doesnt_exist

3. the request module to make a GET request to the Star Wars API and retrieve the data for the movie with the specified movieID.
The request function takes 
    *FIRST ARGUMENT* - the [URL of star wars API](https://swapi-api.alx-tools.com/api/films/${movieId})
    *SECOND ARGUMENT* - a callback function, that is the response data once the request is complete.
The script first checks if there was an error with the request and, if there was, it prints the error. Then, it checks the status code of the response and, if it's not 200 (OK), it prints an error message.

4. using requests , the  starwars API is passed so that we can find the character wedge Antilles and then we count how many times its occurs
The script first checks if there was an error with the request and, if there was, it prints the error. Then, it checks the status code of       the response and, if it's not 200 (OK), it prints an error message.

5. Now we combine both request and fs module to gather contents from  a webpage  and the save it to  a file name of path.




