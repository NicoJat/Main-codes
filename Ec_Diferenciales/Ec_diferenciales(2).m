clear all
close all
clc

syms x y
f=input('Ingresar funcion a evaluar (x minuscula y comillas simples) despejando dy/dx: \n');
f=inline(f);
h=input('Ingresar valor del tamano de paso: \n');
x1=input('Ingresar valor de x dado: \n');
y1=input('Ingresar valor de y dado: \n');
y=y1
x=0;
format long
k1=f(x1,y1);
x2=x1+(h*0.5);
y2=y1+(0.5*h*k1);
format long
k2=f(x2,y2);
x3=x1+(h*0.5);
y3=y1+(0.5*h*k2);
format long
k3=f(x3,y3);
i=0;
x4=x1+h;
y4=y1+(k3*h);
format long
k4=f(x4,y4);
r=((k1+(2*k2)+(2*k3)+k4)*(h/6));

while 1
    format long
    y=y+r
    x=x+h;
    i=i+1;
    if i==5
        break
    end
end
