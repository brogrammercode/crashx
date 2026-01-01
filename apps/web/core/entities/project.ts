import { User } from "./user";

export interface Project {
    id: string;
    name: string;
    apiKey: string;
    discordWebhookUrl?: string;
    user?: User;
    createdAt: string;
}
