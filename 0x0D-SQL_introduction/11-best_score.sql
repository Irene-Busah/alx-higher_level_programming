-- Script to show records with top score at the beginning
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
