import { IProjectRepository } from "@/core/interfaces/project-repository.interface";
import { Project } from "@/core/entities/project";
import { apiClient } from "@/infrastructure/api-client";

export class ApiProjectRepository implements IProjectRepository {
    async create(name: string, discordWebhookUrl?: string): Promise<Project> {
        const response = await apiClient.post<Project>("/projects", {
            name,
            discord_webhook_url: discordWebhookUrl,
        });
        return response.data;
    }

    async getAll(): Promise<Project[]> {
        const response = await apiClient.get<Project[]>("/projects");
        return response.data;
    }
}
