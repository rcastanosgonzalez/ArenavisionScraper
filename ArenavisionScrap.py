import requests

url_arenavision = "http://arenavision.in"
url_horarios = ""
urls_paginas_arenavision = []
urls_acestream = []
menu_arenavision = ""
horarios_arenavision = ""
tabla_horarios = ""
css_arenavision = "<style>body{background:#2f3238 url(images/bg.jpg);color:#bbb;font-family:'Open Sans Condensed',sans-serif;font-size:1em;line-height:1.5;margin:0;padding:0;width:100%;}h1,h2,h3,h4,h5,h6{font-family:'Yanone Kaffeesatz',sans-serif;font-style:normal;font-weight:normal;color:#ddd;margin-top:0.6em;}h1{font-size:2.4em;line-height:1.5;}h2{font-size:2em;line-height:1.2;}h3{font-size:1.8em;line-height:1.2;}h4,h5,h6{font-size:1.6em;line-height:1.5;}p{font-size:1.1em;line-height:1.5;margin:0 0 1.2em 0;}a{color:#d33b3c;text-decoration:none;}a:visited{color:#d33b3c;}a:hover,a:active,li a.active{color:#000;}a:focus{outline:thin dotted;}a:hover,a:active{outline:0;}li ul,li ol{margin:0;}ul,ol{margin:0 1.5em 1.5em 0;padding-left:1.5em;}ul{list-style-type:disc;}ol{list-style-type:decimal;}dl{margin:0 0 1.5em 0;}dl dt{font-weight:bold;}dd{margin-left:1.5em;}hr{background:#666;border:none;clear:both;float:none;height:1px;margin:0 0 1.4375em;width:100%;}fieldset{border:1px solid #ccc;margin:0 0 1.4375em;padding:1.5em;}table{margin-bottom:1.5em;width:100%;}th,tr,td{vertical-align:middle;}th{padding-right:1em;}.sticky-header th,.sticky-table th{border-bottom:3px solid #ccc;padding-right:1em;text-align:left;}img{max-width:100%;}blockquote{background-color:#2f3238;border-left:6px solid #d33b3c;padding:14px 14px 10px 14px;margin:10px 0px;}code,pre{background-color:#2f3238;border-left:6px solid #d33b3c;display:block;padding-left:20px;margin:10px 0;}strong{font-weight:bold;}i{font-style:italic;}.clear{clear:both;width:100%;}.display-block{display:block;}#main .content table{margin-bottom:1.5em;width:100%;}#main .content th{font-weight:bold;padding:10px 5px;background:#2f3238;border:1px solid #505259;}#main .content table td{border:1px solid #505259;padding:5px;}#content{width:1060px;margin:0 auto;background:#26292e url(images/content-bg.jpg);padding:25px 50px;position:relative;z-index:1;}#container{margin:0 auto;padding:0;width:1060px;}.container{width:1060px;margin:0 auto;padding:0;}.wrap{width:1060px;margin:0 auto;padding:0 10px;position:relative;}#main{display:inline;margin:0;}body.two-sidebars #main{float:left;margin:0 0 0 40px;padding:0;width:460px;}body.sidebar-first #main{float:right;margin:0;padding:0;width:730px;}body.sidebar-second #main{float:left;margin:0;padding:0;width:150px;}body.two-sidebars #sidebar-first{float:left;margin:0 0 0 -200px;padding:0;width:360px;}body.two-sidebars #sidebar-second{float:right;margin:0;padding:0;width:220px;}body.sidebar-first #sidebar-first{float:left;margin:0;padding:0;width:100px;}body.sidebar-second #sidebar-second{float:right;margin:0;padding:0;width:220px;}#header{padding-bottom:0px;margin:0 auto;clear:both;width:100%;height:-100px;}#header #logo{float:left;margin:0 1em 1.5em 0;}#social{}#social li{display:inline;float:right;}#social .icon{width:32px;height:32px;float:right;margin-left:1px;}#social .googleplus{background:url(images/googleplus.png) no-repeat;}#social .googleplus:hover{background:url(images/googleplus-hover.png) no-repeat;}#social .twitter{background:url(images/twitter.png) no-repeat;}#social .twitter:hover{background:url(images/twitter-hover.png) no-repeat;}#social .facebook{background:url(images/facebook.png) no-repeat;}#social .facebook:hover{background:url(images/facebook-hover.png) no-repeat;}#header .search-box .form-submit{display:none;}#header .search-box .form-text{background:url(images/search.png) no-repeat;border:0;padding:8px 0;color:#52575f;width:36px;cursor:pointer;}#header .search-box .form-text:focus{outline:none;background:#2f3238 url(images/search.png) no-repeat;padding:1px 1px 1px 1px;cursor:auto;}#navigation{clear:both;margin:0;padding:0;border-bottom:1px solid #52575f;font-family:'Open Sans Condensed',sans-serif;}#navigation ul.menu{clear:both;list-style:none;margin:0;padding:0;}#navigation ul.menu li{float:left;margin:0;padding:0;font-size:20px;list-style:none;}#navigation ul.menu li a{}#navigation ul.menu li a.active,#navigation ul.menu li a:hover{color:#d33b3c;}.navigation li{float:left;position:relative;}.navigation ul li a{display:block;padding:10px 20px 10px 10px;color:#86888b;text-transform:uppercase;}.navigation ul ul{position:absolute;left:0;display:none;margin:0 0 0 -1px;padding:0;list-style:none;border-bottom:1px solid #d33b3c;z-index:110;}.navigation ul ul li{width:170px;float:left;border-top:none;}.navigation ul ul a{}.navigation ul ul li a{background:#111314;display:block;padding:4px 10px;text-decoration:none;border-top:1px solid #d33b3c;text-transform:none;font-size:18px;}li.expanded>a:after{content:" + ";color:#52575f;font-weight:bold;}#breadcrumb{background-color:#2f3238;padding:0.5em 1em;margin-top:14px;}.breadcrumb{clear:both;}.breadcrumb a{color:#d33b3c;}.item-list ul{margin:0;padding:0 0 0 1.5em;}.item-list ul li{margin:0;padding:0;}ul.menu li{margin:0;padding:0;}ul.inline{clear:both;}ul.inline li{margin:0;padding:0 1em 0 0;}.tabs-wrapper{border-bottom:1px solid #333;margin:0 0 1.4375em;}ul.primary{border:none;margin:0;padding:0;}ul.primary li a{background:none;border:none;display:block;float:left;line-height:1.5em;margin:0;padding:0 1em;}ul.primary li a:hover,ul.primary li a.active{background:#000;border:none;color:#ddd;}ul.primary li a:hover{background:#888;text-decoration:none;}ul.secondary{background:#666;border-bottom:none;clear:both;margin:0;padding:0;}ul.secondary li{border-right:none;}ul.secondary li a,ul.secondary li a:link{border:none;color:#ccc;display:block;float:left;line-height:1.5em;padding:0 1em;}ul.secondary li a:hover,ul.secondary li a.active{background:#888;color:#fff;text-decoration:none;}ul.secondary a.active{border-bottom:none;}.node{margin-bottom:3em;}.submitted{background:#2f3238;padding:5px 10px;width:680px;margin:8px 0;}#main img{max-width:700px;}#main footer{margin-bottom:16px;font-family:'Yanone Kaffeesatz',sans-serif;}.field-name-field-tags{margin:0 0 1.5em;}.field-name-field-tags .field-item{margin:0 1em 0 0;}.field-name-field-tags div{display:inline;}ul.pager{margin-bottom:20px;padding:0;font-family:'Yanone Kaffeesatz',sans-serif;}ul.pager .pager-current{background-color:#222;color:#d33b3c;}.pager-item,.pager-next,.pager-last,.pager-previous,.pager-first{background-color:#d33b3c;color:#fff;}.pager-item a,.pager-next a,.pager-last a,.pager-previous a,.pager-first a{color:#fff;}.profile{margin:1.5em 0;}.profile h3{border:none;}.profile dt{margin-bottom:0;}.profile dd{margin-bottom:1.5em;}.password-parent{width:36em;}#comments{clear:both;margin-top:1.5em;}.comment{margin-bottom:1.5em;}.comment .new{color:red;text-transform:capitalize;margin-left:1em;}.block{margin-bottom:2.5em;}#footer .block ul,.sidebar .block ul{list-style-type:none;padding:0;margin:0;}#footer .block li{border-bottom:1px solid #1d2127;padding:4px 0;list-style:none;}.sidebar .block li{border-bottom:1px solid #17191d;padding:4px 0;list-style:none;}.sidebar .block img{max-width:220px;}#footer{clear:both;padding:1em 0;position:relative;font-family:'Open Sans Condensed',sans-serif;display:table;width:100%;}#footer a{color:#d33b3c;}#footer a:hover{color:#ddd;}#footer h2{border-bottom:1px solid #14181d;line-height:1.6;}.footer-one,.footer-two,.footer-three{width:300px;float:left;position:relative;}.footer-one img,.footer-two img,.footer-three img{max-width:300px;}.footer-one,.footer-two{margin-right:20px;}.footer-three{margin-right:0;}#footer-bottom{background:#26292e url(images/content-bg.jpg);padding:14px 0;width:100%;display:table;}#copyright{font-size:16px;width:100%;}#slider{float:left;margin-top:14px;}.main_view{float:left;position:relative;}.window{overflow:hidden;position:relative;width:1062px;height:352px;float:left;}.image_reel{position:absolute;top:0;left:0;}.image_reel img{float:left;}.paging{padding:7px 0 8px 0;text-align:center;z-index:100;}.paging a{text-indent:-9999px;background:url(images/slide-button.png) no-repeat center;width:15px;height:15px;display:inline-block;margin:4px;border:none;outline:none;}.paging a.active{background:url(images/slide-button-active.png) no-repeat center;border:none;outline:none;}.paging a:hover{font-weight:bold;border:none;outline:none;}.slidertitle{background:#d33b3c;display:none;position:absolute;bottom:100px;left:100px;z-index:100;color:#fff;font-size:2em;font-family:'Yanone Kaffeesatz',sans-serif;padding:10px;margin-bottom:14px;}.slidertext{background:#c65e5f;display:none;position:absolute;bottom:50px;left:100px;z-index:101;color:#fff;font-size:1.4em;padding:10px;font-family:'Open Sans Condensed',sans-serif;}.page-header{text-align:center;border-bottom:1px solid #33373c;width:100%;margin-bottom:30px;}.page-header h1{font-size:40px;text-transform:uppercase;color:#ddd;}.page-header h2{font-size:34px;text-transform:uppercase;color:#ddd;}.page-header p{font-size:30px;color:#818181;font-family:'Open Sans Condensed',sans-serif;}.full{width:940px;margin:0 auto;float:left;}.full .button{border:1px solid #52575f;border-radius:6px;padding:4px 10px;}.full .button:hover{border:2px solid #52575f;}.one_three{margin-right:2px;}.one_three_last{margin-right:0;}.one_three,.one_three_last{width:290px;min-height:200px;float:left;position:relative;text-align:center;background:#2f3238;padding:11px;}.last{margin-right:0;}#edit-submit,#edit-preview,#edit-delete,input.form-submit{background:#2f3238;padding:4px 10px;cursor:pointer;border:0;font-family:'Yanone Kaffeesatz',sans-serif;color:#ddd;font-size:1.2em;}#edit-submit:hover,#edit-preview:hover,#edit-delete:hover,input.form-submit:hover{color:#d33b3c;}</style>"


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


def generar_HTML():
    html_horarios = open('horarios.html', 'w')
    html_horarios.write(css_arenavision)

    for index in range(len(urls_acestream)):
        html_horarios.write(" | <a style='font-size:30px' href='"+urls_acestream[index]+"'>"+str(index+1)+"</a> ")

    html_horarios.write(tabla_horarios)
    html_horarios.close()


def do_request(url):
    data = requests.get(url)
    return data.text


obtener_menu_arenavision()
obtener_enlace_horarios_arenavision()
obtener_pagina_horarios_arenavision()
obtener_urls_paginas_arenavision()
obtener_urls_acestream()
obtener_tabla_horarios()
generar_HTML()
