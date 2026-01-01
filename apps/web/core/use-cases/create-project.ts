import { IProjectRepository } from "../interfaces/project-repository.interface";
import { Project } from "../entities/project";

export class CreateProject {
    constructor(private projectRepository: IProjectRepository) { }

    async execute(name: string, discordWebhookUrl?: string): Promise<Project> {
        if (!name) {
            throw new Error("Project name is required");
        }
        return this.projectRepository.create(name, discordWebhookUrl);
    }
}
