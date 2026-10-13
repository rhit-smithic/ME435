clc
clear

ptAOnLink1 = [0; 0; 2; 1]; %the 4th dimension is index (?)
ptBOnLink2 = [1; 0; 1; 1];

% Building the Transoformation Matrices - By Inspection
A1 = create_A_matrix(2, 3, 0, 0); %A is how much it moved in the x, z, alpha, theta
A2 = create_A_matrix(3, 0, 0, 0); %from 1 to 2 origin

T0_1 = A1; %T goes back to 0
T0_2 = A1 * A2;

% DH
actualAPtOnLink0 = T0_1 * ptAOnLink1;
actualBPtOnLink0 = T0_2 * ptBOnLink2;

% Determine A and B on the base frame
expecetedPtAOnLink0 = [2; 0; 5; 1];
expecetedPtBOnLink0 = [6; 0; 4; 1];