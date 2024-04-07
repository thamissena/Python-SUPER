comandoSQL = [
    """
    CREATE TABLE IF NOT EXISTS Categorias (
	    codigoCategoria INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao VARCHAR(225) NOT NULL
   );
  """,
  """
  CREATE TABLE if not EXISTS Produtos (
	codigoProduto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    codigoCategoria INTEGER NOT NULL,
    preco DECIMAL(9,2),
    qt INTEGER,
    ativo BOOLEAN,
    CHECK (qt > 0),
    FOREIGN KEY (codigocategoria) REFERENCES Categorias(codigocategoria) -- campo de ligação 
   );
   """,
   "INSERT INTO Categorias (descricao) VALUES (?);",
   """
   INSERT INTO Produtos (
    nome,
    codigoCategoria,
    preco,
    qt,
    ativo
    ) VALUES (?,?,?,?,?);
   """,
   "SELECT * FROM Categorias",
]
#SQL Injection