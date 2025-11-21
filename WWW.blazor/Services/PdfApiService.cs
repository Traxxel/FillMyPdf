using System.Net.Http.Json;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace WWW.blazor.Services;

public class PdfApiService
{
    private readonly HttpClient _httpClient;
    private readonly string _apiBaseUrl = "http://localhost:5003";

    public PdfApiService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<ProcessResponse?> ProcessPdfAsync(List<string> inputFiles, string formFile, string outputFile)
    {
        var request = new ProcessRequest
        {
            InputFiles = inputFiles,
            FormFile = formFile,
            OutputFile = outputFile
        };

        try
        {
            var response = await _httpClient.PostAsJsonAsync($"{_apiBaseUrl}/process", request);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadFromJsonAsync<ProcessResponse>();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error calling PDF API: {ex.Message}");
            return null;
        }
    }
}

public class ProcessRequest
{
    [JsonPropertyName("input_files")]
    public List<string> InputFiles { get; set; } = new();
    
    [JsonPropertyName("form_file")]
    public string FormFile { get; set; } = string.Empty;
    
    [JsonPropertyName("output_file")]
    public string OutputFile { get; set; } = string.Empty;
}

public class ProcessResponse
{
    [JsonPropertyName("status")]
    public string Status { get; set; } = string.Empty;
    
    [JsonPropertyName("output_file")]
    public string OutputFile { get; set; } = string.Empty;
    
    [JsonPropertyName("metadata")]
    public Dictionary<string, string> Metadata { get; set; } = new();
}

