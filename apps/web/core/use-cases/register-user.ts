import { IAuthRepository } from "../interfaces/auth-repository.interface";
import { AuthResponse } from "../entities/user";

export class RegisterUser {
    constructor(private authRepository: IAuthRepository) { }

    async execute(email: string, password: string, fullName: string): Promise<AuthResponse> {
        if (!email || !password || !fullName) {
            throw new Error("All fields are required");
        }
        return this.authRepository.register(email, password, fullName);
    }
}
