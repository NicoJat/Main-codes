// Programa para calcular las propiedades de la seccion de acero

function seccioni() {

    let bf1 = parseFloat(document.getElementById('bf1').value);
    let tf1 = parseFloat(document.getElementById('tf1').value);
    let bf2 = parseFloat(document.getElementById('bf2').value);
    let tf2 = parseFloat(document.getElementById('tf2').value);
    let tw = parseFloat(document.getElementById('tw').value);
    let hw = parseFloat(document.getElementById('hw').value);

    let area = (bf1*tf1)+(bf2*tf2)+(tw*hw) 
    let centroidxi = (Math.max(bf1,bf2)*0.5)
    let centroidyi = (((tf2/2)*(bf2*tf2))+((tf2+(hw/2))*(tw*hw))+((tf2+hw+(tf1/2))*(bf1*tf1)))/area
    let inerciaxi = (((bf1*(tf1**3)/12))+(bf1*tf1*Math.abs(((tf2+(tf1/2)+hw-centroidyi)**2)))) + ((tw*(hw**3)/12)+(hw*tw*Math.abs(((tf2+(hw/2)-centroidyi))**2))) + ((bf2*(tf2**3)/12)+(bf2*tf2*(centroidyi-(tf2/2))**2))
    let inerciayi = (((tf1*(bf1**3)/12))) + ((hw*(tw**3)/12)) + ((tf2*(bf2**3)/12))
    let inerciapi = inerciaxi + inerciayi
    let x0i = Math.max((bf1/2),(bf2/2))
    let y0i = (tf1*(bf1**3)*hw)/((tf1*(bf1**3))+(tf2*(bf2**3)))
    let rxi = Math.sqrt(inerciaxi/area)
    let ryi = Math.sqrt(inerciayi/area)
    let cwi = ((hw**2)*tf1*(bf1**3)*(bf2**3))/(12*((bf1**3)+(bf2**3)))

    if (tf1 == tf2) {
        document.getElementById("cwi").innerHTML = 'La constante de alabeo es:      ' + cwi + ' cm6'
    }
    else {
        alert("No es posible calcular la constante de alabeo, Procure tf1 sea igual a tf2. Para perfiles I cuyos espesores de alas difieren utilice otra herramienta.")
    }
    
    document.getElementById("areabruti").innerHTML = 'El valor del área bruta es:   '  + area + '  cm2'
    document.getElementById("centroidxi").innerHTML = 'El centroide en X es:    ' + centroidxi + '  cm'
    document.getElementById("centroidyi").innerHTML = 'El centroide en Y es:    ' + centroidyi + '  cm'
    document.getElementById("inerciaxi").innerHTML = 'La inercia en X es:   ' + inerciaxi + '  cm4'
    document.getElementById("inerciayi").innerHTML = 'La inercia en Y es:   ' + inerciayi + '  cm4'
    document.getElementById("inerciapi").innerHTML = 'La inercia polar J es:    ' + inerciapi + '  cm4'
    document.getElementById("rxi").innerHTML = 'El radio de giro rx es:     ' + rxi + '  cm'
    document.getElementById("ryi").innerHTML = 'El radio de giro ry es:     ' + ryi + '  cm'
    document.getElementById("x0i").innerHTML = 'La coordenada x0 es:    ' + x0i + '  cm'
    document.getElementById("y0i").innerHTML = 'La coordenada y0 es:    ' + y0i + '  cm'
    
    //return area, inerciaxi, inerciayi, rxi, ryi
}

function seccionc() {
    let a1 = parseFloat(document.getElementById('a1').value);
    let a2 = parseFloat(document.getElementById('a2').value);
    let a3 = parseFloat(document.getElementById('a3').value);
    let e1 = parseFloat(document.getElementById('e1').value);
    let e2 = parseFloat(document.getElementById('e2').value);
    let e3 = parseFloat(document.getElementById('e3').value);

    let area = (a1*e1)+((a2)*(e2))+((a3)*(e3))
    let centroidxc = ((a1/2*a1*e1)+(e2/2*a2*e2)+(a3/2*a3*e3))/area
    let centroidyc = ((e3/2*a3*e3)+((e3+(a2/2))*a2*e2)+((e3+a2+(e1/2))*a1*e1))/area
    let inerciaxc = (((a1*(e1**3)/12))+(a1*e1*Math.abs(((e3+(e1/2)+a2-centroidyc)**2)))) + ((e2*(a2**3)/12)+(a2*e2*Math.abs(((e3+(a2/2)-centroidyc))**2))) + ((a3*(e3**3)/12)+(a3*e3*(centroidyc-(e3/2))**2))
    let inerciayc = (((e1*(a1**3)/12))+(a1*e1*Math.abs((((a1/2)-centroidxc)**2)))) + ((a2*(e2**3)/12)+(a2*e2*Math.abs((centroidxc-(e2/2))**2))) + ((e3*(a3**3)/12)+(a3*e3*((a3/2)-centroidxc)**2))
    let inerciapc = inerciaxc + inerciayc
    let rxc = Math.sqrt(inerciaxc/area)
    let ryc = Math.sqrt(inerciayc/area)
    let x0c = ((a1**2)+(a3**2))/(2*(a2+a1+a3))
    let y0c = ((a2**2)+(2*a1*a2))/(2*a2*(a1+a3))
    let cwc = (((a1-(e2/2))**3)*((a2+(e1/2)+(e3/2))**2)*e3*(2*((a2+(e1/2)+(e3/2))*e2)+(3*(a1+(e2/2))*e3)))/(12*((a2+(e1/2)+(e3/2))*e2)+(6*(a1+(e2/2))*e3))


    if (a1 == a3) {
        document.getElementById("cwc").innerHTML = 'La constante de alabeo es:      ' + cwc + ' cm6'
    }
    else {
        alert("Le notificamos que no es posible con esta herramienta obtener la constante de alabeo considerando que las dimensones de las alas difieren.")
    }
    
    document.getElementById("areabrutc").innerHTML = 'El valor del área bruta es:   '  + area + '  cm2'
    document.getElementById("centroidxc").innerHTML = 'El centroide en X es:    ' + centroidxc + '  cm'
    document.getElementById("centroidyc").innerHTML = 'El centroide en Y es:    ' + centroidyc + '  cm'
    document.getElementById("inerciaxc").innerHTML = 'La inercia en X es:   ' + inerciaxc + '  cm4'
    document.getElementById("inerciayc").innerHTML = 'La inercia en Y es:   ' + inerciayc + '  cm4'
    document.getElementById("inerciapc").innerHTML = 'La inercia polar J es:    ' + inerciapc + '  cm4'
    document.getElementById("rxc").innerHTML = 'El radio de giro rx es:     ' + rxc + '  cm'
    document.getElementById("ryc").innerHTML = 'El radio de giro ry es:     ' + ryc + '  cm'
    document.getElementById("x0c").innerHTML = 'El radio de giro x0c es:     ' +  x0c + '  cm'
    document.getElementById("y0c").innerHTML = 'El radio de giro y0c es:     ' + y0c + '  cm'

}

function seccionl() {
    let a1l = parseFloat(document.getElementById('a1l').value);
    let a2l = parseFloat(document.getElementById('a2l').value);
    let e1l = parseFloat(document.getElementById('e1l').value);
    let e2l = parseFloat(document.getElementById('e2l').value);

    let area = ((a1l)*(e2l))+((a1l)*(e2l))
    let centroidxl = ((e1l/2*a1l*e1l)+(a2l/2*e2l*a2l))/area
    let centroidyl = (((e2l+(a1l/2))*a1l*e1l)+((e2l/2)*a2l*e2l))/area
    let inerciaxl = (((e1l*(a1l**3)/12))+(a1l*e1l*Math.abs((((a1l/2)-centroidyl)**2)))) + ((a2l*(e2l**3)/12)+(a2l*e2l*Math.abs((centroidyl-(e2l/2))**2)))
    let inerciayl = (((a1l*(e1l**3)/12))+(a1l*e1l*Math.abs(((centroidxl-(e1l/2))**2)))) + ((e2l*(a2l**3)/12)+(a2l*e2l*Math.abs(((a2l/2)-centroidxl)**2)))
    let inerciapl = inerciaxl + inerciayl
    let rxl = Math.sqrt(inerciaxl/area)
    let ryl = Math.sqrt(inerciayl/area)
    let x0l = e1l/2
    let y0l = e2l/2
    let cwl = ((e1l**3)*(((a1l+(e2l/2))**3)+((a2l+(e1l/2))**3)))/36
    
    if (e1l == e2l) {
        document.getElementById("cwl").innerHTML = 'La constante de alabeo es:      ' + cwl + ' cm6'
    }
    else {
        alert("No es posible calcular la constante de alabeo, Procure e1 sea igual a e2. Para perfiles I cuyos espesores de alas difieren utilice otra herramienta.")
    }

    document.getElementById("areabrutl").innerHTML = 'El valor del área bruta es:   '  + area + '  cm2'
    document.getElementById("centroidxl").innerHTML = 'El centroide en X es:    ' + centroidxl + '  cm'
    document.getElementById("centroidyl").innerHTML = 'El centroide en Y es:    ' + centroidyl + '  cm'
    document.getElementById("inerciaxl").innerHTML = 'La inercia en X es:   ' + inerciaxl + '  cm4'
    document.getElementById("inerciayl").innerHTML = 'La inercia en Y es:   ' + inerciayl + '  cm4'
    document.getElementById("inerciapl").innerHTML = 'La inercia polar J es:    ' + inerciapl + '  cm4'
    document.getElementById("rxl").innerHTML = 'El radio de giro rx es:     ' + rxl + '  cm'
    document.getElementById("ryl").innerHTML = 'El radio de giro ry es:     ' + ryl + '  cm'
    document.getElementById("ryc").innerHTML = 'El radio de giro ry es:     ' + ryc + '  cm'
    document.getElementById("x0l").innerHTML = 'La coordenada x0c es:     ' +  x0l + '  cm'
    document.getElementById("y0l").innerHTML = 'La coordenada y0c es:     ' + y0l + '  cm'
    
}

function seccioncuad() {
    let a1cuad = parseFloat(document.getElementById('a1cuad').value);
    let a2cuad = parseFloat(document.getElementById('a2cuad').value);
    let b1cuad = parseFloat(document.getElementById('b1cuad').value);
    let b2cuad = parseFloat(document.getElementById('b2cuad').value);

    let area = (a2cuad*b2cuad)-(a1cuad*b1cuad)
    let centroidxcuad = b2cuad/2
    let centroidycuad = a2cuad/2
    let inerciaxcuad = ((b2cuad*(a2cuad*3))/12)-((b1cuad*(a1cuad*3))/12)
    let inerciaycuad = ((a2cuad*(b2cuad*3))/12)-((a1cuad*(b1cuad*3))/12)
    let inerciapcuad = inerciaxcuad + inerciaycuad
    let rxcuad = Math.sqrt(inerciaxcuad/area)
    let rycuad = Math.sqrt(inerciaycuad/area)

    document.getElementById("areabrutcuadhuec").innerHTML = 'El valor del área bruta es:   '  + area + '  cm2'
    document.getElementById("centroidxcuad").innerHTML = 'El centroide en X es:    ' + centroidxcuad + '  cm'
    document.getElementById("centroidycuad").innerHTML = 'El centroide en Y es:    ' + centroidycuad + '  cm'
    document.getElementById("inerciaxcuad").innerHTML = 'La inercia en X es:   ' + inerciaxcuad + '  cm4'
    document.getElementById("inerciaycuad").innerHTML = 'La inercia en Y es:   ' + inerciaycuad + '  cm4'
    document.getElementById("inerciapcuad").innerHTML = 'La inercia polar J es:    ' + inerciapcuad + '  cm4'
    document.getElementById("rxcuad").innerHTML = 'El radio de giro rx es:     ' + rxcuad + '  cm'
    document.getElementById("rycuad").innerHTML = 'El radio de giro ry es:     ' + rycuad + '  cm'
}
function secciont() {
    let bft = parseFloat(document.getElementById('bft').value);
    let hwt = parseFloat(document.getElementById('hwt').value);
    let tft = parseFloat(document.getElementById('tft').value);
    let twt = parseFloat(document.getElementById('twt').value);

    let area = (bft*tft)+(twt*hwt) 
    let centroidxt = (bft*0.5)
    let centroidyt = (((hwt/2)*(twt*hwt))+((hwt+(tft/2))*(bft*tft)))/area
    let inerciaxt = (((bft*(tft**3)/12))+(bft*tft*Math.abs(((hwt+tft)-centroidyt-(tft/2))**2))) + ((twt*(hwt**3)/12)+(hwt*twt*Math.abs(((centroidyt-(hwt/2))**2))))
    let inerciayt = (tft*(bft**3)/12) + (hwt*(twt**3)/12)
    let inerciapt = inerciaxt + inerciayt
    let rxt = Math.sqrt(inerciaxt/area)
    let ryt = Math.sqrt(inerciayt/area)
    let x0t = bft/2
    let y0t = hwt + (tft/2)
    let cwt = (((tft**3)*(bft**3))/144) + (((twt**3)*(hwt**3))/36)

    document.getElementById("areabrutt").innerHTML = 'El valor del área bruta es:   '  + area + '  cm2'
    document.getElementById("centroidxt").innerHTML = 'El centroide en X es:    ' + centroidxt + '  cm'
    document.getElementById("centroidyt").innerHTML = 'El centroide en Y es:    ' + centroidyt + '  cm'
    document.getElementById("inerciaxt").innerHTML = 'La inercia en X es:   ' + inerciaxt + '  cm4'
    document.getElementById("inerciayt").innerHTML = 'La inercia en Y es:   ' + inerciayt + '  cm4'
    document.getElementById("inerciapt").innerHTML = 'La inercia polar J es:    ' + inerciapt + '  cm4'
    document.getElementById("rxt").innerHTML = 'El radio de giro rx es:     ' + rxt + '  cm'
    document.getElementById("ryt").innerHTML = 'El radio de giro ry es:     ' + ryt + '  cm'
    document.getElementById("x0t").innerHTML = 'La coordenada x0t es:     ' +  x0t + '  cm'
    document.getElementById("y0t").innerHTML = 'La coordenada y0t es:     ' + y0t + '  cm'
    document.getElementById("cwt").innerHTML = 'La constante de alabeo es:      ' + cwt + ' cm6'
}

function seccionohuec() {
    let d1o = parseFloat(document.getElementById('d1o').value);
    let d2o = parseFloat(document.getElementById('d2o').value);

    let area = (Math.PI*(d2o**2)*0.25)-(Math.PI*(d1o**2)*0.25)
    let centroidxohuec = d2o/2
    let centroidyohuec = d2o/2
    let inerciaxohuec = Math.PI*((d2o/2)**4)*0.25 - Math.PI*((d1o/2)**4)*0.25
    let inerciayohuec = Math.PI*((d2o/2)**4)*0.25 - Math.PI*((d1o/2)**4)*0.25
    let inerciapohuec = inerciaxohuec + inerciayohuec
    let rxohuec = Math.sqrt(inerciaxohuec/area)
    let ryohuec = Math.sqrt(inerciayohuec/area)

    document.getElementById("areabrutohuec").innerHTML = 'El valor del área bruta es:   '  + area
    document.getElementById("centroidxohuec").innerHTML = 'El centroide en X es:    ' + centroidxohuec + '  cm'
    document.getElementById("centroidyohuec").innerHTML = 'El centroide en Y es:    ' + centroidyohuec + '  cm'
    document.getElementById("inerciaxohuec").innerHTML = 'La inercia en X es:   ' + inerciaxohuec + '  cm4'
    document.getElementById("inerciayohuec").innerHTML = 'La inercia en Y es:   ' + inerciayohuec + '  cm4'
    document.getElementById("inerciapohuec").innerHTML = 'La inercia polar J es:    ' + inerciapohuec + '  cm4'
    document.getElementById("rxohuec").innerHTML = 'El radio de giro rx es:     ' + rxohuec + '  cm'
    document.getElementById("ryohuec").innerHTML = 'El radio de giro ry es:     ' + ryohuec + '  cm'
}

function secciono() {
    let doo = parseFloat(document.getElementById('doo').value);

    let area = Math.PI*(doo**2)*0.25
    let centroidxoo = doo/2
    let centroidyoo = doo/2
    let inerciaxoo = Math.PI*((doo/2)**4)*0.25
    let inerciayoo = Math.PI*((doo/2)**4)*0.25
    let inerciapoo = inerciaxoo + inerciayoo
    let rxoo = Math.sqrt(inerciaxoo/area)
    let ryoo = Math.sqrt(inerciayoo/area)

    document.getElementById("areabrutoo").innerHTML = 'El valor del área bruta es:   '  + area + '  cm2'
    document.getElementById("centroidxoo").innerHTML = 'El centroide en X es:    ' + centroidxoo + '  cm'
    document.getElementById("centroidyoo").innerHTML = 'El centroide en Y es:    ' + centroidyoo + '  cm'
    document.getElementById("inerciaxoo").innerHTML = 'La inercia en X es:   ' + inerciaxoo + '  cm4'
    document.getElementById("inerciayoo").innerHTML = 'La inercia en Y es:   ' + inerciayoo + '  cm4'
    document.getElementById("inerciapoo").innerHTML = 'La inercia polar J es:    ' + inerciapoo + '  cm4'
    document.getElementById("rxoo").innerHTML = 'El radio de giro rx es:     ' + rxoo + '  cm'
    document.getElementById("ryoo").innerHTML = 'El radio de giro ry es:     ' + ryoo + '  cm'
}
function seccionrec() {
    let a = parseFloat(document.getElementById('a').value);
    let b = parseFloat(document.getElementById('b').value);

    let area = a*b
    let centroidxrectan = b*0.5
    let centroidyrectan = a*0.5
    let inerciaxrectan = b*(a**3)/12
    let inerciayrectan = a*(b**3)/12
    let inerciaprectan = inerciaxrectan + inerciayrectan
    let rxrectan = Math.sqrt(inerciaxrectan/area)
    let ryrectan = Math.sqrt(inerciayrectan/area)

    document.getElementById("areabrutrectan").innerHTML = 'El valor del área bruta es:   '  + area + '  cm2'
    document.getElementById("centroidxrectan").innerHTML = 'El centroide en X es:    ' + centroidxrectan + '  cm'
    document.getElementById("centroidyrectan").innerHTML = 'El centroide en Y es:    ' + centroidyrectan + '  cm'
    document.getElementById("inerciaxrectan").innerHTML = 'La inercia en X es:   ' + inerciaxrectan + '  cm4'
    document.getElementById("inerciayrectan").innerHTML = 'La inercia en Y es:   ' + inerciayrectan + '  cm4'
    document.getElementById("inerciaprectan").innerHTML = 'La inercia polar J es:    ' + inerciaprectan + '  cm4'
    document.getElementById("rxrectan").innerHTML = 'El radio de giro rx es:     ' + rxrectan + '  cm'
    document.getElementById("ryrectan").innerHTML = 'El radio de giro ry es:     ' + ryrectan + '  cm'
}

function e3() {

    let area = parseFloat(document.getElementById("areabruta").value);
    let ry = parseFloat(document.getElementById("ry").value);
    let K = parseFloat(document.getElementById("K").value);
    let L = parseFloat(document.getElementById("L").value);

    let fe = (((Math.PI)**2)*E)/((K*L/ry)**2)
    if (((K*L)/ry)>(4.71*Math.sqrt(E/fy)) || (fy/fe)>2.25) {
        var e3Fcr = 0.877*fe
        var e3Pn = e3Fcr*area
        var e3phiPn = 0.9*e3Pn
    } 
    else if (((K*L)/ry)<=(4.71*Math.sqrt(E/fy))) {
        var e3Fcr = (0.658**(fy/fe))*fy
        var e3Pn = e3Fcr*area
        var e3phiPn = 0.9*e3Pn
    }

    document.getElementById("e3Fcr").innerHTML = 'El Fcr es:    ' + e3Fcr + '   kg/cm2'
    document.getElementById("e3Pn").innerHTML = 'El Pn es:      ' + e3Pn + '    kg'
    document.getElementById("e3phiPn").innerHTML = 'El phiPn es:    ' + e3phiPn + '     kg'
}



function e4() {

    //Kx,Ky,Kz,G,J,rx,ry,K,L,r,Ag,E,fy,In

    if (cso==='a') {

        var h0 = float(input('Especifique h0, la distancia entre centroides de las alas: '))
        var Cw = (Iy*(h0**2))/4
        var Lz = float(input('Especifique Lz de la seccion (cm): '))
        var Kz = 1 //float(input('Especifique Kz de la seccion: '))
        var Fe = ((((Math.pi**2)*E*Cw)/((Kz*Lz)**2))+(G*J))/(Ix+Iy)

        if (((K*L)/r)>(4.71*Math.sqrt(E/fy)) || (fy/Fe)>2.25) {
            var e4Fcr = 0.877*Fe
        }
        else if (((K*L)/r)<=(4.71*Math.sqrt(E/fy))) {
            var e4Fcr = (0.658**(fy/Fe))*fy
            var e4Pn=e4Fcr*Ag
            var e4phiPn=0.9*e4Pn
        }
    }
    else if (cso==='b') {

        var x0 = 18 //float(input('Especifique x0 (cm): '))
        var y0 = 12 //float(input('Especifique y0 (cm): '))
        var Cw = float(input('Especifique Cw (cm6): '))
        var Lz = float(input('Especifique Lz de la seccion (cm): '))
        var Ly = float(input('Especifique Ly de la seccion (cm): '))
        var r0 = Math.sqrt((x0**2)+(y0**2)+((Ix+Iy)/Ag))
        var H = 1-(((x0**2)+(y0**2))/(r0**2))
        var Fey = (((Math.pi)**2)*E)/((Ky*Ly/ry)**2)
        var Fez = ((((Math.pi**2)*E*Cw)/((Kz*Lz)**2))+(G*J))/(Ag*(r0**2))
        var Fe = ((Fey+Fez)/(2*H))*(1-(Math.sqrt(1-((4*Fey*Fez*H)/((Fey+Fez)**2)))))

        if (((K*L)/r)>(4.71*Math.sqrt(E/fy)) || (fy/Fe)>2.25) {
            var e4Fcr = 0.877*Fe
        }
        else if (((K*L)/r)<=(4.71*Math.sqrt(E/fy))) {
            var e4Fcr = (0.658**(fy/Fe))*fy
            var e4Pn = e4Fcr*Ag
            var e4phiPn = 0.9*e4Pn
        }
    }
    else if (cso==='c') {
        var x0 = 18 //float(input('Especifique x0 (cm): '))
        var y0 = 12 //float(input('Especifique y0 (cm): '))
        var r0 = Math.sqrt((x0**2)+(y0**2)+((Ix+Iy)/Ag))
        var H = 1-(((x0**2)+(y0**2))/(r0**2))
        var Cw = float(input('Especifique Cw (cm6): '))
        var Lx = float(input('Especifique Lx de la seccion (cm): '))
        var Ly = float(input('Especifique Ly de la seccion (cm): '))
        var Lz = float(input('Especifique Lz de la seccion (cm): '))
        var Fex = (((Math.pi)**2)*E)/((Kx*Lx/rx)**2)
        var Fey = (((Math.pi)**2)*E)/((Ky*Ly/ry)**2)
        var Fez = ((((Math.pi**2)*E*Cw)/((Kz*Lz)**2))+(G*J))/(Ag*(r0**2))
        var a1 = 1-((x0**2)/(r0**2))-((y0**2)/(r0**2))
        var b1 = Fex+Fey+Fez+((Fey*(x0**2))/(r0**2))+((Fey*(y0**2))/(r0**2))
        var c1 = (Fey*Fez)+(Fex*Fez)
        var d1 = (Fex*Fey*Fez)
        var coeff = [a1, -b1, c1, -d1]
        var Fe = Math.amin(Math.roots(coeff))

        if (((K*L)/r)>(4.71*Math.sqrt(E/fy)) || (fy/Fe)>2.25) {
            var e4Fcr = 0.877*Fe
        }
        else if (((K*L)/r)<=(4.71*Math.sqrt(E/fy))) {
            var e4Fcr = (0.658**(fy/Fe))*fy
            var e4Pn = e4Fcr*Ag
            var e4phiPn = 0.9*e4Pn
            return e4Pn, e4phiPn, e4Fcr
        }
    }
}


// function E7(Fcr,fy,E,D,t,Ag,c,lmb,lmbr,b) {

//     if (c == 9) {

//         if ((D/t) <= (0.11*(E/fy))) {
//             Ae=Ag
//         }
//         else if ((0.11*(E/fy))<(D/t) && (D/t)<(0.45*(E/fy))) {
//             Ae=(((0.038*E)/(fy*(D/t)))+(2/3))*Ag
//         }
//         ePn=Fcr*Ae
//         ephiPn=0.9*ePn
//         print('Los siguientes valores consideran el Area efectiva debido a p&&eo local')
//         print(ePn)
//         print(ephiPn)

//     }
//     else {
//         if (c==5 || c==7 || c==8 || c==9) {
//             c1=0.18
//         }
//         else if (c==6) {
//             c1=0.2
//         }
//         else {
//             c1= 0.22
//         }
        
//         c2=(1-(Math.sqrt(1-(4*c1))))/(2*c1)
//         Fel = ((c2*(lmbr/lmb))**2)*fy

//         if (lmb<=lmbr*(Math.sqrt(fy/Fcr))) {
//             be=b
//         }
//         else if (lmb>(lmbr*Math.sqrt(fy/Fcr))) {
//             be=b*(1-(c1*Math.sqrt(Fel/Fcr)))*(Math.sqrt(Fel/Fcr))
//             Ae=(b-be)*t
//             ePn=Fcr*Ae
//             ephiPn=0.9*ePn
//             print('Los siguientes valores consideran el Area efectiva debido a p&&eo local')
//             print(ePn)
//             print(ephiPn)
//         }
//     }
        
// }