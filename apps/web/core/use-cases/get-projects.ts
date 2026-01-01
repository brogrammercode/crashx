import { IProjectRepository } from "../interfaces/project-repository.interface";
import { Project } from "../entities/project";

export class GetProjects {
    constructor(private projectRepository: IProjectRepository) { }

    async execute(): Promise<Project[]> {
        return this.projectRepository.getAll();
    }
}
