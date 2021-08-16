/*select mark.name, sum(stock.quantity), shop.name
from mark
left join stock on mark.id = stock.markID
left join shop on stock.shopID = shop.id
group by mark.name
having sum(stock.quantity) > 10*/

/*select mark.id, mark.name, shop.id, shop.name, stock.quantity from mark 
left join stock on stock.markID = mark.id 
left join shop on shop.id = stock.shopID 
group by mark.name having max(stock.quantity) and sum(stock.quantity) > 10*/

select mark.name, sum(stock.quantity), M.name
from mark
left join stock on mark.id = stock.markID
join (select mark.id, shop.name, stock.quantity from mark 
left join stock on stock.markID = mark.id 
left join shop on shop.id = stock.shopID 
group by mark.name having max(stock.quantity) and sum(stock.quantity) > 10) as M on M.id = mark.id
group by mark.name
having sum(stock.quantity) > 10