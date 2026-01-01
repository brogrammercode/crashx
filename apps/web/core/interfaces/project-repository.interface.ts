import { Project } from "../entities/project";

export interface IProjectRepository {
    create(name: string, discordWebhookUrl?: string): Promise<Project>;
    getAll(): Promise<Project[]>;
}
