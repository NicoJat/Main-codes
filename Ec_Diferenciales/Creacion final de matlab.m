clear all
close all
clc


 
display('1.Metodo Biseccion');
display('2.Metodo Newton');
display('3.Metodo Secante');
z=input('Escoja una opcion: \n');

switch z
    case 1

        %Biseccion
        disp('Ejecuto Biseccion');
        f=input('Ingresar funcion a evaluar (x minuscula y comillas simples): \n');
        f=inline(f);
        q=input('Ingresar primer valor: \n');
        w=input('ingresar segundo valor: \n');
        tol=0.00000001;
        s=abs(q-w)/0.5;
        x=linspace(q,w,s);

        for i=1:s-1
            if (f(x(i)))*f(x(i+1))<0
                a=x(i);
                b=x(i+1);
                xn=0;
                k=0;
                eps=abs(b-a);
                if (f(a)*f(b))<0
                    while (abs(b-a))/2>tol
                        xn=(a+b)/2;
                        eps=eps-(xn-a);
                        k=k+1;
                        fprintf('%d\t %f\t %f\n',k,xn,eps)
                        if (f(xn)*f(a))<=0
                            b=xn;
                        else
                            a=xn;
                        end
                    end
                end
            display(' ')
            end
        end


    case 2

        %Newton
        disp('Ejecuto Newton')
        f=input('Ingresar funcion a evaluar (x minuscula y comillas simples): \n');
        f=inline(f);
        tol=0.00000001;
        i=1;
        q=input('Ingresar primer valor: \n');
        w=input('ingresar segundo valor: \n');
        a=0.5;
        s=abs(q-w)/a;
        x=linspace(q,w,s);

        for i=1:s-1
            if (f(x(i)))*f(x(i+1))<0
                x(i);
                x(i+1);
                x0=(x(i)+x(i+1))/2;
                Deriv_ant=(f(x0+tol)-f(x0))/tol;
                eps=abs(x(i+1)-x(i));
                k=0;
                while 1
                    xn=x0-(f(x0)/Deriv_ant);
                    Deriv_ant=(f(x0+tol)-f(x0))/tol;
                    k=k+1;
                    eps=abs(xn-x0);
                    fprintf('%d\t %f\t %f\n',k,xn,eps)
                    if eps<=tol
                        break
                    end
                    x0=xn;
                end
                display(' ')
            end
        end



    case 3

        %Secante
        disp('Ejecuto Secante')
        f=input('Ingresar funcion a evaluar (x minuscula): \n');
        f=inline(f);
        q=input('Ingresar primer valor: \n');
        w=input('ingresar segundo valor: \n');
        s=abs(q-w)/0.1;
        x=linspace(q,w,s);
        for i=1:s-1
            if (f(x(i)))*f(x(i+1))<0
                a=x(i);
                b=x(i+1);
                xn=(b-f(b))*((b-a)/(f(b)-f(a)));
                tol=0.0000001;
                eps=abs(b-a);
                k=0;
                x0=0;
                if (f(a)*f(b))<0
                    while 1
                        xn=b-((f(b))*(b-xn))/(f(b)-f(xn));
                        k=k+1;
                        eps=abs(xn-x0);
                        fprintf('%d\t %f\t %f\n',k,xn,eps)
                        if eps<=tol
                            break
                        end
                        x0=xn;
                    end
                end
                display(' ')
            end    
        end

    otherwise
        disp('Opción equivocada')
    end
    
pause

