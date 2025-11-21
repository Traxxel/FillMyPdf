using WWW.blazor.Models;

namespace WWW.blazor.Services;

public class ProjectService
{
    private readonly List<Project> _projects = new();

    public List<Project> GetAllProjects()
    {
        return _projects;
    }

    public Project? GetProject(Guid id)
    {
        return _projects.FirstOrDefault(p => p.Id == id);
    }

    public Project CreateProject(string name, string description)
    {
        var project = new Project
        {
            Name = name,
            Description = description
        };
        _projects.Add(project);
        return project;
    }

    public void DeleteProject(Guid id)
    {
        var project = _projects.FirstOrDefault(p => p.Id == id);
        if (project != null)
        {
            _projects.Remove(project);
        }
    }

    public void AddInputFile(Guid projectId, string fileName, string filePath, long fileSize)
    {
        var project = GetProject(projectId);
        if (project != null)
        {
            project.InputFiles.Add(new InputFile
            {
                FileName = fileName,
                FilePath = filePath,
                FileSize = fileSize
            });
        }
    }

    public void SetOutputFile(Guid projectId, string fileName, string filePath, long fileSize)
    {
        var project = GetProject(projectId);
        if (project != null)
        {
            project.OutputFile = new OutputFile
            {
                FileName = fileName,
                FilePath = filePath,
                FileSize = fileSize
            };
        }
    }
}
