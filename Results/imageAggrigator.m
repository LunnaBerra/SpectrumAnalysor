clc
clf
clear
i=0;

while true
    %filename = 'No GPS/test1_10min_0dBm_87cm_aborted/sample' + string(i) + '.csv';
    filename = 'Yepson/test1_3min_50dBm_87cm_låda_metall_externelektronik/sample' + string(i) + '.csv';
    %filename = 'Katt\test1_5min_50dBm_87cm/sample' + string(i) + '.csv';

    if isfile(filename)
        Array1 = csvread(filename,1,0);
        A1colx = Array1(:,1);
        A1coly = Array1(:,2);
        hold on
        plot(A1colx,A1coly)
        title('Linjegrafsamling av alla tester utan GPS-tag närvarande')
        xlabel('Hz')
        ylabel('dBm')
        i=i+1;
    else
        hold off
        break;
    end
end


