import { AuthResponse } from "@/core/entities/user";

export interface IAuthRepository {
    login(email: string, password: string): Promise<AuthResponse>;
    register(email: string, password: string, fullName: string): Promise<AuthResponse>;
}
