import sqlite3  # it is part of the standard library of python.
from tqdm import tqdm
import os
from collections import Counter
import numpy as np
cwd = os.getcwd()
from datetime import datetime
#=============================================
# Only for MAC-Users you have to use this:
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
#=============================================

conn = sqlite3.connect("mylife.db")
c = conn.cursor()

# Define Some constants
DAY = 86400
YEAR = 365 * DAY
SLIDE = 1 * DAY
WINDOW = 1 * YEAR

testing_list = []


def word_graph():
    SAVE_DIR = "word_images_1yrwin_1dslide"
    # We will define a starting and ending time, using SQL-Query.
    # Search for sqlite find max/min : SELECT MAX() FROM X
    # We will try to find maximum time.
    c.execute("SELECT max(unix) FROM words")
    #d = c.fetchall()
    max_time = c.fetchall()[0][0]  # you have a list with tuple inside thus we need [0][0]
    print(max_time)
    # We will aslo try to find the minimum time in our database
    c.execute("SELECT min(unix) FROM words")
    min_time = c.fetchall()[0][0]
    print("==============================================================")
    print(f"Maximum time is = {max_time} and minimum time is = {min_time}")
    print("==============================================================")

    """
    Including the following in our algorithm.
    We will iterate across all words in our database using while loop:
    """
    START = min_time
    END = min_time + WINDOW
    # print(START, END)
    # c.execute(f"SELECT word FROM words WHERE unix > {START} AND unix < {END}")
    # test = c.fetchall()[0]
    # print(test)
    # Iteration
    counter = 0  # This counter for the images that we will create.

    while END < max_time:
        print(counter)
        if os.path.isfile(f"./{SAVE_DIR}/{counter}.png"):
            pass
        else:
            words = []
            c.execute(f"SELECT word FROM words WHERE unix > {START} and unix < {END}")
        # Make your query for each word form your database.

            data = c.fetchall()
            # print(data)
            """
            for row in data:
                word = row[0]
                words.append(row[0])
            """
            words = [i[0] for i in data]

            # We will seek the most common words-Counter object.

            word_counter = Counter(words)
            common_words = [topic[0] for topic in word_counter.most_common(10)]
            # print(common_words)
            """
            Starting the figure collection here including:
                -
            """
            y_pos = np.arange(len(common_words))
            word_counts = [topic[1] for topic in word_counter.most_common(10)]  # bring the second value which is the count (dictionary the Counter actuall bring not tuple)
            plt.figure(figsize=(12, 7))
            plt.bar(y_pos, word_counts, align="center", alpha=0.5)
            plt.xticks(y_pos, common_words)
            plt.ylabel("Volume")
            plt.title(f"{datetime.fromtimestamp(END).day}-{datetime.fromtimestamp(END).month}-{datetime.fromtimestamp(END).year}")
            # plt.show()
            # Save the figure to the directory that we created
            plt.savefig(f"./{SAVE_DIR}/{counter}.png")
            plt.close()

        counter += 1
        START += SLIDE
        END += SLIDE

        # break


word_graph()
conn.commit()
conn.close()
# print(testing_list)
