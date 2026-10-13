classdef BuiltinLEDFrontend < hgsetget
    %Controls the Built-in LED through the Pi Flask server

    properties
        count
        period
    end

    methods
        function obj = BuiltinLEDFrontend()
            obj.count = 0;
            obj.period = 0;
        end

        function response = on(obj)
            onCommand = sprintf('LED ON');
            response = obj.sendCommand(onCommand);
        end

        function response = off(obj)
            offCommand = sprintf('LED OFF');
            response = obj.sendCommand(offCommand);
        end

        function response = flash(obj,count,period)
            flashCommand = sprintf('FLASH %d %d',count,period);
            response = obj.sendCommand(flashCommand);
        end

    end

    methods (Access = private)
        function response = sendCommand(obj,command)
            import matlab.net.*
            import matlab.net.http.*

            r = RequestMessage;
            uri = URI("http://127.0.0.1:5000/api/" + command);
            resp = send(r,uri);
            response = resp.Body.Data;
        end
    end
end
