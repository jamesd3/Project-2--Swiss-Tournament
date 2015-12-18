# Project-2--Swiss-Tournament Version 1.0 - 17 December 2015
- This is a project for Udacity's Full Stack Web Developer Nanodegree program

- The general purpose of this project is to successfully conduct a Swiss Style
  Tournament using Python and PostgreSQL


### Installation

To run this program, you will need to download the following files:

- tournament.sql
  Creates and connects to tournament database, then creates tables and views.

- tournament.py
  Program creates definitions necessary to conduct a tournament as follows:

      - connect connects to the PostgreSQL database.  Returns a database
        connection.

      - deletePlayers removes all the player records from the database.

      - deleteMatches removes all the match records from the database.

      - countPlayers returns the number of players currently registered.

      - registerPlayer adds a player to the tournament database.

      - playerStandings returns a list of the players and their win records,
        sorted by wins.
      - reportMatch records the outcome of a single match between two players.

      - swissPairings returns a list of pairs of players for the next round of
        a match.

- tournament_test.py
  Program runs a series of tests to ensure tournament.py is functional.

- Please also be sure to download Python 2.7 with psycopg2 module installed,
  a virtualization software package such as Oracle VM VirtualBox, GIT and 
  BASH or an appropriate emulation tool, and Vagrant for your development 
  environment.


### Changelog

Version 1.0 - 17 December 2015 

- Original Submission with features described as above.


### User Guide

In order to run this program, please run module for tournament_test.py

    1. Access Git Bash or equivalent emulation tool and configure Vagrant for
       your development environment. 

    2. Establish a database titled "tournament" and create tables and views
       from tournament.sql.

    3. Using your terminal run "tournament_test.py" by typing 
       "python tournament_test.py"

    4. If all tests pass, the tournament.py program works.


### Resources

- [https://docs.python.org/2/tutorial/controlflow.html] (https://docs.python.org/) 4.6 Defining functions for testPairings.

- [https://plus.google.com/u/0/events/cpm6l19ue5ohplkn335bhfv7910?authkey=CPyGkKyFhoeyVg] (https://plus.google.com/+Udacity/) Provides supplemental information to assist in project completion.

- [pep8online.com/] (http://pep8online.com/) for proper formatting of "*.py" files

- [wikihow.com/] (http://www.wikihow.com/) for proper readme formatting


### Tournament Project can be reached at:

Email: james.delapa@gmail.com

Website: Website Coming Soon
