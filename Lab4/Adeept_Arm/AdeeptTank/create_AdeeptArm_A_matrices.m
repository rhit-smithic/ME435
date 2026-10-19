function [A1, A2, A3] = create_AdeeptArm_A_matrices(jointAngles)
% Create the A matrices for the arm.

a = [64, 0, 0];
d = [0, 0, 140];
alpha = [0, -90, 0];

A1 = create_A_matrix(a(1), d(1), alpha(1), jointAngles(1));
A2 = create_A_matrix(a(2), d(2), alpha(2), jointAngles(2));
A3 = create_A_matrix(a(3), d(3), alpha(3), jointAngles(3));

end