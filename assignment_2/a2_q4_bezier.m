function [] = bezier()
    % N*2 matrix containing 'N' control points [x1 y1;...;xN yN]
    V = input('Enter 4 Control Points:');
    N = size(V, 1);         % Number of control points
    
    % In our case, check that N = 4
    if (N ~= 4)
        disp('Number of control points not equal to 4. Exitting...');
        return;
    end
    
    num_pts = 100;          % Number of points to be used to plot the Bezier Curve
    t = (0:1/num_pts:1);    % Array of values of parameter 't' for plotting the curve
    
    M_B = [1 -3 3 -1; 0 3 -6 3; 0 0 3 -3; 0 0 0 1];  % Hermite matrix equivalent for Bezier Curve with 4 Control Points
    T = [t.^3; t.^2; t; t.^0]';                     % Parameter Matrix
    
    B = T * M_B * V;                                % Points on the Bezier Curve can be obtained using B(t) = [t][M_B][V]
    
    
    % Plot the Control Polygon
    plot(V(:,1), V(:,2), 'Marker', 'o', 'LineWidth', 2, 'DisplayName', 'Control Polygon');
    hold on;
    
    % Plot the Bezier Curve
    plot(B(:, 1), B(:, 2), 'LineWidth', 2, 'DisplayName', 'Bezier Curve');
    hold off; 
    
    legend;
end