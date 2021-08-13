select
    manufacturer.name as manufacturer
    ,shop.name as shop
    ,SUM(stock.quantity) as quantity
from
    manufacturer
   join mark on mark.manufacturerID = manufacturer.ID
   left join stock on stock.markID = mark.id
   left join shop on shop.id = stock.shopID
group by 
    manufacturer.name
    ,shop.name
order by SUM(stock.quantity) desc