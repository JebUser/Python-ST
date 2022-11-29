from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo


class Controlador_excel:
    # Constructor del excel
    def __init__(self) -> None:
        super().__init__()
        self.excel_nombre = ""
        self.wb = Workbook()

    def exportar_informacion(self, controlador, fecha_inicial, fecha_final):
        # Activar el archivo para modificar
        ws = self.wb.active
        # Agregar los encabezados de la tabla
        ws.append(["Id", "Nombre", "Télefono", "Email", "Mascotas", "Familia",
                   "Detalles personales", "Desempeño", "Educacion", "Sitios estudio",
                   "Lugar trabajo", "Nombre empresa", "Ingreso mensual", "Modalidad trabajo",
                   "Ha liderado grupo de trabajo", "Personas acargo", "Roles desempeñados",
                   "Experiencia laboral", "Información profesional"])

        # Rows can also be appended
        i = 1
        for key in controlador.entrevistas:
            # Esta parte del codigo transforma las listas a strings para que el excel pueda visualizar los datos
            strmascotas = ""
            strfamilia = ""
            strdesempeno = ""
            strS_studio = ""
            strTrabajo = ""
            strRoles = ""
            flag = False
            j = 1
            if (fecha_inicial.year == fecha_final.year and
                    (fecha_inicial.month <= controlador.entrevistas[key].fecha.month <= fecha_final.month)):
                flag = True
            elif controlador.entrevistas[key].fecha.year == fecha_inicial.year:
                if fecha_inicial.month <= controlador.entrevistas[key].fecha.month:
                    flag = True
            elif controlador.entrevistas[key].fecha.year == fecha_final.year:
                if fecha_final.month >= controlador.entrevistas[key].fecha.month:
                    flag = True
            if flag:
                for word in controlador.entrevistas[key].aspirante.mascotas:
                    strmascotas += f"{word} "
                for word in controlador.entrevistas[key].aspirante.familia:
                    strfamilia += f"{word} "
                for word in controlador.entrevistas[key].aspirante.desempeno:
                    strdesempeno += f"{j}. {word} "
                    j += 1
                for word in controlador.entrevistas[key].aspirante.sitios_estudio:
                    strS_studio += f"{word} "
                for word in controlador.entrevistas[key].aspirante.lugar_trabajo:
                    strTrabajo += f"{word} "
                for word in controlador.entrevistas[key].aspirante.roles:
                    strRoles += f"{word} "
                # Aca agrega los datos al excel sin complicaciones
                ws.append([controlador.entrevistas[key].aspirante.id,
                           controlador.entrevistas[key].aspirante.nombre,
                           controlador.entrevistas[key].aspirante.telefono,
                           controlador.entrevistas[key].aspirante.email,
                           strmascotas,
                           strfamilia,
                           controlador.entrevistas[key].aspirante.detalles,
                           strdesempeno,
                           controlador.entrevistas[key].aspirante.educacion,
                           strS_studio,
                           strTrabajo,
                           controlador.entrevistas[key].aspirante.nombre_empresa,
                           controlador.entrevistas[key].aspirante.ingreso_mensual,
                           controlador.entrevistas[key].aspirante.modalidad_trabajo,
                           controlador.entrevistas[key].aspirante.liderado,
                           controlador.entrevistas[key].aspirante.personas_a_cargo,
                           strRoles,
                           controlador.entrevistas[key].aspirante.exp,
                           controlador.entrevistas[key].aspirante.info])
                i += 1

        # Aca empieza la configuración de la tabla
        tab = Table(displayName="Table1", ref=f"A1:S{i}")

        # Se agregan los estilos a las filas, colunmas y encabezado
        style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                               showLastColumn=False, showRowStripes=True, showColumnStripes=True)
        tab.tableStyleInfo = style
        ws.add_table(tab)

        # Se guarda el archivo
        self.excel_nombre = str(fecha_inicial) + " to " + str(fecha_final)
        self.wb.save(f"outputs/Aspirantes {self.excel_nombre}.xlsx")
