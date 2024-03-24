comandoSQL = [
    """
    CREATE TABLE IF NOT EXISTS Categorias (
	    codigoCategoria INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao VARCHAR(225) NOT NULL
   )
  """,
  """
  CREATE TABLE if not EXISTS Produtos (
	codigoProduto INTEGER PRIMARY KEY AUTOINCREMENT,
    codigoCategoria INTEGER NOT NULL,
    preco DECIMAL(9,2),
    qt INTEGER,
    ativo BOOLEAN,
    CHECK (qt > 0),
    FOREIGN KEY (codigocategoria) REFERENCES Categorias(codigocategoria) -- campo de ligação 
   )
   """,
   
]