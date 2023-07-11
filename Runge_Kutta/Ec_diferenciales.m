clear all
clc

x1=1;
x2=2;
h=input('Ingresar valor del tamano de paso: \n');
x=floor((x2-x1)/h);
y=input('Ingresar valor de y dado: \n');
dy=zeros(x,1);
dx=zeros(x,1);


for i=1:x+1
    dx(i)=x1+(i-1)*h;
    if i==1
        dy(i)=y;
    else
        y=dy(i-1);
        x=dx(i-1);
        
        k1=(y/x)-(y/x).^2
        k2=((y+(0.5*k1*h))/(x+(0.5*h)))-((y+(0.5*h))/(x+(0.5*h))).^2
        k3=((y-(k1*h+2*k2*h))/(x+h))-((y-(k1*h+2*k2*h))/(x+h)).^2
        
        y=y+((k1+4*k2+k3)/6)*h
        dy(i)=y;
    end
end
plot(dx,dy,'-b.')
