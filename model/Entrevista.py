
class Entrevista:
    #Constructor
    # Recibe aspirante como el objeto de aspirante y semestre para automatizar la asignación del periodo en el controlador.
    def __init__(self, aspirante, fecha, hora, programa, semestre, clases, en_valle, municipio, admitido, carta_generada):
        self.aspirante = aspirante
        self.fecha = fecha
        self.hora = hora
        self.programa = programa
        self.semestre = semestre
        self.clases = clases
        self.en_valle = en_valle
        self.municipio = municipio
        self.admitido = admitido
        self.carta_generada = carta_generada
        self.infoadmitido = ""

