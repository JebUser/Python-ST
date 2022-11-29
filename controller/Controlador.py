from abc import abstractmethod
from datetime import datetime

from PIL import Image

from controller.ControladorPDF import ControladorPdf
from model.Aspirante import Aspirante
from model.Entrevista import Entrevista
import plotly.graph_objects as go

class Controlador:
    # Constructor
    def __init__(self):
        super().__init__()
        # Se mira en que mes estamos para saber que semestre debe mostrar el programa
        self.tiempo_actual = datetime.now()
        if self.tiempo_actual.month >= 6:
            bimestre = 2
        else:
            bimestre = 1

        self.semestre = [self.tiempo_actual.year, bimestre] # Se crea una lista que contiene año actual y semestre
        self.aspirantes = {}
        self.entrevistas = {}

        # Datos para la carta
        self.firma = Image.open('img/firma.jpg')
        self.firmante = "LUISA RINCON PEREZ"
        self.rol = "Directora de Programa"

        self.induccion = datetime(2023, 1, 21, 8, 0, 0)
        self.ubicacion = "Auditorio 1 de Almendros"
        self.enlace_zoom = "https://javerianacali-edu-co.zoom.us/j/8595879785 (Código de acceso: 271823)"

    def modificar_carta(self, induccion, ubicacion, enlace_zoom):
        self.induccion = induccion
        self.ubicacion = ubicacion
        self.enlace_zoom = enlace_zoom
    
    def agregar_aspirante(self, aspirante):
        self.aspirantes[aspirante.id] = aspirante

    def agregar_entrevista(self, entrevista):
        key = entrevista.fecha.strftime('%Y-%m-%d') + "/" + entrevista.hora.strftime('%H-%M')
        self.entrevistas[key] = entrevista

    def modificar_firma_firmante(self, firma, firmante, rol):
        self.firma = firma
        self.firmante = firmante
        self.rol = rol

    def generar_periodos_posteriores(self):
        # Este metodo genera los periodos posteriores al año/semestre actual y retorna una lista de ellos
        posteriores = []
        ano = datetime.now().year
        bimestre = self.semestre[1]
        for i in range(3):
            if bimestre == 2:
                ano += 1
                bimestre = 1
                posteriores.append([ano, bimestre])
            else:
                bimestre = 2
                posteriores.append([ano, bimestre])

        return posteriores

    def generar_periodo_posterior(self):
        # Este metodo genera el periodo posterior para el caso de que el director de programa lo acepte
        posteriores = []
        ano = datetime.now().year
        bimestre = self.semestre[1]
        if bimestre == 2:
            ano += 1
            bimestre = 1
            posteriores.append([ano, bimestre])
        else:
            bimestre = 2
            posteriores.append([ano, bimestre])

        return posteriores

    # Metodos para ver en todos los roles
    def mostrar_aspirantes(self, st):
        # Primero verificar si hay registrado algun aspirante para poder crear la entrevista.
        if [self.aspirantes[key] for key in self.aspirantes]:
            st.write("Aspirantes Disponibles:")
        else:
            st.warning("No hay ningun aspirante registrado en el sistema.")

        conteo = 1
        # Se muestran cada uno de los aspirantes registrados (probablemente salga en desorden por lo que se usan
        # diccionarios)
        for key in self.aspirantes:
            st.write("#### Aspirante N°", conteo)
            conteo += 1
            col0, col1, col2 = st.columns(3)
            col3, col4, col5 = st.columns(3)
            col6, col7, col8 = st.columns(3)
            col9, col10, col11 = st.columns(3)
            col12, col13, col14 = st.columns(3)
            col15, col16, col17 = st.columns(3)

            with col0:
                st.write("**Cédula de Ciudadanía**")
                st.write(self.aspirantes[key].id)
            with col1:
                st.write("**Nombre del Aspirante**")
                st.write(self.aspirantes[key].nombre)
            with col2:
                st.write("**Teléfono**")
                st.write("+57", self.aspirantes[key].telefono)
            with col3:
                st.write("**Email**")
                st.write(self.aspirantes[key].email)
            with col4:
                st.write("**Mascotas**")
                st.write(self.aspirantes[key].mascotas)
            with col5:
                st.write("**Núcleo Familiar**")
                st.write(self.aspirantes[key].familia)
            with col6:
                st.write("**Detalles Info Personal**")
                st.write(self.aspirantes[key].detalles)
            with col7:
                st.write("**Desempeño ordenado**")
                st.write(self.aspirantes[key].desempeno)
            with col8:
                st.write("**Educacion**")
                st.write(self.aspirantes[key].educacion)
            with col9:
                st.write("**Sitios de Estudio/Actualización**")
                st.write(self.aspirantes[key].sitios_estudio)
            with col10:
                st.write("**Lugar de Trabajo Actual**")
                st.write(self.aspirantes[key].lugar_trabajo)
            with col11:
                st.write("**Nombre de la Empresa**")
                st.write(self.aspirantes[key].nombre_empresa)
            with col12:
                st.write("**Ingrso mensual en salarios mínimos**")
                st.write(self.aspirantes[key].ingreso_mensual)
            with col13:
                st.write("**Modalidad de Trabajo**")
                st.write(self.aspirantes[key].modalidad_trabajo)
            with col14:
                st.write("**¿Ha liderado equipos de trabajo?**")
                st.write(self.aspirantes[key].liderado)
                if self.aspirantes[key].liderado:
                    st.write("Personas a cargo: ", self.aspirantes[key].personas_a_cargo)
            with col15:
                st.write("**Roles Desempeñados**")
                st.write(self.aspirantes[key].roles)
            with col16:
                st.write("**Años de experiencia profesional relacionada con el programa**")
                st.write(self.aspirantes[key].exp)
            with col17:
                st.write("**Detalles Info Personal y Perfil**")
                st.write(self.aspirantes[key].info)

    def mostrar_entrevistas(self, st):
        if [self.entrevistas[key] for key in self.entrevistas]:
            st.write("Entrevistas Disponibles:")
        else:
            st.warning("No hay ningun aspirante registrado en el sistema.")

        conteo = 1
        # Se muestran cada una de las entrevistas registradas (probablemente salga en desorden por lo que se usan
        # diccionarios)
        for key in self.entrevistas:
            st.write("#### Entrevista N°", conteo)
            conteo += 1
            col0, col1, col2 = st.columns(3)
            col3, col4, col5 = st.columns(3)
            col6, col7 = st.columns(2)

            with col0:
                st.write("**Cédula de Ciudadanía**")
                st.write(self.entrevistas[key].aspirante.id)
            with col1:
                st.write("**Nombre del Aspirante**")
                st.write(self.entrevistas[key].aspirante.nombre)
            with col2:
                st.write("**Fecha de la Entrevista**")
                st.write(self.entrevistas[key].fecha)
            with col3:
                st.write("**Hora de la Entrevista**")
                st.write(self.entrevistas[key].hora)
            with col4:
                st.write("**Programa de Interés**")
                st.write(self.entrevistas[key].programa)
            with col5:
                st.write("**Periodo de Interés**")
                st.write(self.entrevistas[key].semestre)
            with col6:
                st.write("**Preferencia de las Clases**")
                st.write(self.entrevistas[key].clases)
            with col7:
                st.write("**¿Se encuentra en el Valle del Cauca?**")
                st.write(self.entrevistas[key].en_valle)
                if not self.entrevistas[key].en_valle:
                    st.write("Municipio de Residencia", self.entrevistas[key].municipio)

    def view_agregar_aspirante(self, st):
        st.title("Generación de aspirantes")

        # Aca pide la información personal
        st.header("Perfil personal")
        id = st.number_input('Ingresa id del aspirante', step=1, value=0)
        nombre = st.text_input('Ingrese el nombre')
        telefono = st.number_input('Ingrese telefono', step=1, value=0)
        email = st.text_input('Ingrese email')
        mascotas = st.multiselect('Mascotas', ['Perro', 'Gato', 'Otro'])
        if 'Otro' in mascotas:
            mascotas.append(st.text_input("Ingrese su otra mascota"))
        familia = st.multiselect('Estado familiar:',
                                 ['Vive solo', 'Viven con l@ parej@', 'Tiene hijos', 'Vive con los padres',
                                  'Vive con hermanos', 'Vive con tios', 'Vive con amigos'])
        detalles = st.text_area('Ingrese detalles adicionales sobre el perfil personal')

        # Aca pide la informacion laboral
        st.header("Perfil laboral")
        desempeno = st.multiselect('Seleccione en orden, ¿Que rol se desempeña mejor?',
                                   ['Trabajo en equipo', 'Expresión oral', 'Expresión escrita', 'Liderazgo'])

        st.subheader("Nivel de educación")
        # Este if revisa si el usuario puso que tiene otro nivel de educación
        educacion = st.selectbox('Ingrese nivel de educación',
                                 ['Ing de sistemas', 'Ing electrónico', 'Profesión afin', 'Otro'])
        if educacion == 'Otro':
            educacion = st.text_input('Ingrese otro nivel de educación')

        st.subheader("Plataformas de aprendizaje")
        # Este if revisa si el usuario puso que tiene otro nivel de educación
        sitios_estudio = st.multiselect('Ingrese sitios de estudio',
                                        ['Platzi', 'Coursera', 'Udemy', 'Udacity', 'Youtube', 'Libros',
                                         'Otras plataformas'])
        if 'Otras plataformas' in sitios_estudio:
            sitios_estudio.append(st.text_input('Ingrese otros sitios de estudio'))

        lugar_trabajo = st.multiselect('Ingrese lugar/es de trabajo',
                                       ['Empresa propia', 'extranjera', 'Colombiana', 'Freelance'])
        nombre_empresa = st.text_input('Ingrese nombre del lugar de trabajo actual')
        ingreso_mensual = st.selectbox('Ingrese el ingreso mensual en salarios minimos',
                                       ['Menos de tres', 'Entre tres y cinco', 'Entre cinco y nueve', 'Diez o más'])
        modalidad_trabajo = st.radio('Ingrese modalidad de trabajo',
                                     ['Presencialidad total', 'presencialidad parcial', 'teletrabajo'], horizontal=True)

        #  Opcion para ver si el aspirante ha liderado y habilita la opcion de si ha tenido más gente a cargo
        liderado = st.checkbox('Has liderado? Marca para si')
        if liderado:
            personas_a_cargo = st.number_input('¿Cuantas personas has tenido a cargo?', step=1, value=0)
        else:
            personas_a_cargo = 0
        roles = st.multiselect('¿Que roles has desempeñado?',
                               ['Desarrollador', 'Arquitecto', 'Líder técnico',
                                'QA automator', 'Gerente de proyecto', 'Scrum master'
                                   , 'Otro rol admin'])
        if 'Otro rol admin' in roles:
            roles.append(st.text_input("Ingrese otro rol"))
        exp = st.number_input('Ingrese sus años de experiencia', step=1, value=0)
        info = st.text_area('Detalles adicionales sobre la infor profesional')

        # Crea el objeto aspirante
        aspirante = Aspirante(id, nombre, telefono, email, mascotas, familia, detalles, desempeno, educacion,
                              sitios_estudio
                              , lugar_trabajo, nombre_empresa, ingreso_mensual, modalidad_trabajo, liderado,
                              personas_a_cargo, roles,
                              exp, info)
        # Se verifica si no dejo nada sin responder y luego se agrega el objeto aspirante al diccionario
        if st.button('Agregar aspirante'):
            if (id != 0 and nombre != "" and telefono != 0 and email != "" and len(mascotas) != 0
                    and len(familia) != 0 and detalles != "" and len(desempeno) == 4 and educacion != ""
                    and len(sitios_estudio) != 0 and len(lugar_trabajo) != 0 and nombre_empresa != ""
                    and ingreso_mensual != "" and modalidad_trabajo != "" and (
                            not liderado or liderado and personas_a_cargo != 0)
                    and len(roles) != 0 and exp != 0 and info != ""):
                self.agregar_aspirante(aspirante)  # Agrega el aspirante a la lista de aspirantes
                st.balloons()
                st.success("Aspirante " + nombre + " agregado")
            else:
                st.warning("Por favor ingrese todos los campos!")
        return self
    def crear_entrevista(self, st):
        st.title("Ingresar datos de una Entrevista")
        seleccion = st.selectbox('Selecciona el aspirante entrevistado',
                                 [(self.aspirantes[key].nombre, self.aspirantes[key].id) for key in
                                  self.aspirantes])  # Esta variable recibe la llave del aspirante al cual se le va a realizar la entrevista.
        fecha = st.date_input('Fecha de la entrevista')
        hora = st.time_input('Hora de la entrevista')
        programa = st.selectbox('Programa de interés',
                                ('Maestría Ing Software', 'Especialización Ing Software', 'Co-terminal'))
        semestre = st.selectbox('Periodo de interés', self.generar_periodos_posteriores())
        clases = st.selectbox('Preferencia de las clases', ('Presencial', 'Virtual'))
        en_valle = st.checkbox('¿Se encuentra en el Valle del Cauca?, marque si es sí')
        if not en_valle:
            municipio = st.text_input('Municipio de Residencia')
        else:
            municipio = "Valle del Cauca"

        if st.button("Enviar"):
        # Se verifica que no deja nada sin responder y se agrega la entrevista al diccionario
            if seleccion is not None and fecha != self.tiempo_actual.date and programa != "" and semestre != [] and clases != "" and municipio != "":
                entrevista = Entrevista(self.aspirantes[seleccion[1]], fecha, hora, programa, semestre, clases,
                                        en_valle, municipio, "Por Confirmar", "Por generar")  # Cuando se quiere crear la entrevista, se busca al aspirante con la llave que se registró anteriormente.
                self.agregar_entrevista(entrevista)
                st.balloons()
                st.success("Entrevista agregada exitosamente.")
            else:
                st.warning("Por favor llenar todos los campos.")

    def editar_info_aspirantes(self, st):
        # Edita los aspirantes y entrevistas separados en displays
        st.title("Editar info de aspirantes")
        # Selecciona el objeto entrevista que contiene el aspirante
        selec = st.selectbox('Selecciona el aspirante entrevistado a editar',
                             [(self.entrevistas[key].aspirante.nombre, key) for key in
                              self.entrevistas])
        entrevista_sel = self.entrevistas[selec[1]]
        # Se le pide la nueva información al usuario mostrando la información anterior
        with st.expander("Editar información de aspirante"):
            st.header(f"Se ha seleccionado el aspirante {entrevista_sel.aspirante.nombre}")
            st.header("Perfil personal")
            id = st.number_input('Ingresa nuevo id del aspirante', step=1, value=entrevista_sel.aspirante.id)
            nombre = st.text_input('Ingrese el nuevo nombre', entrevista_sel.aspirante.nombre)
            telefono = st.number_input('Ingrese nuevo telefono', step=1, value=entrevista_sel.aspirante.telefono)
            email = st.text_input('Ingrese nuevo email', entrevista_sel.aspirante.email)
            mascotas = st.multiselect('Nuevas mascotas', entrevista_sel.aspirante.mascotas,
                                      entrevista_sel.aspirante.mascotas)
            if 'Otro' in mascotas:
                mascotas.append(st.text_input("Ingrese su otra nueva mascota"))
            familia = st.multiselect('Nuevo estado familiar:',
                                     ['Vive solo', 'Viven con l@ parej@', 'Tiene hijos', 'Vive com los padres',
                                      'Vive con hermanos', 'Vive con tios', 'Vive con amigos'],
                                     entrevista_sel.aspirante.familia)
            detalles = st.text_area('Ingrese nuevos detalles adicionales sobre el perfil personal',
                                    entrevista_sel.aspirante.detalles)

            # Aca pide la informacion laboral
            st.header("Perfil laboral")
            desempeno = st.multiselect('Seleccione en orden, ¿Que rol se desempeña mejor ahora?',
                                       ['Trabajo en equipo', 'Expresión oral', 'Expresión escrita', 'Liderazgo'],
                                       entrevista_sel.aspirante.desempeno)

            st.subheader("Nivel de educación")
            # Este if revisa si el usuario puso que tiene otro nivel de educación
            st.info(f"Eduación anterior: {entrevista_sel.aspirante.educacion}")
            educacion = st.selectbox('Ingrese nuevo nivel de educación',
                                     ['Ing de sistemas', 'Ing electrónico', 'Profesión afin', 'Otro'])
            if educacion == 'Otro':
                educacion = st.text_input('Ingrese otro nuevo nivel de educación')

            st.subheader("Plataformas de aprendizaje")
            # Este if revisa si el usuario puso que tiene otro nivel de educación
            sitios_estudio = st.multiselect('Ingrese nuevos sitios de estudio',
                                            ['Platzi', 'Coursera', 'Udemy', 'Udacity', 'Youtube', 'Libros',
                                             'Otras plataformas'])
            if 'Otras plataformas' in sitios_estudio:
                sitios_estudio.append(st.text_input('Ingrese otros nuevos sitios de estudio'))

            lugar_trabajo = st.multiselect('Ingrese nuevo/s lugar/es de trabajo',
                                           ['Empresa propia', 'extranjera', 'Colombiana', 'Freelance'],
                                           entrevista_sel.aspirante.lugar_trabajo)
            nombre_empresa = st.text_input('Ingrese nuevo nombre del lugar de trabajo actual',
                                           entrevista_sel.aspirante.nombre_empresa)
            ingreso_mensual = st.selectbox('Ingrese el nuevo ingreso mensual en salarios minimos',
                                           ['Menos de tres', 'Entre tres y cinco', 'Entre cinco y nueve', 'Diez o más'])
            st.info(f"Salario anterior: {entrevista_sel.aspirante.ingreso_mensual}")
            modalidad_trabajo = st.radio('Ingrese nueva modalidad de trabajo',
                                         ['Presencialidad total', 'presencialidad parcial', 'teletrabajo'],
                                         horizontal=True)
            st.info(f"Modalidad anterior: {entrevista_sel.aspirante.modalidad_trabajo}")

            #  Opcion para ver si el aspirante ha liderado y habilita la opcion de si ha tenido más gente a cargo
            liderado = st.checkbox('Has liderado ahora? Marca para si')
            st.info(f"Ha liderado antes? {entrevista_sel.aspirante.liderado}")
            if liderado:
                personas_a_cargo = st.number_input('¿Cuantas personas has tenido a cargo?', step=1,
                                                   value=entrevista_sel.aspirante.personas_a_cargo)
            else:
                personas_a_cargo = 0
            roles = st.multiselect('¿Que roles nuevos has desempeñado?',
                                   ['Desarrollador', 'Arquitecto', 'Líder técnico',
                                    'QA automator', 'Gerente de proyecto', 'Scrum master'
                                       , 'Otro rol admin'], entrevista_sel.aspirante.roles)
            if 'Otro rol admin' in roles:
                roles.append(st.text_input("Ingrese otro nuevo rol"))
            exp = st.number_input('Ingrese sus nuevo/s años de experiencia', step=1, value=entrevista_sel.aspirante.exp)
            info = st.text_area('Detalles nuevos adicionales sobre la infor profesional', entrevista_sel.aspirante.info)
            # Se remplaza el antiguo aspirante con uno nuevo
            if st.button('Guardar nueva info'):
                if (id != 0 and nombre != "" and telefono != 0 and email != "" and len(mascotas) != 0
                        and len(familia) != 0 and detalles != "" and len(desempeno) == 4 and educacion != ""
                        and len(sitios_estudio) != 0 and len(lugar_trabajo) != 0 and nombre_empresa != ""
                        and ingreso_mensual != "" and modalidad_trabajo != "" and (
                                not liderado or liderado and personas_a_cargo != 0)
                        and len(roles) != 0 and exp != 0 and info != ""):
                    entrevista_sel.aspirante = Aspirante(id, nombre, telefono, email, mascotas, familia, detalles,
                                                         desempeno,
                                                         educacion, sitios_estudio, lugar_trabajo, nombre_empresa,
                                                         ingreso_mensual,
                                                         modalidad_trabajo, liderado, personas_a_cargo, roles, exp,
                                                         info)
                    st.balloons()
                    st.success("Cambios guardados!")
                else:
                    st.warning("Por favor ingrese todos los campos!")

        with st.expander("Editar información entrevista"):
            st.header(f"Se ha seleccionado el aspirante {entrevista_sel.aspirante.nombre}")
            st.title("Ingresar nuevos datos de una Entrevista")
            fecha = st.date_input('Nueva fecha de la entrevista', entrevista_sel.fecha)
            hora = st.time_input('Nueva hora de la entrevista', entrevista_sel.hora)
            programa = st.selectbox('Nuevo programa de interés',
                                    ('Maestría Ing Software', 'Especialización Ing Software', 'Co-terminal'))
            st.info(f"Programa de interés anterior: {entrevista_sel.programa}")
            semestre = st.selectbox('Nuevo periodo de interés', self.generar_periodos_posteriores())
            st.info(f"Opcion seleccionada anteriormente: {entrevista_sel.semestre}")
            clases = st.selectbox('Nueva preferencia de las clases', ('Presencial', 'Virtual'),
                                  )
            st.info(f"Opcion seleccionada anteriormente: {entrevista_sel.clases}")
            en_valle = st.checkbox('¿Todavía se encuentra en el Valle del Cauca?, marque si es sí')
            st.info(f"Opcion seleccionada anteriormente: {entrevista_sel.en_valle}")
            if not en_valle:
                municipio = st.text_input('Municipio de Residencia', entrevista_sel.municipio)
            else:
                municipio = "Valle del Cauca"
            admision = st.selectbox("Estado de admisión",
                                    ['Admitido', 'No admitido', 'Admitido con reserva', 'Por confirmar'])
            st.info(f"Estado de admisión anterior: {entrevista_sel.admitido}")
            carta_estado = st.selectbox("Estado de generación de carta", ['Generada', 'Por generar'])
            st.info(f"Estado de la carta de admisión anterior: {entrevista_sel.admitido}")

            if st.button("Guardar información"):
                # En caso de que la fecha y hora no se cambien, solo se cambian los demás valores
                if fecha == entrevista_sel.fecha or hora == entrevista_sel.fecha:
                    if selec is not None and fecha != self.tiempo_actual.date and programa != "" and semestre != [] and clases != "" and municipio != "":
                        self.entrevistas[selec[1]].fecha = fecha
                        self.entrevistas[selec[1]].hora = hora
                        self.entrevistas[selec[1]].programa = programa
                        self.entrevistas[selec[1]].semestre = semestre
                        self.entrevistas[selec[1]].clases = clases
                        self.entrevistas[selec[1]].en_valle = en_valle
                        self.entrevistas[selec[1]].municipio = municipio
                        self.entrevistas[selec[1]].admitido = admision
                        self.entrevistas[selec[1]].carta_generada = carta_estado
                        st.balloons()
                        st.success("Entrevista modificada exitosamente")
                    ''' 
                    En caso de que se cambio la fecha y hora, se tiene que crear una nueva entrevista ya que la fecha
                    y hora son la clave de las entrevistas en el diccionario
                    '''
                elif fecha != entrevista_sel.fecha or hora != entrevista_sel.fecha:
                    entrevista = Entrevista(entrevista_sel.aspirante, fecha, hora, programa, semestre, clases,
                                            en_valle, municipio,
                                            admision,
                                            carta_estado)  # Cuando se quiere crear la entrevista, se busca al
                    # aspirante con la llave que se registró anteriormente.
                    self.agregar_entrevista(entrevista)
                    del self.entrevistas[selec[1]]
                    st.balloons()
                    st.success("Entrevista modificada exitosamente")
                else:
                    st.warning("Por favor llenar todos los campos.")

        return self

    def generar_carta(self, st):
        controladorpdf = ControladorPdf()
        str_fecha_actual = self.tiempo_actual.strftime('%Y-%m-%d')
        parametro = "(Sin Condiciones)"

        st.title("Generar carta")
        # Se selecciona una tupla que contiene la llave del diccionario, el nombre del aspirante y su id
        seleccion = st.selectbox('Seleccione la entrevista', [
            (key, self.entrevistas[key].aspirante.nombre, self.entrevistas[key].aspirante.id) for key in
            self.entrevistas if self.entrevistas[key].carta_generada == "Por generar"])

        admitido = self.entrevistas[seleccion[0]].admitido
        # En caso ser admitido con reserva se recoge su justificación
        if admitido == 'Admitido con Reserva':
            parametro = self.entrevistas[seleccion[0]].infoadmitido

        if st.button('Generar Carta') and seleccion is not None:
            if admitido == 'Admitido' or admitido == 'Admitido con Reserva':
                # Llama al controlador pdf para crear la carta
                controladorpdf.carta_admision(st, self, self.entrevistas[seleccion[0]], str_fecha_actual,
                                              parametro)

                st.balloons()
                st.success("Carta generada, aspirante admitido.")
            elif admitido == 'Por generar':
                st.warning("Aún falta por revisar esta entrevista")
            else:
                controladorpdf.carta_no_admision(st, self, self.entrevistas[seleccion[0]],
                                                 str_fecha_actual)

                st.snow()
                st.success("Carta generada, aspirante no admitido.")

            self.entrevistas[seleccion[0]].admitido = admitido
        else:
            st.warning("Por favor seleccione una entrevista.")

    def estadisticas(self, st):
        # Preferencias de las clases (esto para saber los gustos de los aspirantes respecto a los metodos de aprendizaje)
        presencial = 0
        virtual = 0

        # Valores de admisión (esto para poder revisar la tasa de aceptación y cuantas entrevistas faltan por revisar)
        admitidos = 0
        admitidos_reserva = 0
        no_admitidos = 0
        por_generar = 0

        # Programas de interés (esto para poder revisar el programa de interés más demandado)
        maestria = 0
        especializacion = 0
        coterminal = 0

        # Se encuentra en valle? (esto para poder revisar la población perteneciente al valle)
        en_valle = 0
        no_en_valle = 0

        # Revisamos todos los datos necesarios entre las entrevistas.
        for key in self.entrevistas:
            if self.entrevistas[key].clases == 'Presencial':
                presencial += 1
            else:
                virtual += 1

            if self.entrevistas[key].admitido == 'Admitido':
                admitidos += 1
            elif self.entrevistas[key].admitido == 'Admitido con Reserva':
                admitidos_reserva += 1
            elif self.entrevistas[key].admitido == 'No admitido':
                no_admitidos += 1
            else:
                por_generar += 1

            if self.entrevistas[key].programa == 'Maestría Ing Software':
                maestria += 1
            elif self.entrevistas[key].programa == 'Especialización Ing Software':
                especializacion += 1
            else:
                coterminal += 1

            if self.entrevistas[key].en_valle:
                en_valle += 1
            else:
                no_en_valle += 1

        # Ahora se muestran los respectivos datos en diagramas circulares.
        st.title("Estadísticas")

        st.write("**Preferencias de clases**")
        graph_clases = go.Figure(data = [go.Pie(labels=["Presencial", "Virtual"], values = [presencial, virtual])])
        st.write(graph_clases)

        st.write("**Tasa de Admisiones**")
        graph_admisiones = go.Figure(data = [go.Pie(labels=["Admitido", "Admitido con Reserva", "No admitido", "Por generar"], values = [admitidos, admitidos_reserva, no_admitidos, por_generar])])
        st.write(graph_admisiones)

        st.write("**Tasa de Programas de Interés**")
        graph_programas = go.Figure(data = [go.Pie(labels=["Maestría Ing Software", "Especialización Ing Software", "Co-terminal"], values = [maestria, especializacion, coterminal])])
        st.write(graph_programas)

        st.write("**Aspirantes que se encuentran en el Valle del Cauca**")
        graph_valle = go.Figure(data = [go.Pie(labels=["Se encuentra", "No se encuentra"], values = [en_valle, no_en_valle])])
        st.write(graph_valle)

    # Metodos para roles especificos con sobreescritura

    @abstractmethod
    def generar_excel(self, st):
        pass

    @abstractmethod
    def cambiar_firma_firmante(self, st):
        pass

    @abstractmethod
    def generar_concepto_entrevista(self, st):
        pass