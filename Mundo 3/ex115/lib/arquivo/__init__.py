def arqexiste(arquivo):
    import os

    os.chdir(r"C:\Users\riccm\OneDrive\Documentos\Cursos\Curso em Vídeo\curso-python\Mundo 3\ex115")
    try:
        abrir = open(arquivo, "rt")
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True
