namespace CeeBee.Models
{
    public class Data
    {
        public List<string> SelectedNames { get; set; }

        public bool ShowPseudo { get; set; }

        public string TextInput { get; set; }

        public float DurationSec { get; set; }

        public float DurationMs { get; set; }

        public IFormFile File { get; set; }
    }
}