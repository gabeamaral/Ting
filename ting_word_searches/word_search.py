def exists_word(word, instance):
    words = list()
    ocorrencias = list()
    for index in range(len(instance)):
        for index2, line in enumerate(
            instance.search(index)["linhas_do_arquivo"]
        ):
            if word.lower() in line.lower():
                ocorrencias.append({"linha": index2 + 1})
        if ocorrencias:
            words.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(index)["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )
    return words


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
