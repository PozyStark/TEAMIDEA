select mark.name, manufacturer.name from mark 
left join manufacturer on mark.manufacturerID = manufacturer.id
where mark.id not in (select stock.markID from stock)