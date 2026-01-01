import { IAuthRepository } from "../interfaces/auth-repository.interface";
import { AuthResponse } from "../entities/user";

export class LoginUser {
    constructor(private authRepository: IAuthRepository) { }

    async execute(email: string, password: string): Promise<AuthResponse> {
        if (!email || !password) {
            throw new Error("Email and password are required");
        }
        return this.authRepository.login(email, password);
    }
}
