# Assistant of event agency 
## _a fun helper for your business_

[![N|Solid](https://avatars.githubusercontent.com/u/82182253?s=400&u=162b30109520f984d0c4b831572c07c82aff62d9&v=4)](https://github.com/Teosoph-s-company/new_project)

✨My name is Addy and I am your personal assistant.✨

I was created to help you run your business, keep all your customer records, remind you of important events, and make you laugh.

The data base of your clients consists of the contact's name, phone numbers, the contact`s birthday, emails, addresses and notes. Together, we can expand it and make more usefull.
----------------------------------------------------


Below you will find all the commands that I can perform for you:

## Commands

1. show all - I'll show you the whole addressbook and all information about all users
2. add contact John 481-234-56-78 - I'll add the new contact {name} and {phone, birthday, email or address} to you addressbook
3. remove contact John 481-234-56-78 - I'll remove the phone from the contac
4. remove contact John 04-04-1978 - I'll remove the birthday from the contact
5. change contact John 481-234-56-78 481-234-56-79 - I'll change the first phone of the contact on new one
6. change contact John 04-04-1978 04-04-1979 - I'll change the first birthday of the contact on new one
7. find contact all John - I'll search through the contents of the contact book. I will show you all the information about one user
8. find contact phone John - I'll show you phone and in how many days the contact"s birthday will be.
9. find contact birthday John - I'll show you in how many days the contact"s birthday will be.
10. find contact email John - I'll show you email and in how many days the contact"s birthday will be.
11. find contact address John - I'll show you address and in how many days the contact"s birthday will be.
12. find contact notes John - I'll show you notes about user and in how many days the contact"s birthday will be.
13. find by tag <tag> - I'll show you notes about all users by tag and in how many days the contact"s birthday will be.
14. name, phone, birthday, email or address {value} - I'll show you the {value} contacts from the addressbook about one or more users
            by a few digits of the phone number or letters of the name
15. near birthday {number} - search people, who birthday in {number} days
16. add notes {name} {tag} {note} - I'll add note by tag
17. change notes {name} {tag} {old_note} (new_note) - I'll change note by tag
18. delete notes {name} {tag} {note} - I'll delete note by tag
19. search {value} - search what do you need, if I contain it, I`ll show you
20. clean {path} - I'll sort out the old folder with a lot of information, make it easier and more convenient for you in the {path}


> I plan to develop and learn thanks to your commands, and become more and more useful in communication and business. I want to find a user-friendly interface, and connect a database, I think SQLite.

## Tech

Addy uses:

- Python 3.8

And of course Addy itself is open source with a public repository on GitHub.

## Installation

```sh 
python3 -m venv virtual_environment 
source virtual_environment/bin/activate 
pip install prettytable 
pip personal_assistent
```

## License

MIT

**Free Software!**
