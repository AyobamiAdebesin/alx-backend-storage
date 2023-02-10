-- A SQL script that creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0 if the second number is 
-- equal to 0

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
	DECLARE c INT;
	IF b = 0 THEN
		SET c = 0
	ELSE
		SET c = a/ b;
	END IF
	RETURN c;
END;
