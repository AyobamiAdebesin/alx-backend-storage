-- A SQL script that creats an index idx_name_first_score
-- on the table `names` and the first letter of name and score

CREATE INDEX IF NOT EXISTS idx_name_first_score ON names (name(1), score);
