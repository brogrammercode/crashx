package com.crashx.api.services;

import com.crashx.api.models.Crash;
import com.crashx.api.models.Project;
import com.crashx.api.repositories.CrashRepository;
import com.crashx.api.repositories.ProjectRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class CrashService {

    private final CrashRepository crashRepository;
    private final ProjectRepository projectRepository;
    private final DiscordService discordService;

    public Crash reportCrash(String apiKey, Crash crashData) {
        Project project = projectRepository.findByApiKey(apiKey)
                .orElseThrow(() -> new IllegalArgumentException("Invalid API Key"));

        crashData.setProject(project);
        crashData.setStatus(Crash.Status.OPEN);
        
        Crash savedCrash = crashRepository.save(crashData);

        // Async Discord Notification
        discordService.sendCrashAlert(project.getDiscordWebhookUrl(), savedCrash, project.getName());

        return savedCrash;
    }
}
