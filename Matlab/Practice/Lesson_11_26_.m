A=[];
A=[A 1 1];
for n = 10
    for i = 3:1:n
        a = A(i-2) + A(i-1);
        A = [A a];
    end
end
disp(A)
%
%
Pnum = [];
for i = 1:1:1001
    flg1 = 0;
    for n = 1:1:i
        if mod(i,n)==0
            continue
        else
            flg1 = 1;
        end
    end
    if flg1 == 0
        Pnum = [Pnum i];
    end
end
disp(Pnum)