import sqlite3

class Livro:
    def criar():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titulo VARCHAR(255) NOT NULL,
                ano INTEGER NOT NULL,
                editora VARCHAR(255) NOT NULL,
                quantidade INTEGER NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livro_autor (
                livro_id INTEGER NOT NULL,
                autor_id INTEGER NOT NULL,
                FOREIGN KEY(livro_id) REFERENCES livros(id),
                FOREIGN KEY(autor_id) REFERENCES autores(id),
                PRIMARY KEY (livro_id, autor_id)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livro_categoria (
                livro_id INTEGER NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(livro_id) REFERENCES livros(id),
                FOREIGN KEY(categoria_id) REFERENCES categorias(id),
                PRIMARY KEY (livro_id, categoria_id)
            );
        """)
        conn.close()

    def novo_livro(titulo, ano, editora, quantidade):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO livros (titulo, ano, editora, quantidade)
            VALUES (?, ?, ?, ?);
        """, (titulo, ano, editora, quantidade))
        conn.commit()
        conn.close()

    def listar_livros():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        resultado = []
        for row in cursor.fetchall():
            resultado.append({
                'id': row[0],
                'titulo': row[1],
                'ano': row[2],
                'editora': row[3],
                'quantidade': row[4],
            })
        conn.close()
        return resultado

    def detalha_livro(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM livros
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'titulo': item[1],
            'ano': item[2],
            'editora': item[3],
            'quantidade': item[4],
        }

    def atualiza_livro(id, titulo, ano, editora, quantidade):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE livros
            SET titulo=?, ano=?, editora=?, quantidade=?
            WHERE id=?;
        """, (titulo, ano, editora, quantidade, id))
        conn.commit()
        conn.close()

    def remove_livro(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM livro_autor WHERE livro_id=?;
        """, (id,))
        cursor.execute("""
            DELETE FROM livro_categoria WHERE livro_id=?;
        """, (id,))
        cursor.execute("""
            DELETE FROM livros WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

class Autor:
    def criar():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                data_nascimento DATE NOT NULL,
                nacionalidade VARCHAR(255) NOT NULL
            );
        """)
        conn.close()

    def novo_autor(nome, data_nascimento, nacionalidade):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO autores (nome, data_nascimento, nacionalidade)
            VALUES (?, ?, ?);
        """, (nome, data_nascimento, nacionalidade))
        conn.commit()
        conn.close()

    def listar_autores():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM autores")
        resultado = []
        for row in cursor.fetchall():
            resultado.append({
                'id': row[0],
                'nome': row[1],
                'data_nascimento': row[2],
                'nacionalidade': row[3],
            })
        conn.close()
        return resultado

    def detalha_autor(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM autores
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'nome': item[1],
            'data_nascimento': item[2],
            'nacionalidade': item[3],
        }

    def atualiza_autor(id, nome, data_nascimento, nacionalidade):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE autores
            SET nome=?, data_nascimento=?, nacionalidade=?
            WHERE id=?;
        """, (nome, data_nascimento, nacionalidade, id))
        conn.commit()
        conn.close()

    def remove_autor(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM livro_autor WHERE autor_id=?;
        """, (id,))
        cursor.execute("""
            DELETE FROM autores WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

class Categoria:
    def criar():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                descricao VARCHAR(500) NOT NULL
            );
        """)
        conn.close()

    def nova_categoria(nome, descricao):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO categorias (nome, descricao)
            VALUES (?, ?);
        """, (nome, descricao))
        conn.commit()
        conn.close()

    def listar_categorias():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categorias")
        resultado = []
        for row in cursor.fetchall():
            resultado.append({
                'id': row[0],
                'nome': row[1],
                'descricao': row[2],
            })
        conn.close()
        return resultado

    def detalha_categoria(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM categorias
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'nome': item[1],
            'descricao': item[2],
        }

    def atualiza_categoria(id, nome, descricao):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE categorias
            SET nome=?, descricao=?
            WHERE id=?;
        """, (nome, descricao, id))
        conn.commit()
        conn.close()

    def remove_categoria(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM livro_categoria WHERE categoria_id=?;
        """, (id,))
        cursor.execute("""
            DELETE FROM categorias WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

class Emprestimo:
    def criar():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emprestimos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                livro_id INTEGER NOT NULL,
                usuario_id INTEGER NOT NULL,
                data_emprestimo DATE NOT NULL,
                data_devolucao DATE,
                FOREIGN KEY(livro_id) REFERENCES livros(id),
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
            );
        """)
        conn.close()

    def novo_emprestimo(livro_id, usuario_id, data_emprestimo, data_devolucao):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao)
            VALUES (?, ?, ?, ?);
        """, (livro_id, usuario_id, data_emprestimo, data_devolucao))
        conn.commit()
        conn.close()

    def listar_emprestimos():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.id, l.titulo, u.nome, e.data_emprestimo, e.data_devolucao
            FROM emprestimos e
            JOIN livros l ON e.livro_id = l.id
            JOIN usuarios u ON e.usuario_id = u.id;
        """)
        resultado = []
        for row in cursor.fetchall():
            resultado.append({
                'id': row[0],
                'livro': row[1],
                'usuario': row[2],
                'data_emprestimo': row[3],
                'data_devolucao': row[4],
            })
        conn.close()
        return resultado

    def detalha_emprestimo(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.id, l.titulo, u.nome, e.data_emprestimo, e.data_devolucao
            FROM emprestimos e
            JOIN livros l ON e.livro_id = l.id
            JOIN usuarios u ON e.usuario_id = u.id
            WHERE e.id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'livro': item[1],
            'usuario': item[2],
            'data_emprestimo': item[3],
            'data_devolucao': item[4],
        }

    def atualiza_emprestimo(id, livro_id, usuario_id, data_emprestimo, data_devolucao):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE emprestimos
            SET livro_id=?, usuario_id=?, data_emprestimo=?, data_devolucao=?
            WHERE id=?;
        """, (livro_id, usuario_id, data_emprestimo, data_devolucao, id))
        conn.commit()
        conn.close()

    def remove_emprestimo(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM emprestimos
            WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

class Usuario:
    def criar():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            );
        """)
        conn.close()

    def novo_usuario(nome, email):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nome, email)
            VALUES (?, ?);
        """, (nome, email))
        conn.commit()
        conn.close()

    def listar_usuarios():
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        resultado = []
        for row in cursor.fetchall():
            resultado.append({
                'id': row[0],
                'nome': row[1],
                'email': row[2],
            })
        conn.close()
        return resultado

    def detalha_usuario(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM usuarios
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'nome': item[1],
            'email': item[2],
        }

    def atualiza_usuario(id, nome, email):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE usuarios
            SET nome=?, email=?
            WHERE id=?;
        """, (nome, email, id))
        conn.commit()
        conn.close()

    def remove_usuario(id):
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM emprestimos WHERE usuario_id=?;
        """, (id,))
        cursor.execute("""
            DELETE FROM usuarios WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    Livro.criar()
    Autor.criar()
    Categoria.criar()
    Emprestimo.criar()
    Usuario.criar()
