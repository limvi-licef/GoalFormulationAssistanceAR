using System;
using StereoKit;

using UdpSockets;
using UdpCameras;

namespace ContextualAssistanceV2
{
    class Program
    {

        static DisplayUdpSocket socket;
        static UdpFRCamera camera;

        static void Main(string[] args)
        {
            // Initialize StereoKit
            StereoKitApp.settings.assetsFolder = "Assets";
            if (!StereoKitApp.Initialize("ContextualAssistanceV2", Runtime.MixedReality)) Environment.Exit(1);

            camera = new UdpFRCamera();
            _ = camera.Start();

            socket = new DisplayUdpSocket();
            socket.OnReceivedDisplayCommand += Program.OnReceivedDisplayCommand;

            _ = camera.Connect("172.22.192.1", "9999");
            _ = socket.Connect("172.22.192.1", "9998");

            // Core application loop
            while (StereoKitApp.Step(() =>
            {

            })) ;
            StereoKitApp.Shutdown();
        }

        private static void OnReceivedDisplayCommand(string cmd, string[] args)
        {
            if (cmd == "Text")
            {
                // parse data
                var text = args[0];
                var x = float.Parse(args[1]);
                var y = float.Parse(args[2]);
                var z = float.Parse(args[3]);

            }
            else if (cmd == "Speak")
            {

            }
            else if (cmd == "del")
            {

            }
        }
    }
}
