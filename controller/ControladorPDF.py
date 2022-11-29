import os

from fpdf import FPDF


class ControladorPdf:
    # Constructor
    def __init__(self) -> None:
        super().__init__()
        self.pdf = FPDF()


    def carta_admision(self, st, controlador, entrevista_seleccionada, str_fecha_actual, parametro):
        # Se crea el pdf
        self.pdf.add_page()
        self.pdf.set_font("times", size=11)
        self.pdf.image("img/logoPUJhorizontal.png", 10, 16, 80)

        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        
        self.pdf.cell(185, 6, txt=f"Santiago de Cali, {str_fecha_actual}", ln = 1, align = 'L')
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.cell(185, 6, txt="Sr", ln = 1, align='L')
        self.pdf.set_font("times", 'B', size=11)
        self.pdf.cell(185, 6, txt=f"{entrevista_seleccionada.aspirante.nombre}", ln = 1, align = 'L')
        self.pdf.set_font("times", size=11)
        self.pdf.cell(185, 6, txt=f"Código {entrevista_seleccionada.aspirante.id}", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt=f"Municipio de {entrevista_seleccionada.municipio}", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.multi_cell(185, 6,
                            txt=f"En nombre de la Pontificia Universidad Javeriana Cali, me complace comunicarle que ha sido aceptada su solicitud de admisión por Ingreso Normal al Programa de {entrevista_seleccionada.programa} para el periodo de {entrevista_seleccionada.semestre}. Al formalizar su ingreso en nuestra institución encontrará un mundo de oportunidades de formación a su alcance que marcarán de manera positiva su vida personal y profesional futura.",
                            ln = 1, align = 'J')
        self.pdf.multi_cell(185, 6,
                            txt=f"Para efectos de la matrícula financiera, la Oficina de Servicios y Apoyo Financiero le enviará vía email el recibo de pago. Así mismo, lo(a) invitamos a preguntar y conocer las diferentes opciones de financiación que ofrece la Javeriana Cali en el siguiente enlace: http://www.javerianacali.edu.co/financiacion .",
                            ln = 1, align = 'J')
        self.pdf.cell(185, 6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.cell(185, 6,
                      txt=f"Su código de identificación en el programa es: {entrevista_seleccionada.aspirante.id}",
                      ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt=f"{parametro}", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.multi_cell(185, 6,
                            txt=f"La jornada de bienvenida e inducción se realizará el día {controlador.induccion}, en el {controlador.ubicacion}. sí puede asistir de manera presencial. Si prefiere asistir de manera remota, puede hacerlo conectándose a través del siguiente enlace: {controlador.enlace_zoom}. Durante la jornada participará en diferentes actividades que facilitarán su proceso de adaptación a la Universidad, por lo tanto, la asistencia es obligatoria.",
                            ln = 1, align = 'J')
        self.pdf.cell(185, 6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.cell(185, 6, txt="Cordial saludo,", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.image(controlador.firma, 10, 205, 30)

        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.set_font("times", 'B', size=11)
        self.pdf.cell(185, 6, txt=f"{controlador.firmante}", ln = 1, align = 'L')
        self.pdf.set_font("times", size=11)
        self.pdf.cell(185, 6, txt=f"{controlador.rol}", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt=f"{entrevista_seleccionada.programa}", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.cell(185, 6, txt="__________________________________________________________________________________________________________________________________________", ln = 1, align = 'L')

        self.pdf.set_font("times", size=8)
        self.pdf.set_text_color(89, 143, 188)
        self.pdf.cell(185, 6, txt="NIT 860.013.720-1", ln = 1, align = 'C')
        self.pdf.cell(185, 6,
                      txt="Calle 18 #118-250 Avenida Cañasgordas, Cali-Colombia, A.A. 26239, Código Postal: 760031",
                      ln = 1, align = 'C')
        self.pdf.cell(185, 6,
                      txt="PBX (+57-2) 321 8200 / 485 6400 - Línea gratuita nacional 01-8000-180556 - www.javerianacali.edu.co",
                      ln = 1, align = 'C')
        self.pdf.set_font("times", size=6)
        self.pdf.cell(185, 6, txt="Vigilada Mineducación Res. 12220 de 2016", ln = 1, align = 'C')
        # Se crea el archivo
        self.pdf.output(name=f'outputs/Admision_{entrevista_seleccionada.aspirante.id}.pdf', dest='F')
        # Abre el archivo
        full_path = os.path.join(os.getcwd(), f'outputs/Admision_{entrevista_seleccionada.aspirante.id}.pdf')

        os.startfile(full_path)

    def carta_no_admision(self, st, controlador, entrevista_seleccionada, str_fecha_actual):
        self.pdf.add_page()
        self.pdf.set_font("times", size=11)
        self.pdf.image("img/logoPUJhorizontal.png", 10, 16, 80)

        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.cell(185, 6, txt=f"Santiago de Cali, {str_fecha_actual}", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt = "", ln = 1)  # Espacio en blanco

        self.pdf.cell(185, 6, txt="Sr", ln = 1, align="L")
        self.pdf.set_font("times", 'B', size=11)
        self.pdf.cell(185, 6, txt=f"{entrevista_seleccionada.aspirante.nombre}", ln = 1, align = 'L')
        self.pdf.set_font("times", size=11)
        self.pdf.cell(185, 6, txt=f"Código {entrevista_seleccionada.aspirante.id}", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt=f"Municipio de {entrevista_seleccionada.municipio}", align="L")
        self.pdf.cell(185, 6, txt = "", ln = 1)  # Espacio en blanco

        self.pdf.multi_cell(185, 6,
                            txt=f"En nombre de la Pontificia Universidad Javeriana Cali quiero agradecerle el haber pensado en nosotros como su opción de formación académica y humana.",
                            ln = 1, align = 'J')
        self.pdf.multi_cell(185, 6,
                            txt=f"Lamentablemente, le informamos que su solicitud de admisión para el programa de la {entrevista_seleccionada.programa} para el periodo de {entrevista_seleccionada.semestre}, no ha sido exitoso.",
                            ln = 1, align = 'J')
        self.pdf.cell(185, 6, txt = "", ln = 1)  # Espacio en blanco

        self.pdf.multi_cell(185, 6,
                      txt=f"Agradecemos nuevamente su interés en nuestra Universidad y esperamos poder atender sus necesidades futuras en este u otro programa institucional.",
                      ln = 1, align = 'J')
        self.pdf.cell(185, 6, txt = "", ln = 1)  # Espacio en blanco

        self.pdf.cell(185, 6, txt="Reciba un Cordial saludo,", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt = "", ln = 1)  # Espacio en blanco

        self.pdf.image(controlador.firma, 10, 145, 30)

        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco
        self.pdf.cell(185,6, txt="", ln = 1)  # Espacio en blanco

        self.pdf.set_font("times", 'B', size=11)
        self.pdf.cell(185, 6, txt=f"{controlador.firmante}", ln = 1, align = 'L')
        self.pdf.set_font("times", size=11)
        self.pdf.cell(185, 6, txt=f"{controlador.rol}", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt=f"{entrevista_seleccionada.programa}", ln = 1, align = 'L')
        self.pdf.cell(185, 6, txt = "", ln = 1)  # Espacio en blanco

        self.pdf.cell(185, 6, txt="__________________________________________________________________________________________________________________________________________", ln = 1, align = 'L')

        self.pdf.set_font("times", size=10)
        self.pdf.set_text_color(89, 143, 188)
        self.pdf.cell(185, 6, txt="NIT 860.013.720-1", ln = 1, align = 'C')
        self.pdf.cell(185, 6,
                      txt="Calle 18 #118-250 Avenida Cañasgordas, Cali-Colombia, A.A. 26239, Código Postal: 760031",
                      ln = 1, align = 'C')
        self.pdf.cell(185, 6,
                      txt="PBX (+57-2) 321 8200 / 485 6400 - Línea gratuita nacional 01-8000-180556 - www.javerianacali.edu.co",
                      ln = 1, align = 'C')
        self.pdf.cell(185, 6, txt="Vigilada Mineducación Res. 12220 de 2016", ln = 1, align = 'C')
        # Se crea el archivo
        self.pdf.output(name=f'outputs/No_Admision_{entrevista_seleccionada.aspirante.id}.pdf', dest='F')
        # Se abre el archvio
        full_path = os.path.join(os.getcwd(), f'outputs/No_Admision_{entrevista_seleccionada.aspirante.id}.pdf')

        os.startfile(full_path)
