SELECT 

tb_pedidos.codigo_pedido , 
tb_clientes.codigo_cliente, tb_clientes.nome , tb_clientes.sobrenome , tb_clientes.endereco , tb_clientes.cidade ,
tb_pedidos.data_pedido ,
tb_produtos.produto, tb_produtos.preco, 
tb_pedidos.valor 

FROM

tb_produtos

JOIN 

tb_itens
ON
tb_produtos.codigo_produto = tb_itens.codigo_produto

JOIN

tb_pedidos
ON

tb_itens.codigo_pedido = tb_pedidos.codigo_pedido

join

tb_clientes
ON

tb_pedidos.codigo_cliente = tb_clientes.codigo_cliente 

WHERE

tb_clientes.cidade = "Sao Paulo" ;









