%% USER DEFINED VALUES

A = [5 1 4 1 3 1 1 3 1 1 4 1 5 1 1 2 1 4 1 1 2 1 1 3 1 4 1 1];

E = 10^7*ones(21);

P = [10 5000 135;
    8 4000 270];

N_XY = [1  0     0   1 1;
        2  8    20   0 0;
        3  15   12.5 0 0;
        4  20   12.5 0 0;
        5  27   20   0 0;
        6  35    0   1 1;
        7  35   25   0 0;
        8  22.5 25   0 0;
        9  17.5 25   0 0;
        10 12.5 25   0 0;
        11  0   25   0 0]

SF = 75;

ID = [1 2;2 3;3 4;4 5;5 6;6 7;7 8;8 9;9 10;10 11; 11 1;2 11;2 10;
      3 10;3 9;4 9;4 8;5 8;5 7;1 3;4 6]

%Input does not need to be added below this point, but feel free to edit.

%% Stiffness Matrix
% Calculates stiffness matrix for each element, and sums them appropriatly
% into global stiffness matrix

k = LOCALkelement(N_XY,ID,A,E);
Nnode = size(N_XY,1);
Nelem = size(ID,1);

k_sum = zeros(2*Nnode);
IDn = zeros(Nelem,4);

for i=1:Nelem
    
    IDn(i,:) = [(ID(i,1)*2-1) ID(i,1)*2 (ID(i,2)*2-1) ID(i,2)*2] ;
    k_sum(IDn(i,:),IDn(i,:)) =  k_sum(IDn(i,:),IDn(i,:)) + k{i};
    
end


%% Nodal Loading
%Defines a global loading vector based on load vector P

P_sum = zeros(2*Nnode,1);

for i=1:size(P,1)
    
    P_sum(P(i,1)*2-1)=P(i,2)*cos(P(i,3)*pi/180);
    P_sum(P(i,1)*2)= P(i,2)*sin(P(i,3)*pi/180);
    
end

%% Apply Boundary Conditions
%Apply the boundary conditions by defining ID matrix for non-constrained values
%Redefine stiffness matrix, load vector, and displacement vector with ID

Nbc =sum(~N_XY,1);
IDf = zeros(Nbc(4)+Nbc(5),1);

for i  = 1:Nnode
    
    if N_XY(i,4)==0
        for q = 1: Nbc(4)+Nbc(5)
            
            if IDf(q)==0
                IDf(q)=N_XY(i,1)*2-1;
                break
            end
        end
    end
    
    if N_XY(i,5)==0
        for y = 1:Nbc(4)+Nbc(5)
            if IDf(y)==0
                IDf(y)=N_XY(i,1)*2;
                break
            end
        end
    end
    
end

k_disp = k_sum(IDf,IDf);
p_disp = P_sum(IDf);
u_disp = linsolve(k_disp,p_disp);

u_sum = zeros(2*(Nnode),1);
u_sum(IDf) = u_disp;

%% Reactions

R_sum = k_sum*u_sum-P_sum;

def_XY = [N_XY(:,2) N_XY(:,3)];
for i=1:2*Nnode
    
    if u_sum(i)~=0 && mod(i,2)==1
        def_XY((i/2)+.5,1) = N_XY((i/2)+.5,2)+SF*u_sum(i);
    end
    
    if u_sum(i)~=0 && mod(i,2)==0
        def_XY((i/2),2) = N_XY((i/2),3)+SF*u_sum(i)
    end
end

%% Force & Stress

[fe,stress] = LOCALforce(N_XY,ID,A,E,u_sum);

%% Plot Solutions
%Green indicates element in tension
%Red indicates element in compress
%Black nodes are constrained

for i=1:Nelem
    Afac = max(A);
    plot([N_XY(ID(i,1),2) N_XY(ID(i,2),2)],[N_XY(ID(i,1),3) N_XY(ID(i,2),3) ],'Color',[.50 .50 .60],'Linewidth',5)
    
    hold on
    
    if fe(i)>0
        plot([def_XY(ID(i,1),1) def_XY(ID(i,2),1)],[def_XY(ID(i,1),2) def_XY(ID(i,2),2)],'g-.','Linewidth',3)
    else
        plot([def_XY(ID(i,1),1) def_XY(ID(i,2),1)],[def_XY(ID(i,1),2) def_XY(ID(i,2),2)],'r-.','Linewidth',3)
    end
    title('Truss 2D')
    xlabel('X Global')
    ylabel('Y Global')
    hold on
    grid on
    text((N_XY(ID(i,1),2)+N_XY(ID(i,2),2))/2,((N_XY(ID(i,1),3)+N_XY(ID(i,2),3))/2),['E',num2str(i)],'Color','k','FontSize',15)
end

for i=1:Nnode
    if N_XY(i,4)==0 && N_XY(i,5)==0
        plot(N_XY(i,2),N_XY(i,3),'o','Color',[.50 .50 .60],'Linewidth',6)
        
    else
        plot(N_XY(i,2),N_XY(i,3),'ko','Linewidth',6)
    end
    
end


%% SUB-FUNCTION kelement

function k = LOCALkelement(N_XY,ID,A,E)

for i=1:size(ID,1)
    dx(i) = N_XY(ID(i,2),2)-N_XY(ID(i,1),2);
    dy(i) = N_XY(ID(i,2),3)-N_XY(ID(i,1),3);
    L(i) = (dx(i)^2+dy(i)^2)^.5;
    c(i) = dx(i)/L(i);
    s(i) = dy(i)/L(i);
    h = [-c(i);-s(i);c(i);s(i)];
    
    k{i} = (A(i)*E(i)/L(i))*h*h';
end

end

%% SUB-FUNCTION Force/Stress

function [fe,stress] = LOCALforce(N_XY,ID,A,E,u_sum)

for i=1:size(ID,1)
    dx(i) = N_XY(ID(i,2),2)-N_XY(ID(i,1),2);
    dy(i) = N_XY(ID(i,2),3)-N_XY(ID(i,1),3);
    L(i) = (dx(i)^2+dy(i)^2)^.5;
    c(i) = dx(i)/L(i);
    s(i) = dy(i)/L(i);
    h = [-c(i);-s(i);c(i);s(i)];
    
    fe(i) = (A(i)*E(i)/L(i))*h'*u_sum([ID(i,1)*2-1 ID(i,1)*2 ID(i,2)*2-1 ID(i,2)*2]);
    stress(i) = fe(i)/A(i);
end

end