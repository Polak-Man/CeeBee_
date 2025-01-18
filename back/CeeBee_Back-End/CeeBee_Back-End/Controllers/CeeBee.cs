using CeeBee.Models;
using Microsoft.AspNetCore.Mvc;
using System.IO;
using System.Net.Sockets;
using System.Text;
using Newtonsoft.Json;

namespace CeeBee.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CeeBeeController : ControllerBase
    {
        [HttpPost]
        public IActionResult PostData([FromForm] Data data)
        {
            // V�rifiez si un fichier a �t� t�l�charg�
            if (data.File != null && data.File.Length > 0)
            {
                // D�finir le chemin de stockage
                var uploadsFolder = Path.Combine(Directory.GetCurrentDirectory(), "uploads");
                Directory.CreateDirectory(uploadsFolder); // Cr�ez le dossier s'il n'existe pas

                // Cr�er un nom de fichier unique
                var fileName = Path.GetFileName(data.File.FileName);
                var filePath = Path.Combine(uploadsFolder, fileName);

                // Enregistrer le fichier
                using (var stream = new FileStream(filePath, FileMode.Create))
                {
                    data.File.CopyTo(stream);
                }

                // Envoyer les donn�es au serveur Python via socket
                using (var client = new TcpClient("localhost", 5000)) // Connectez-vous au serveur Python
                {
                    var jsonData = JsonConvert.SerializeObject(data); // Utilisez JsonConvert ici
                    var dataToSend = Encoding.UTF8.GetBytes(jsonData);
                    var stream = client.GetStream();
                    stream.Write(dataToSend, 0, dataToSend.Length);
                }
            }

            return Ok(new { message = "Donn�es re�ues avec succ�s." });
        }
    }
}