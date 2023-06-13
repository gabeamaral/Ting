import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(0, len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
    files = txt_importer(path_file)
    dictionary = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(files),
        'linhas_do_arquivo': files,
    }
    instance.enqueue(dictionary)
    print(dictionary, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos')
        return
    del_file = instance.dequeue()['nome_do_arquivo']
    print(f'Arquivo {del_file} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
