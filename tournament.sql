-- Since there might be existing databases, we drop the "tournament" database.
-- This ensures that we eliminate any pre-existing data.
-- DROP DATABASE IF EXISTS tournament;

-- This code will eliminate pre-existing tables and views.
DROP TABLE IF EXISTS players, matches CASCADE;
DROP VIEW IF EXISTS win_total, loss_total, standings;

-- Create a new database titled "tournament".
CREATE DATABASE tournament;


-- Create table to catalog players in each tournament.
CREATE TABLE players ( player_id SERIAL PRIMARY KEY,
                      player_name TEXT );

-- Create table to catalog each match in each tournament.
CREATE TABLE matches ( match_id SERIAL PRIMARY KEY,
                     win INTEGER,
                     loss INTEGER,
                     FOREIGN KEY (win) REFERENCES players (player_id)  ON DELETE CASCADE,
                     FOREIGN KEY (loss) REFERENCES players (player_id)  ON DELETE CASCADE
                     );


-- Create a series of views to reflect the data recorded in matches and players.
-- Win total counts the number of wins for each player.
CREATE VIEW win_total as
            SELECT players.player_id as id, players.player_name as name,
                   COUNT(matches.win) as wins
                   FROM players 
                   LEFT JOIN matches ON players.player_id = matches.win
                   GROUP BY players.player_id 
                   ORDER BY wins;

-- Loss total counts the number of losses for each player.
CREATE VIEW loss_total as 
            SELECT players.player_id as id, players.player_name as name,
                   COUNT(matches.loss) as losses
                   FROM players 
                   LEFT JOIN matches ON players.player_id = matches.loss
                   GROUP BY players.player_id 
                   ORDER BY losses;

-- Standings is a ranked chart of players by most wins then fewest losses.
CREATE VIEW standings as
            SELECT win_total.id as id,
                   win_total.name as name, win_total.wins as wins, loss_total.losses as losses,
                   win_total.wins + loss_total.losses as matches
                   FROM win_total 
                   INNER JOIN loss_total
                   ON win_total.id = loss_total.id 
                   ORDER BY wins DESC, losses;
