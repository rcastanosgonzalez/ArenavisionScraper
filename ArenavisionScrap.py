import requests

url_arenavision = "http://arenavision.in"
url_horarios = ""
urls_paginas_arenavision = []
urls_acestream = []
menu_arenavision = ""
horarios_arenavision = ""
tabla_horarios = ""


def obtener_pagina_arenavision():
    return do_request(url_arenavision)


def obtener_menu_arenavision():
    global menu_arenavision
    pagina_arenavision = obtener_pagina_arenavision()

    indice_menu = pagina_arenavision.find('class="leaf"')
    substring_menu = pagina_arenavision[indice_menu:]
    indice_menu = substring_menu.find('</nav>')
    substring_menu = substring_menu[:indice_menu]

    menu_arenavision = substring_menu


def obtener_enlace_horarios_arenavision():
    global url_horarios

    indice_horarios = menu_arenavision.find('<a href="/')
    substring_horarios = menu_arenavision[indice_horarios+9:]
    indice_horarios = substring_horarios.find('"')
    substring_horarios = substring_horarios[:indice_horarios]

    url_horarios = url_arenavision + substring_horarios


def obtener_pagina_horarios_arenavision():
    global horarios_arenavision
    horarios_arenavision = do_request(url_horarios)


def obtener_urls_paginas_arenavision():
    global urls_paginas_arenavision

    indice_arenavision = 1

    while menu_arenavision.find('ArenaVision ' + str(indice_arenavision)) != -1:
        indice_url = menu_arenavision.find('ArenaVision ' + str(indice_arenavision))
        substring_url = menu_arenavision[:indice_url]
        indice_url = substring_url.rfind('"')
        url = substring_url[substring_url.rfind('/'):indice_url]
        urls_paginas_arenavision.append(url_arenavision+url)

        indice_arenavision = indice_arenavision + 1


def obtener_urls_acestream():
    global urls_acestream

    for index in range(len(urls_paginas_arenavision)):

        data = do_request(urls_paginas_arenavision[index])

        indice = data.find("acestream://")
        substring = data[indice:]
        indice = substring.find('"')
        substring = substring[:indice]

        urls_acestream.append(substring)


def obtener_tabla_horarios():
    global tabla_horarios

    indice_horarios = horarios_arenavision.find("<table")
    substring_horarios = horarios_arenavision[indice_horarios:]
    indice_horarios = substring_horarios.find("</table>")
    substring_horarios = substring_horarios[:indice_horarios]
    substring_horarios = substring_horarios + '</table>'

    tabla_horarios = substring_horarios

    
def quitar_publicidad():
    global tabla_horarios

    while tabla_horarios.find('<td colspan="6"') != -1:
        indice_publicidad = tabla_horarios.find('<td colspan="6"')
        substring_tabla_inicio = tabla_horarios[:indice_publicidad]
        indice_fin_publicidad = tabla_horarios.find("</td>", indice_publicidad)
        substring_tabla_final = tabla_horarios[indice_fin_publicidad+5:]
        tabla_horarios = substring_tabla_inicio + substring_tabla_final

        
def generar_HTML():
    html_horarios = open('horarios.html', 'w')

    html_horarios.write('<!DOCTYPE html><html><head><link rel="stylesheet"href="https://fonts.googleapis.com/css?family=Roboto"><style>html{font-family: "Roboto";}table{width: 90%;border-collapse: collapse;}td{text-align:center;}tr{border-top: 1px solid black;}tr:hover {background-color: lightyellow;}</style><title>Horarios Arenavision</title></head><body>')
    html_horarios.write('<div align="center">')
    for index in range(len(urls_acestream)):
        html_horarios.write(" <a style='font-size:30px' href='"+urls_acestream[index]+"'>"+str(index+1)+"</a> |")

    html_horarios.write('</div><br /><br />')
    html_horarios.write(tabla_horarios)
    html_horarios.write('</body></html>')
    html_horarios.close()


def quitar_estilos():
    global tabla_horarios

    while tabla_horarios.find('style=') != -1:
        indice_estilo = tabla_horarios.find('style="')
        substring_anterior = tabla_horarios[:indice_estilo]
        substring_posterior = tabla_horarios[indice_estilo+7:]
        indice_final_estilo = substring_posterior.find('"')
        substring_posterior = substring_posterior[indice_final_estilo:]
        tabla_horarios = substring_anterior + substring_posterior


def do_request(url):
    data = requests.get(url)
    return data.text


obtener_menu_arenavision()
obtener_enlace_horarios_arenavision()
obtener_pagina_horarios_arenavision()
obtener_urls_paginas_arenavision()
obtener_urls_acestream()
obtener_tabla_horarios()
quitar_publicidad()
quitar_estilos()
generar_HTML()
