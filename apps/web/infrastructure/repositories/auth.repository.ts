import { IAuthRepository } from "@/core/interfaces/auth-repository.interface";
import { AuthResponse } from "@/core/entities/user";
import { apiClient } from "@/infrastructure/api-client";

export class ApiAuthRepository implements IAuthRepository {
    async login(email: string, password: string): Promise<AuthResponse> {
        const response = await apiClient.post<AuthResponse>("/auth/login", {
            email,
            password,
        });
        return response.data;
    }

    async register(email: string, password: string, fullName: string): Promise<AuthResponse> {
        const response = await apiClient.post<AuthResponse>("/auth/register", {
            email,
            password,
            fullName,
        });
        return response.data;
    }
}
