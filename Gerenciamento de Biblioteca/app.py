from flask import *
from db import Autor, Categoria, Emprestimo, Livro, Usuario

app = Flask(__name__)
app.secret_key = 'chave_foda'

@app.route('/')
def listar_livros():
    livros = Livro.listar_livros()
    return render_template('livros.html', livros=livros)

@app.route('/livros/novo', methods=['GET', 'POST'])
def novo_livro():
    if request.method == 'POST':
        dados = request.form.to_dict()
        Livro.novo_livro(dados.get('titulo'), dados.get('ano'), dados.get('editora'), dados.get('quantidade'))
        return redirect(url_for('listar_livros'))
    return render_template('form_livro.html', livro=None, title='Novo Livro')

@app.route('/livros/editar/<int:id>', methods=['GET', 'POST'])
def editar_livro(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        Livro.atualiza_livro(id, dados.get('titulo'), dados.get('ano'), dados.get('editora'), dados.get('quantidade'))
        return redirect(url_for('listar_livros'))
    livro = Livro.detalha_livro(id)
    return render_template('form_livro.html', livro=livro, title='Editar Livro')

@app.route('/livros/remover/<int:id>')
def remover_livro(id):
    Livro.remove_livro(id)
    return redirect(url_for('listar_livros'))

@app.route('/autores')
def listar_autores():
    autores = Autor.listar_autores()
    return render_template('autores.html', autores=autores)

@app.route('/autores/novo', methods=['GET', 'POST'])
def novo_autor():
    if request.method == 'POST':
        dados = request.form.to_dict()
        Autor.novo_autor(dados.get('nome'), dados.get('data_nascimento'), dados.get('nacionalidade'))
        return redirect(url_for('listar_autores'))
    return render_template('form_autor.html', autor=None, title='Novo Autor')

@app.route('/autores/editar/<int:id>', methods=['GET', 'POST'])
def editar_autor(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        Autor.atualiza_autor(id, dados.get('nome'), dados.get('data_nascimento'), dados.get('nacionalidade'))
        return redirect(url_for('listar_autores'))
    autor = Autor.detalha_autor(id)
    return render_template('form_autor.html', autor=autor, title='Editar Autor')

@app.route('/autores/remover/<int:id>')
def remover_autor(id):
    Autor.remove_autor(id)
    return redirect(url_for('listar_autores'))

@app.route('/categorias')
def listar_categorias():
    categorias = Categoria.listar_categorias()
    return render_template('categorias.html', categorias=categorias)

@app.route('/categorias/novo', methods=['GET', 'POST'])
def nova_categoria():
    if request.method == 'POST':
        dados = request.form.to_dict()
        Categoria.nova_categoria(dados.get('nome'), dados.get('descricao'))
        return redirect(url_for('listar_categorias'))
    return render_template('form_categoria.html', categoria=None, title='Nova Categoria')

@app.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        Categoria.atualiza_categoria(id, dados.get('nome'), dados.get('descricao'))
        return redirect(url_for('listar_categorias'))
    categoria = Categoria.detalha_categoria(id)
    return render_template('form_categoria.html', categoria=categoria, title='Editar Categoria')

@app.route('/categorias/remover/<int:id>')
def remover_categoria(id):
    Categoria.remove_categoria(id)
    return redirect(url_for('listar_categorias'))

@app.route('/emprestimos')
def listar_emprestimos():
    emprestimos = Emprestimo.listar_emprestimos()
    return render_template('emprestimos.html', emprestimos=emprestimos)

@app.route('/emprestimos/novo', methods=['GET', 'POST'])
def novo_emprestimo():
    if request.method == 'POST':
        dados = request.form.to_dict()
        Emprestimo.novo_emprestimo(dados.get('livro_id'), dados.get('usuario_id'), dados.get('data_emprestimo'), dados.get('data_devolucao'))
        return redirect(url_for('listar_emprestimos'))
    livros = Livro.listar_livros()
    usuarios = Usuario.listar_usuarios()
    return render_template('form_emprestimo.html', emprestimo=None, livros=livros, usuarios=usuarios, title='Novo Empréstimo')

@app.route('/emprestimos/editar/<int:id>', methods=['GET', 'POST'])
def editar_emprestimo(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        Emprestimo.atualiza_emprestimo(id, dados.get('livro_id'), dados.get('usuario_id'), dados.get('data_emprestimo'), dados.get('data_devolucao'))
        return redirect(url_for('listar_emprestimos'))
    emprestimo = Emprestimo.detalha_emprestimo(id)
    livros = Livro.listar_livros()
    usuarios = Usuario.listar_usuarios()
    return render_template('form_emprestimo.html', emprestimo=emprestimo, livros=livros, usuarios=usuarios, title='Editar Empréstimo')

@app.route('/emprestimos/remover/<int:id>')
def remover_emprestimo(id):
    Emprestimo.remove_emprestimo(id)
    return redirect(url_for('listar_emprestimos'))

@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.listar_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/usuarios/novo', methods=['GET', 'POST'])
def novo_usuario():
    if request.method == 'POST':
        dados = request.form.to_dict()
        Usuario.novo_usuario(dados.get('nome'), dados.get('email'))
        return redirect(url_for('listar_usuarios'))
    return render_template('form_usuario.html', usuario=None, title='Novo Usuário')

@app.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        Usuario.atualiza_usuario(id, dados.get('nome'), dados.get('email'))
        return redirect(url_for('listar_usuarios'))
    usuario = Usuario.detalha_usuario(id)
    return render_template('form_usuario.html', usuario=usuario, title='Editar Usuário')

@app.route('/usuarios/remover/<int:id>')
def remover_usuario(id):
    Usuario.remove_usuario(id)
    return redirect(url_for('listar_usuarios'))

if __name__ == '__main__':
    app.run(debug=True)
