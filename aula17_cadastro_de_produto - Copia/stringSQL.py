comandoSQL = {
   0: """
    CREATE TABLE IF NOT EXISTS Categorias (
	    codigoCategoria INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao VARCHAR(225) NOT NULL
   );
  """,
  1:"""
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
   2:"INSERT INTO Categorias (descricao) VALUES (?);",
   3:"""
   INSERT INTO Produtos (
     nome,
     codigoCategoria,
     preco,
     qt,
     ativo
   ) VALUES (?,?,?,?,?);
   """,
   4:"SELECT * FROM Categorias",
   5:"""
   UPDATE INTO Categorias SET descricao = ? 
   WHERE codigoCategoria = ? 
   """,
   6:"""
   UPDATE INTO Produtos SET nome = ? 
   WHERE codigoProduto = ? 
   """,
}
#SQL Injection