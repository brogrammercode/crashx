package com.crashx.api.services;

import com.crashx.api.models.Project;
import com.crashx.api.models.User;
import com.crashx.api.repositories.ProjectRepository;
import com.crashx.api.repositories.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.security.SecureRandom;
import java.util.Base64;
import java.util.List;
import java.util.UUID;

@Service
@RequiredArgsConstructor
public class ProjectService {

    private final ProjectRepository projectRepository;
    private final UserRepository userRepository;

    public Project createProject(String name, String discordWebhookUrl, String userEmail) {
        User user = userRepository.findByEmail(userEmail)
                .orElseThrow(() -> new RuntimeException("User not found"));

        Project project = Project.builder()
                .name(name)
                .discordWebhookUrl(discordWebhookUrl)
                .user(user)
                .apiKey(generateApiKey())
                .build();

        return projectRepository.save(project);
    }

    public List<Project> getUserProjects(String userEmail) {
        User user = userRepository.findByEmail(userEmail)
                .orElseThrow(() -> new RuntimeException("User not found"));
        return projectRepository.findByUserId(user.getId());
    }

    private String generateApiKey() {
        SecureRandom random = new SecureRandom();
        byte[] bytes = new byte[32];
        random.nextBytes(bytes);
        return "cx_" + Base64.getUrlEncoder().withoutPadding().encodeToString(bytes);
    }
}
