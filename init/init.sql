CREATE TABLE IF NOT EXISTS vendas (
    id SERIAL PRIMARY KEY,
    produto VARCHAR(100),
    quantidade INT,
    preco NUMERIC(10,2),
    data_venda DATE
);
