Pnum = [];
for i = 1:1:1001
    flg1 = 0;
    flg2 = 0;
    if mod(i,3)==0
        flg1 = 1;
    end
    if mod(i,5)==0
        flg2 = 1;
    end
    if flg2 == flg1 && flg1 ==1
        Pnum = [Pnum i];
    end
end
disp(Pnum)
