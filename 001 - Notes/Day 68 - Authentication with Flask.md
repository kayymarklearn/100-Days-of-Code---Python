2026-03-24 10:08

Status: Incomplete

Tags: [[Day 66 - Building REST API Service]]
[[Day 63 - Database with Sqlite]]

# **Authentication**
The most important component of a website is having users. Real humans who can contribute to the website. If Facebook had no users then it would just be adverts. If blogs had no users then it would just be the ramblings of an author.

But in order to have users and associate data to user accounts, we need a way to register them and allow them to sign back into their accounts at a later date.

This means they will be giving us some information that we have to keep secure. This is what authentication is all about, how to figure out if a user really is who they say they are. And that is the goal of today; Figure out how to register, login and logout users with email and password. So they can access their own private profile pages.

#### Encryption and Hashing
*Encryption* basically means scrambling something so others can't understand it unless they knew the key to decode (or unscramble) it.
![[Pasted image 20260324124949.png]]
*Hashing*  uses a so called hash function to turn data into a hash, the hash is stored in a db, hash functions are mathematical equations that make it almost impossible to turn a hash back into the original data. While encryption is used to ensure data cannot be read easily hashing is mainly used to ensure the integrity or authenticity of data. 
![[Pasted image 20260324130132.png]]

#### Hacking Passwords 101
The problem with hashing is that the same text always give the hash, so hackers can build hash tables for the most common passwords and compare those to the hash values in databases to get the passwords of users. When it comes to hashing, longer passwords are always better.
##### How to Make a hash table
- All words from a dictionary
- All numbers from a telephone book
- All combinations of characters up to 5 places.
- You can generate you hash table using a hash function.
- ...............More on this late

#### Hashing and Salting
*Salting* generates a random set of characters that is added to the text before being passed through the hash function to generate a new hash, this adds a new level of complexity to the hash.
![[Pasted image 20260324133209.png]]
#Note One of the industry standard hash functions is bcrypt.
*Salt rounds* Take data + salt hash it, take the new hash + salt and hash again, the number of times you do this is salt rounds. In our db we don't save passwords, we save salt + hash and their email and usernames.

#### code
> Check the flask_auth dir for code example.



## References
[Cryptii](https://cryptii.com/)
[Werkzeug security](https://werkzeug.palletsprojects.com/en/stable/utils/#module-werkzeug.security)
[Flask sessions](https://flask.palletsprojects.com/en/latest/quickstart/#sessions)
[Flask Login Manager](https://flask-login.readthedocs.io/en/latest/)
[Messages Flashing](https://flask.palletsprojects.com/en/stable/patterns/flashing/)


