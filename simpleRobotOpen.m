clc
clear all;
fprintf('Connecting to robot...');
s = serialport('COM6', 19200, "Timeout", 15);
pause(1.5);   % short pause to allow your computer to connect to Serial port
writeline(s, 'INITIALIZE');
readline(s)
fprintf('Ready\n');
