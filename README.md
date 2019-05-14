# Data Analysis of Google Tracking
Through Google Databse and Tacking Takeout here we will show series of tips and ticks to learn how to
* Build Search word Database.
* Creating Search over time video graphs.
All Details for this project is located in ONENOTE Page under: Building Search Word DataBase Project.
While the file location is at:
* ~/Desktop/My_DATA_MP/Learning/[1] Data_Analysis_Python_Tricks.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
Then login to the following website from Google:
https://myaccount.google.com/data-and-personalization
and then go to the Data & Personalization.
The you will go to download your data:
Grab them all to know more information that Google collect on you.

## Getting Started
We have created two VirtualEnv for each machine we are working and they are:

```
For MacPro     : Ghpylib37Conda
For MacBook Pro: X
```

## Steps
### make table
This step is shown in the SQLite DataBase as following:
![](https://github.com/Ghasak/Data_Analysis_Google_Tracking/blob/master/1.png)

### Search Data
list of stop words is located here: in a format of list (English word)
https://gist.github.com/sebleier/554280

### Dynamically inserting into a Database with SQLite.
```
From:
c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))
Get:
c.execute("INSERT INTO words (unix, word) VALUES (?,?)", (d,w))
```
https://pythonprogramming.net/sqlite-part-2-dynamically-inserting-database-timestamps/

### Folder Protection
the folder Backup has the files that needed to this session.
including the google Takeout and the mylife.db in SQLite.

### Initializing the repository
you will need to perform for bigger folders the following steps.
* initalizing your repository:
```
 git lfs track "*.db" "*.xlsx" "*.csv"
```
* uploading everything to the Staging Area
```
git add . and check with git status
```

### Working Progress ...
Similar to the other configurations, we will add more features to our current python file.
We will create a dynmaic figure that show the words that we googled in the past year.
Adding the DataBase to our SQL-Studio App on MacBook.
![](https://github.com/Ghasak/Data_Analysis_Google_Tracking/blob/master/2.gif)

### Prerequisites
What things you need to install the software and how to install them

```
pip install requirements.txt
```
to see your mylife.db you will need to install SQLite Studio.
## Python Version

I have used Python3.7 Anaconda.
See the results:
![]()
## Authors

* **Ghasak Ibrahim** - *Initial work* -

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
## Acknowledgments
* Hat tip to anyone whose code was used

## Inspiration
following this project from:
* [1] (https://www.youtube.com/watch?v=Siyg1Wn5VDs&list=PLQVvvaa0QuDfWjcDi0GB1AsAuSCAb_JoX&index=1&frags=pl%2Cwn)

## To add some keyboard keys use:
<kbd>Ctrl</kbd>
