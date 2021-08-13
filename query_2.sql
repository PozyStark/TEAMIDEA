select shop.name, mark.name, SUM(stock.quantity)
from shop

left join stock on shop.id = stock.shopID

left join mark on mark.id = stock.markID

left join manufacturer on manufacturer.id = mark.manufacturerID

where manufacturer.country = 'Japan'

group by shop.name
