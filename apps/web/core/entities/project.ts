import { User } from "./user";

export interface Project {
    id: string;
    name: string;
    api_key: string;
    discord_webhook_url?: string;
    user?: User;
    created_at: string;
    updated_at: string;
}
