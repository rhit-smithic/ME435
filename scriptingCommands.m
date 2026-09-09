writeline(s,'X-AXIS 5')      % Send command #n
readline(s);   % Get response to command #n
writeline(s,'GRIPPER OPEN'); % Send command #n+1
readline(s);   % Get response to command #n+1

for i = 1:5
  writeline(s,'Z-AXIS EXTEND');
  readline(s);
  writeline(s,'Z-AXIS RETRACT');
  readline(s);
end
