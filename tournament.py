# Import psycopg2 as PostgreSQL adaper for Python.
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    query = "DELETE FROM players"
    c.execute(query)
    DB.commit()
    DB.close()


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    query = "DELETE FROM matches"
    c.execute(query)
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    query = "SELECT COUNT(player_id) AS num FROM players"
    c.execute(query)
    results = c.fetchone()
    DB.close()
    if results:
        return results[0]
    else:
        return '0'


def registerPlayer(name):
    """Adds a player to the tournament database.

   The database assigns a unique serial id number for the player.  (This
   should be handled by your SQL database schema, not in your Python code.)

   Args:
   name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (player_name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
    A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    query = """SELECT players.player_id AS id, players.player_name AS name,
                      standings.wins AS wins, standings.matches AS matches
               FROM players
               LEFT OUTER JOIN standings
               ON players.player_id = standings.id;
            """
    c.execute(query)
    rows = c.fetchall()
    DB.commit()
    DB.close

    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
        winner:  the id number of the player who won
        loser:  the id number of the player who lost
    """

# Log wins and losses into matches.
    DB = connect()
    c = DB.cursor()
    c.execute(
        "INSERT INTO matches (win, loss) VALUES (%s, %s)",
        (winner, loser,)
        )
    DB.commit()
    DB.close()

# Log wins and losses into standings.
    DB = connect()
    c = DB.cursor()
    query = """SELECT id, name, wins, losses, matches
               FROM standings;
            """
    c.execute(query)
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
    A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # Call a list of players ranked for suitable pairing.
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM standings;")
    rows = c.fetchall()
    db.close()

    # Create a function that pairs each player with their best matchup.
    i = 0
    pairings = []

    while i < len(rows):
        id1 = rows[i][0]
        name1 = rows[i][1]
        id2 = rows[i + 1][0]
        name2 = rows[i + 1][1]
        pairings.append((id1, name1, id2, name2))
        i = i + 2

    return pairings
