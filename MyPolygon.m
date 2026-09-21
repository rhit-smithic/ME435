classdef MyPolygon < handle
    % handle is a subclass. in matlab, if you ever mutate an object of a
    % class, it copies it. but if you use a handle it'll be the same
    % object.

    properties
        Patch % tells what object patch is so it helps w/ autocomplete .
    end

    methods
        function obj = MyPolygon(xCoords, yCoords, color) %constructor
            obj.Patch = patch(xCoords, yCoords, color);
        end

        function move(obj, dx, dy) %method
            obj.Patch.XData = obj.Patch.XData + dx;
            obj.Patch.YData = obj.Patch.YData + dy;
        end
    end
end

% EVERY TIME YOU MODIFY CLASS, type clear in the command window first to
% get rid of all current instances of class