using System;
using Microsoft.Azure.Devices;
using Newtonsoft.Json;
using System.Text;
using System.Configuration;

static ServiceClient serviceClient;
static string connectionString = "HostName=MyRaspRGHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=aXJPkb8sDrC4oj8+pyfy6MP1hv1Hx6VqbH9G1qxF6MU=";

public async static void Run(string myIoTHubMessage, TraceWriter log)
{
    log.Info($"C# IoT Hub trigger function processed a message: {myIoTHubMessage}");
    ServiceClient serviceClient = ServiceClient.CreateFromConnectionString(connectionString);

    var serviceMessage = new Microsoft.Azure.Devices.Message(Encoding.ASCII.GetBytes(myIoTHubMessage));
    serviceMessage.Ack = DeliveryAcknowledgement.Full;
    serviceMessage.MessageId = Guid.NewGuid().ToString();
    await serviceClient.SendAsync("RGRasp", serviceMessage);

    // Condition for calling the sendmsg
    // if (int(myIoTHubMessage) >= 40)
    // {
//         sendmsg("red");
//     }
//     else
//     {
//         sendmsg("green");
//     }
 }

// private async void sendmsg(string message)
// {
//     try
//     {
//         ServiceClient serviceClient = ServiceClient.CreateFromConnectionString(connectionString);

//         var serviceMessage = new Microsoft.Azure.Devices.Message(Encoding.ASCII.GetBytes(message));
//         serviceMessage.Ack = DeliveryAcknowledgement.Full;
//         serviceMessage.MessageId = Guid.NewGuid().ToString();

//         await serviceClient.SendAsync("RGRasp", serviceMessage);
//         await serviceClient.CloseAsync();

//     }
//     catch (Exception ex)
//     {
//     }
// }