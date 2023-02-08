-- A script that creates a trigger that decreases the quantity
-- of an item after adding a new order
DELIMITER //

CREATE TRIGGER decrease_quant
AFTER INSERT ON order
FOR EACH ROW
	BEGIN
		UPDATE items
		SET quantity = quantiy - NEW.number WHERE name=NEW.item_name;
	END//
